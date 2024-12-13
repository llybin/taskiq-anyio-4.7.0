ARG REPOSITORY
FROM ${REPOSITORY}python:3.12.7-slim-bullseye

EXPOSE 8003/tcp

ENV TZ=Etc/UTC \
	DEBIAN_FRONTEND=noninteractive \
	DJANGO_SETTINGS_MODULE=ggg.settings \
	# https://docs.python.org/3.12/using/cmdline.html
	PYTHONFAULTHANDLER=1 \
	PYTHONUNBUFFERED=1 \
	# https://github.com/pypa/pip/blob/master/src/pip/_internal/cli/cmdoptions.py
	PIP_NO_CACHE_DIR=on \
	PIP_DISABLE_PIP_VERSION_CHECK=on \
	PIP_DEFAULT_TIMEOUT=100 \
	# https://docs.pytest.org/en/8.3.x/explanation/pythonpath.html
	PYTEST_ADDOPTS='--import-mode=importlib' \
	# https://python-poetry.org
	PKG_POETRY_VERSION=1.8.4 \
	# https://pypi.org/project/pip/
	PKG_PIP_VERSION=24.3.1

# Install system dependencies
RUN apt-get update \
	&& apt-get install --assume-yes --no-install-recommends --no-install-suggests \
		tini \
	&& rm -rf /var/lib/apt/lists/*

# Copy only requirements to cache them in a docker layer
WORKDIR /app
COPY ./poetry.lock ./pyproject.toml /app/

# Install application dependencies and clean
RUN set -ex \
	&& pip install --upgrade pip==$PKG_PIP_VERSION \
	&& pip install "poetry==$PKG_POETRY_VERSION" \
	&& poetry config virtualenvs.create false \
	&& poetry install --no-interaction --no-ansi

COPY ./docker/entrypoint.sh /app/
COPY ./docker/scripts/wait-for-it.sh /app/

# Copy application files
COPY src /app/src

# Set the workdir
WORKDIR /app/src

# Create the entrypoint
ENTRYPOINT ["/usr/bin/tini", "--", "/app/entrypoint.sh"]
