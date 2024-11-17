# Use the official Python image as a base
FROM python:3.10-slim

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
