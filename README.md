# LATE SHOW API

## Project Description
The Late Show API models relationships between episodes, guests, and their appearances, allowing users to manage and query this data. The database stores information about each episode, guest, and appearance.

## Setup

- Clone the repository.
```bash
git clone https://github.com/crea-tivecoder/Late_show_API.git
cd Late_show_API
```
- Create environment **(optional)** with `pipenv install`, shell using `pipenv shell` & install dependencies with `pip install -r requirements.txt`.

- Create the database with:

```bash
flask db init
flask db migrate -m 'Initial Migration'
flask db upgrade
```

- Run `python seed.py` to seed the database.
- Start the app with `python app.py`.
- Use the URL link together with the API endpoints to run in your postman extension or app.
 For example: `GET http://127.0.0.1:5555/episodes/`


## Project Structure

```bash*
.
├── app.py
├── db.py
├── instance
│   └── lateshow.db
├── migrations
│   ├── alembic.ini
│   ├── env.py
│   ├── __pycache__
│   │   └── env.cpython-311.pyc
│   ├── README
│   ├── script.py.mako
│   └── versions
│       ├── fee4d8eeabb2_initial_migration.py
│       └── __pycache__
│           └── fee4d8eeabb2_initial_migration.cpython-311.pyc
├── models
│   ├── appearance.py
│   ├── episode.py
│   ├── guest.py
│   ├── __init__.py
│   └── __pycache__
├── __pycache__
│   ├── app.cpython-311.pyc
│   └── db.cpython-311.pyc
├── README.md
├── requirements.txt
├── routes
│   ├── appearance_routes.py
│   ├── episode_routes.py
│   ├── guest_routes.py
│   └── __pycache__
├── seed.py
└── utils
    └── challenge-4-lateshow.postman_collection.json
```

## Project Preview

- **`app.py`**
Main entry point for the Flask application, responsible for running the server

- **`db.py`**
Handles the database setup and initialization using SQLAlchemy

- **`seed.py`**
Populates the database with initial data for episodes, guests, and appearances

- **`requirements.txt`**
Lists the dependencies required for the project, including Flask and SQLAlchemy

- **instance**
A directory for storing application-specific files like the SQLite database

- ***instance/`lateshow.db`***
SQLite database file that holds all the data for the application

- **migrations**
Directory that manages database schema migrations

- ***migrations/versions/***
Contains versioned migration scripts that track schema changes over time

- **models**
Directory containing the data models for episodes, guests, and appearances

- ***models/`__init__.py`***
Initializes the models package for use within the application

- ***models/`episode.py`***
Defines the Episode model, representing TV show episodes in the database

- ***models/`guest.py`***
Defines the Guest model, representing individual guests in the database

- ***models/`appearance.py`***
Defines the Appearance model, linking episodes and guests in the database

- **routes**
Directory containing API route definitions for managing episodes, guests, and appearances

- ***routes/`episode_routes.py`***
Contains API routes for creating, retrieving, and managing episodes

- ***routes/`guest_routes.py`***
Contains API routes for creating, retrieving, and managing guests

- ***routes/`appearance_routes.py`***
Contains API routes for creating, retrieving, and managing appearances of guests on episodes

- **utils**
Directory for utility files, such as the Postman collection for testing the API

## Endpoints

### Guests

- `GET /guests`: Get all guests.
- `GET /guests/<id>`: Get a specific guest by ID.

### Episodes

- `GET /episodes`: Get all episodes.
- `GET /episodes/<id>`: Get a specific episode by ID.

### Appearances

- `POST /appearances`: Create a new `Appearance` that is associated with an existing `Episode` and `Guest`

#### NOTE

Ensure the body section of postman has a raw json structure as:

```bash
{
  "rating": 5,
  "episode_id": 100,
  "guest_id": 123
}
```

