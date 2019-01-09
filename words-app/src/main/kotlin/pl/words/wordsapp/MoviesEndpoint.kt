package pl.words.wordsapp

import org.springframework.web.bind.annotation.GetMapping
import org.springframework.web.bind.annotation.PathVariable
import org.springframework.web.bind.annotation.RestController


@RestController
class MoviesEndpoint(val moviesStorage: MoviesSqlStorage) {

    @GetMapping("/movie")
    fun getAllMovies() = moviesStorage.getMovies()

    @GetMapping("/movie/{id}/word")
    fun geMovieWords(@PathVariable("id") id: Int) = moviesStorage.getMovieWords(id)
}
