package pl.words.wordsapp

import org.springframework.context.annotation.Bean
import org.springframework.context.annotation.Configuration
import org.springframework.jdbc.core.JdbcTemplate
import org.springframework.jdbc.datasource.DriverManagerDataSource
import javax.sql.DataSource


@Configuration
class SqlStorageConfiguration {

    @Bean
    fun moviesSqlStorage(jdbcTemplate: JdbcTemplate) = MoviesSqlStorage(jdbcTemplate)

    @Bean
    fun jdbcTemplate(dataSource: DataSource) = JdbcTemplate(dataSource)

    @Bean
    fun dataSource(): DriverManagerDataSource {
        val dataSource = DriverManagerDataSource()

        dataSource.setDriverClassName("com.mysql.jdbc.Driver")
        dataSource.setUsername("root")
        dataSource.setPassword("password")
        dataSource.setUrl("jdbc:mysql://127.0.0.1:3306/test_db")
        return dataSource
    }
}