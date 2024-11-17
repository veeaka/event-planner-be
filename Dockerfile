# Use the official Python image as a base
FROM python:3.10-slim

# Set environment variables to prevent Python from writing pyc files and buffering logs
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory inside the container
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements/local.txt /app/
RUN pip install --no-cache-dir -r local.txt

# Copy the rest of the project files into the container
COPY . /app/

# Expose port 8000 for the Django app
EXPOSE 8000

# Run Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
