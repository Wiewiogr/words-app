import MySQLdb
import movies
import translation


class MySQLClient:
    def __init__(
        self, host="127.0.0.1", port=3306, user="root", passwd="password", db="test_db"
    ):
        self.db = MySQLdb.connect(host=host, port=port, user=user, passwd=passwd, db=db)

    def add_movie_with_words(self, movie, words_ids):
        cur = self.db.cursor()
        movie_sql = (
            'INSERT INTO movie(title, year, poster_url) VALUES("%s",%d ,"%s");'
            % (movie.title, movie.year, movie.poster_url)
        )
        try:
            print(movie_sql)
            cur.execute(movie_sql)
            cur.execute("SELECT LAST_INSERT_ID();")
            movie_id = cur.fetchone()[0]

            for word_id in words_ids:
                movie_word_sql = (
                    "INSERT INTO movie_word(movie_id, word_id) VALUES(%d,%d);"
                    % (movie_id, word_id)
                )
                cur.execute(movie_word_sql)

            self.db.commit()
        except:
            print("rollback is needed")
            self.db.rollback()

    def movie_exists(self, movie):
        cur = self.db.cursor()
        sql = 'SELECT id FROM movie WHERE title="%s";' % (movie.title)
        cur.execute(sql)
        return cur.fetchone() != None

    def get_word_id(self, word):
        cur = self.db.cursor()
        sql = 'SELECT id FROM word WHERE content="%s";' % (word)
        cur.execute(sql)
        result = cur.fetchone()
        if result != None:
            return result[0]
        else:
            return None

    def add_word_and_get_id(self, word):
        sql = 'INSERT INTO word(content, meaning) VALUES("%s","%s");' % (
            word.content,
            word.meaning,
        )
        cur = self.db.cursor()
        try:
            cur.execute(sql)
            cur.execute("SELECT LAST_INSERT_ID();")
            id = cur.fetchone()[0]
            self.db.commit()
            return id
        except:
            print("rollback is needed")
            self.db.rollback()
            return -1


if __name__ == "__main__":
    client = MySQLClient()
    # client.add_movie_with_words(movies.Movie("title", 1995, "url"), [2,5,8,9])
    # print(client.movie_exists(movies.Movie("title", 1995, "url")))
    print(client.get_word_id(translation.Word("dupa", "sfasdf")))
    # print(client.add_word_and_get_id(translation.Word("dupa", "sfasdf")))
