import cleanup
import parser
import words
import downloader
import movies
import db
import translation

access_key = ""
secret_key = ""
bucket = ""
region_name = ""
endpoint_url = ""

spaces_client = downloader.SpacesClient(access_key, secret_key, bucket, region_name, endpoint_url)
movie_paths = spaces_client.get_list("new-data")[1:]

omdb_token = ""
movies_client = movies.OMDBMoviesClient("http://www.omdbapi.com/", omdb_token)

db_client = db.MySQLClient()

movies_words = {}


for path in movie_paths:
    year_title = path.split("/")[-2].split("-")
    year = int(year_title[0])
    title = "-".join(year_title[1:])
    movie = movies_client.get_movie_details(title, year)

    if db_client.movie_exists(movie):
        print("Skipping movie")
        continue

    subtitles = spaces_client.get_subtitles_as_string(path)
    word_list = parser.parse_srt_format(subtitles)

    cleaned_words = cleanup.cleanup(word_list)
    word_count = words.count_word_counts(cleaned_words)
    word_stats = words.add_zipf_frequency(word_count)

    proper_words = list(filter(words.is_proper, word_stats))

    for word in sorted(proper_words, key=lambda x: words.compute_score(x), reverse=True):
        print(word.content, word.count, word.zipf_frequency, words.compute_score(word))

    movies_words[movie] = list(map(lambda w: w.content, proper_words))
    break


already_added_words = {}
movies_words_id = {}

for movie, movie_words in movies_words.items():

    word_ids = []
    for word in movie_words:
        word_id = -1
        if word in already_added_words:
            word_ids.append(already_added_words[word])
            continue

        word_id = db_client.get_word_id(word)

        if word_id != None:
            word_ids.append(word_id)
            already_added_words[word] = word_id
            continue

        word_with_meaning = translation.to_word_with_meaning(word)
        word_id = db_client.add_word_and_get_id(word_with_meaning)
        word_ids.append(word_id)
        already_added_words[word] = word_id

    db_client.add_movie_with_words(movie, word_ids)

