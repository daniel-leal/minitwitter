# Minitwitter

Este projeto foi escrito em python utilizando o microframework
fastapi. É uma simples api de cadastro de usuários

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
