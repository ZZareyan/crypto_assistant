FROM python:3.12-slim

WORKDIR /app

RUN pip install uv

COPY pyproject.toml .
RUN uv sync --no-dev

COPY app/ app/
COPY alembic/ alembic/
COPY alembic.ini .

CMD ["uv", "run", "python", "-m", "app.main"]
