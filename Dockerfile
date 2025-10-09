FROM python:3.12-slim

WORKDIR /usr/src/app

COPY pyproject.toml uv.lock .python-version ./

RUN pip install uv

RUN uv sync

COPY ./src ./src
