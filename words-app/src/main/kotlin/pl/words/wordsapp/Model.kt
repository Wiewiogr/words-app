
package pl.words.wordsapp

import java.sql.ResultSet


data class Movie(val id: Int, val title: String, val posterUrl: String) {
    companion object {
        @JvmStatic
        fun fromResultSet(rs: ResultSet) = Movie(
                rs.getInt("id"),
                rs.getString("title"),
                rs.getString("poster_url")
        )
    }
}

data class Word(val id: Int, val content: String, val meaning: String) {
    companion object {
        @JvmStatic
        fun fromResultSet(rs: ResultSet) = Word(
                rs.getInt("id"),
                rs.getString("content"),
                rs.getString("meaning")
        )
    }
}