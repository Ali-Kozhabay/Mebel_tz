# Use Python slim image
FROM python:3.13

# Set work directory
WORKDIR /tz_project

# Install Poetry
RUN pip install --upgrade pip && pip install poetry

# Configure Poetry to not create virtual environment
RUN poetry config virtualenvs.create false

# Copy Poetry files
COPY pyproject.toml poetry.lock* ./

# Install dependencies without installing the project itself
RUN poetry install --no-root

# Copy all project files
COPY . .

# Run the application
CMD ["poetry", "run", "python", "-m", "app"]
