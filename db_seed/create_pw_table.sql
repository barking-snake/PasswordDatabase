CREATE TABLE pw (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER FOREIGN KEY NOT NULL,
    username varchar(16) NOT NULL,
    password BLOB NOT NULL,
    password_type varchar(24) NOT NULL,
    short_desc varchar(16) NOT NULL,
    long_desc varchar(140)
);

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username varchar(16) NOT NULL,
    password BLOB NOT NULL
);