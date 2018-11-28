[![Build Status](https://travis-ci.org/nikoskef/escape-api-alchemy.svg?branch=master)](https://travis-ci.org/nikoskef/escape-api-alchemy)

## Escape Room Api Flask/SqlAlchemy

This Rest Api app is created using [Flask](http://flask.pocoo.org/),
 [JWT-Extended](https://flask-jwt-extended.readthedocs.io/en/latest/)
 and [Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.3/).
The Flask app deals with rooms and users.

## Hosted

It is hosted on [Digital Ocean](https://www.digitalocean.com/) and its domain name is [rooms-escape.com](https://rooms-escape.com/rooms).

## End Points

The end point of the application are:
- Room, '/room/<int:_id>'
- RoomCreate, '/room/create'
- RoomList, '/rooms'
- UserRegister, '/register'
- User, '/user/<int:user_id>'
- UserLogin, '/login'

## Tests

For the end points, there are unit tests, integration tests and system tests.
Continuous Integration using [TravisCI](https://travis-ci.org/nikoskef/escape-api-alchemy/builds/)

## Updated App

An updated app can be found [here](https://github.com/nikoskef/rest-api-marsh) with full documentation
