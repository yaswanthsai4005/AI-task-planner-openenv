FROM python:3.10

WORKDIR /app
COPY . .

RUN pip install openenv-core openai pydantic

CMD ["openenv", "serve"]
