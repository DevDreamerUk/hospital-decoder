from yoyo import step

steps = [
    step(
        """
         CREATE SCHEMA IF NOT EXISTS general;
        """
    ),

    step(
        """
        CREATE TABLE IF NOT EXISTS general.report (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            path VARCHAR(100) NOT NULL,
            created_at timestamp NOT NULL
        );
        """,

    )
]