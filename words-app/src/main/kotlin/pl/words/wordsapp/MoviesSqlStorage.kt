package pl.words.wordsapp

import org.springframework.jdbc.core.JdbcTemplate


class MoviesSqlStorage(private val jdbcTemplate: JdbcTemplate) {
    private val getAllMoviesQuery = "SELECT * FROM movie;"

    fun getMovies(): List<Movie> {
        return jdbcTemplate.query(getAllMoviesQuery,
                { rs, rowNum -> Movie.fromResultSet(rs) })
    }

    fun getMovieWords(id: Int): List<Word> {
        val getMovieWordsQuery =
                "SELECT * FROM word WHERE id in (SELECT word_id FROM movie_word WHERE movie_id = $id);"

        return jdbcTemplate.query(getMovieWordsQuery,
                { rs, rowNum -> Word.fromResultSet(rs) })
    }

}
