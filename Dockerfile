ARG PYTHON_VERSION=3.10

# BASE IMAGE
FROM python:${PYTHON_VERSION}-slim-bullseye AS base

# Set time zone to France
ENV TZ=Europe/Paris

RUN apt update -y && apt upgrade -y

# Create the user
ENV USER=app
RUN useradd --create-home $USER
WORKDIR /home/$USER


# BUILDER IMAGE
FROM base AS builder
ARG GITLAB_USERNAME
ARG GITLAB_TOKEN

# Install `poetry`
ENV \
  POETRY_HOME=/etc/poetry \
  POETRY_VERSION=2.2.0 \
  POETRY_VIRTUALENVS_IN_PROJECT=true
RUN apt install -y --no-install-recommends \
    curl \
    unzip \
    build-essential \
  && curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="$POETRY_HOME/bin:$PATH"

# Activate user
USER $USER

# Force initalise poetry to create the virtual environment
RUN poetry init --no-interaction

# ---
# Dashboard image

# BUILD IMAGE DASHBOARD
FROM builder AS build-dashboard

# Copy migrations config
COPY pyproject.toml poetry.lock ./

# Install runtime dependencies
RUN poetry install --only main --only dashboard

# ---
# Runtime image

# BUILD RUNTIME IMAGE
FROM builder AS build-runtime
ARG GITLAB_USERNAME
ARG GITLAB_TOKEN

# Copy migrations config
COPY pyproject.toml poetry.lock ./

# Install runtime dependencies
RUN poetry install --only main


# RUNTIME IMAGE
FROM base AS runtime

ENV PYTHONUNBUFFERED=1

# Copy virtualenv from the builder
COPY --from=build-runtime /home/$USER/.venv /home/$USER/.venv

# Activate virtualenv
ENV PATH="/home/$USER/.venv/bin:$PATH"
# Change logs directory permissions
RUN mkdir /logs && chown -R $USER:$USER /logs

# Copy packages
COPY api api
COPY service service
COPY common common
COPY db_sql db_sql
COPY alembic.ini alembic.ini

COPY pyproject.toml pyproject.toml

# Activate user
USER $USER

