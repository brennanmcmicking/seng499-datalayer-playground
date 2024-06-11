CREATE TABLE IF NOT EXISTS Users (
    user_id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    username TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    location GEOGRAPHY(POINT,4326) NOT NULL,
    join_date TIMESTAMP NOT NULL,
    items_sold INTEGER[] NOT NULL,
    items_purchased INTEGER[] NOT NULL,
    profile_picture TEXT,
    biography TEXT
);