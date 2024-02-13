FROM python:3.11
WORKDIR /app

# Install FFmpeg
RUN apt-get update \
    && apt-get install -y ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry for dependency management
RUN pip install poetry

COPY pyproject.toml poetry.lock* /app/

# Install dependencies using Poetry
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Copy the rest of your application's code
COPY .. /app

# Set the command to run your application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0"]