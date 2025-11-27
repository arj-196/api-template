This is a api template repository. It doesn't do anything yet.
You can use this repository as a starting point for building your own API.


Product structure and important files:

- **Git related**:
  - `.gitignore`: This file specifies which files and directories to ignore in the git repository.

- **Python related**:
  - `poetry.lock` and `pyproject.toml`: These files are used by Poetry to manage project dependencies and settings.

- **Environment variables**:
  - We have 2 env files: 
    - `.env` contains all the sensitive information which is not tracked in git. So this file needs to be created manually.
    - `.env.docker.env` file is used to configure our app in docker.
    - All the default variable settings are set for local out of docker environment so that the app can run outside docker containers. This makes using debugging tools much easier.

- **Docker related**:
  - `docker-compose.yml`: This file defines the services, networks, and volumes for our multi-container Docker application.
  - `Dockerfile`: This file contains the instructions to build Docker images for all our services.

- **CI/CD related**:
  - `.gitlab-ci.yml`: This file contains the CI/CD pipeline configuration for GitLab.
    - The pipeline assumes that we are using Azure as our cloud provider.


- **Common module**:
  - `common`: This directory contains common utilities and modules that can be shared across different parts of the application.
    - `common/settings.py`: This file contains the application settings and configuration.

- **Database related**:
  - For this example we are using Postgres as our database. The database service is defined in the `docker-compose.yml` file.
  - `alembic.ini`: This is the configuration file for Alembic.
  - `db_sql`: This directory contains the database configuration and migration scripts.
    - `db_sql/versions`: This directory contains the migration scripts for the database.
    - `db_sql/models.py`: This file contains the database models defined using SQLAlchemy.
      - Note that in the services we don't work directly with the SQLAlchemy instances, rather we convert them to Pydantic models and work with those.


- **API related**:
  - `api`: This directory contains the code to configure the api (currently using fastapi).
    - Other api related logic like "Authentication" will be defined here.
    - Note that the actual api routes are not defined in this directory. They should be defined in their dedicated service module as routers.

- **Service module**:
  - `service`: This directory contains the main service logic of the application.
    - Each service should have its own subdirectory here.
    - Each service should define its own api routes as FastAPI routers.
    - Each service should define its own business logic and operations.

- **Service Dataset module**:
  - `service/dataset`: This directory contains the a simple service that manages datasets in our app. We can get, create and delete datasets.
    - `service/dataset/models.py`: This file contains the Pydantic models related to datasets.
    - `service/dataset/db.py`: This file contains the database operations related to datasets.
    - `service/dataset/routes.py`: This file contains the FastAPI router for dataset-related API endpoints.

- **Integration tests**:
  - `integration_tests`: This directory contains the integration tests for the application.
    - `integration_tests/conftest.py`: This file contains the pytest fixtures for the integration tests.

