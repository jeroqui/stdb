FROM python:3.9.5


ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.3.1 \
    ENV_NAME="Production"

# System deps:
RUN pip install "poetry==$POETRY_VERSION"

WORKDIR /backend-code
COPY poetry.lock pyproject.toml /backend-code/
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-root \
    && poetry add psycopg2 hypercorn

# Creating folders, and files for the project:
COPY . /backend-code/
RUN chmod 755 production-entrypoint.sh

CMD "/backend-code/production-entrypoint.sh"
