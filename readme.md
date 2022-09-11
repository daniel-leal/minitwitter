# Minitwitter

This project was written in python using fastapi microframework. It's just a simple register api.

## Libs

- fastapi (microframework)
- sqlalchemy (orm)
- alembic (migrations)
- psycopg2 (postgresql)
- bcrypt (encode pw)
- flake8, black isort (style guide)

## How to run with docker

```bash
$ docker compose build
```

```bash
$ docker compose up
```

access api docs:
[http://localhost:8000/docs](http://localhost:8000/docs)

## How to run local

- Create `.env` file base on `.env.dist` and put your local database envs.
- Install dependencies `pip install -r requirements.txt`
- Run migrations: `alembic upgrade head`
- Run server: `uvicorn main:app --reload`
