# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app/

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside the container
EXPOSE 8000

# Define environment variable for Django settings
ENV PYTHONUNBUFFERED 1

# Run Django's development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
