FROM python:3.11

# Set the working directory of the application
WORKDIR /app

# Install FFmpeg
RUN apt-get update \
    && apt-get install -y ffmpeg \
    && rm -rf /var/lib/apt/lists/*poe

# Install Poetry for dependency management
RUN pip install poetry

# Install dependencies using Poetry
COPY pyproject.toml poetry.lock* /app/
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Copy the rest of your application's code
COPY ./backend /app/backend

# Set the command to run your application
CMD ["uvicorn", "backend.app:app", "--host", "0.0.0.0"]