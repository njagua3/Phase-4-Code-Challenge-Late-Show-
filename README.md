# TV Show API

This project is a RESTful API for managing TV shows, episodes, and guest appearances. It allows users to retrieve and manage data related to TV shows, including episode details, guest information, and ratings for guest appearances.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Models](#models)

## Features

- Create, read, update, and delete (CRUD) operations for episodes and guests.
- Manage guest appearances in episodes with ratings.
- Simple and intuitive API responses in JSON format.
- Built using Flask, SQLAlchemy, and SQLite.

## Technologies Used

- **Flask**: A lightweight WSGI web application framework for Python.
- **SQLAlchemy**: An SQL toolkit and Object-Relational Mapping (ORM) library for Python.
- **Flask-Migrate**: A tool that handles SQLAlchemy database migrations for Flask applications.
- **SQLite**: A lightweight database engine for development and testing.

## Installation

Follow these steps to set up the project locally:

1. **Clone the repository:**


   git clone paste ssh
   
Create a virtual environment:


python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install the required packages:


pip install -r requirements.txt
Initialize the database:


flask db init
flask db migrate -m "Initial migration"
flask db upgrade
Run the application:


python app.py
Access the API at http://127.0.0.1:5000/

Usage
After running the application, you can access the API endpoints using tools like Postman or cURL.
API Endpoints
Root Endpoint
GET /
Returns a welcome message for the TV Show API.
Episodes
GET /episodes
Retrieve all episodes.

GET /episodes/<id>
Retrieve a specific episode by ID.

POST /episodes
Create a new episode.
Request Body:

json
Copy code
{
    "date": "YYYY-MM-DD",
    "number": "Episode Number"
}
PUT /episodes/<id>
Update an existing episode by ID.
Request Body:

json

{
    "date": "YYYY-MM-DD",
    "number": "Episode Number"
}
DELETE /episodes/<id>
Delete an episode by ID.

Guests
GET /guests
Retrieve all guests.

GET /guests/<id>
Retrieve a specific guest by ID.

POST /guests
Create a new guest.
Request Body:

json

{
    "name": "Guest Name",
    "occupation": "Guest Occupation"
}
PUT /guests/<id>
Update an existing guest by ID.
Request Body:


{
    "name": "Guest Name",
    "occupation": "Guest Occupation"
}
DELETE /guests/<id>
Delete a guest by ID.

Appearances
GET /appearances
Retrieve all guest appearances.

GET /appearances/<id>
Retrieve a specific appearance by ID.

POST /appearances
Create a new appearance.
Request Body:

json
Copy code
{
    "rating": "1-5",
    "episode_id": "Episode ID",
    "guest_id": "Guest ID"
}
PUT /appearances/<id>
Update an existing appearance by ID.
Request Body:

json

{
    "rating": "1-5",
    "episode_id": "Episode ID",
    "guest_id": "Guest ID"
}
DELETE /appearances/<id>
Delete an appearance by ID.

Models