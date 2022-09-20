# brit-takehome-task

## Features

- **FastAPI** with Python 3.10
- **React Admin** with Typescript
- Postgres 14
- SqlModel with Alembic for migrations
- Pytest for backend tests
- Jest for frontend tests
- Prettier/Eslint (with Airbnb style guide)
- Docker compose for easier development
- Nginx as a reverse proxy to allow backend and frontend on the same port

## Development

The only hard dependencies for this project are docker and docker-compose.

### Quick Start

Starting the project with hot-reloading enabled
(the first time it will take a while):

```bash
chmod +x scripts/build.sh
./scripts/build.sh
```

```bash
docker-compose up
```

And navigate to http://localhost:8000

_Note: If you see an Nginx error at first with a `502: Bad Gateway` page, you may have to wait for webpack to build the development server (the nginx container builds much more quickly)._

Auto-generated docs will be at
http://localhost:8000/api/docs

### Rebuilding containers:

```
docker-compose build
```

### Restarting containers:

```
docker-compose restart
```

### Bringing containers down:

```
docker-compose down
```

### Frontend Development

Alternatively to running inside docker, it can sometimes be easier
to use npm directly for quicker reloading. To run using npm:

```
cd frontend
npm install
npm start
```

This should redirect you to http://localhost:3000

### Frontend Tests

```
cd frontend
npm install
npm test
```

## Migrations

Migrations are run using alembic. To run all migrations:

```
docker-compose run --rm backend alembic upgrade head
```

To create a new migration automatically:

After you have created a new model or altered and existing models run
```
docker-compose run --rm backend alembic revision -m "create users table" --autogenerate
```
This will detect changes between your model definitions and the database schema and generate
migrations scripts accordingly.

If you need more control you can also create migrations manually. For more information see
[Alembic's official documentation](https://alembic.sqlalchemy.org/en/latest/tutorial.html#create-a-migration-script).

## Testing

There is a helper script for both frontend and backend tests:

```
./scripts/test.sh
```

### Backend Tests

```
docker-compose run backend pytest
```

any arguments to pytest can also be passed after this command

### Frontend Tests

```
docker-compose run frontend test
```

This is the same as running npm test from within the frontend directory

## Logging

```
docker-compose logs
```

Or for a specific service:

```
docker-compose logs -f name_of_service # frontend|backend|db
```

TODO:
Add `pre-commit-config` to validate commits with
- mypy
- black
- isort
- flake8 / pylint
- prettier
- eslint