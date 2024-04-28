FROM python:3.10

RUN pip install poetry
WORKDIR /bot
COPY . .
RUN poetry install --without dev

ENTRYPOINT [ "poetry", "run", "python", "united_batchery_bot" ]