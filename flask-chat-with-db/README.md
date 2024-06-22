# Python Flask Chat Application witH Persistent Storage

## Getting Started

`poetry install`
`poetry run python ./app.py`

## Database

- Create account with [MongoDB Atlas](https://cloud.mongodb.com/).
- Create a free cluster M0 - designed for learning and exploring MongoDB in a Cloud Environment. This is free for all time as it's a very limited DB.
  - Future suggestion: Run MongoDB in a Docker container alongside this application.
  - Note your credentials for connection, be sure to store them as environment variables (or an appropriate security consideration).
- Continue setup as instructed, and download MongoDB Compass (if desired), for the purposes of the application, PyMongo is preferred.
- Create a Database and Collection (for users), noting the names of both. Example ChatDB and users, respectively.

## Flask-Login