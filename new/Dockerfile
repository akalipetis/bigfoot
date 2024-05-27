ARG DOCKERIZE_VERSION=0.16.0
ARG PYTHON_VERSION=3.12

# Dockerize
FROM powerman/dockerize:$DOCKERIZE_VERSION as dockerize

# Python
FROM python:$PYTHON_VERSION

COPY --from=dockerize /usr/local/bin/dockerize /usr/local/bin/dockerize

# Install Poetry
ARG POETRY_VERSION=1.8.3
ARG POETRY_ARGS=--without=dev
ENV POETRY_HOME=/opt/poetry\
    PATH="${PATH}:/opt/poetry/bin"
RUN python3 -m venv ${POETRY_HOME} &&\
    ${POETRY_HOME}/bin/pip install poetry==${POETRY_VERSION} &&\
    poetry config virtualenvs.create false

WORKDIR /usr/src/app
COPY poetry.lock pyproject.toml ./
RUN poetry check && poetry check --lock && poetry install ${POETRY_ARGS}

COPY ./ ./
RUN poetry run python manage.py collectstatic --noinput

CMD ["gunicorn", "bigfoot_django.wsgi", "--log-file=-", "--access-logfile=-", "--bind", "0.0.0.0"]
