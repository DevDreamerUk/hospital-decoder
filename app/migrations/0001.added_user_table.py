from yoyo import step

steps = [
    step(
        """
         CREATE SCHEMA IF NOT EXISTS social;
        """
    ),

    step(
        """
        CREATE TABLE hospital_decoding.social.user (
        id SERIAL PRIMARY KEY,
        username TEXT UNIQUE NOT NULL,
        email TEXT UNIQUE,
        password_hash TEXT NOT NULL,
        created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT now(),
        updated_at TIMESTAMP WITHOUT TIME ZONE
);
        """,

    )
]