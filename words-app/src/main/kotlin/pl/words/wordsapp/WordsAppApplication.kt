package pl.words.wordsapp

import org.springframework.boot.autoconfigure.SpringBootApplication
import org.springframework.boot.runApplication

@SpringBootApplication
class WordsAppApplication

fun main(args: Array<String>) {
    runApplication<WordsAppApplication>(*args)
}
