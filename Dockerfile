FROM python:3.12-slim

ENV POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

RUN pip install --no-cache-dir poetry

RUN poetry --version

WORKDIR /app

COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root

COPY src ./src

WORKDIR /app/src

CMD ["sh", "-c", "poetry run alembic upgrade head && poetry run python run.py"]
