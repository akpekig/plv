# Use an official Python runtime as a base image
FROM python:3.10-alpine as base

# Set the working directory
WORKDIR /api

# Copy only the requirements file to optimize caching
COPY requirements.txt .

# Install dependencies
RUN apk --no-cache add build-base libffi-dev openssl-dev && \
    pip install --no-cache-dir -r requirements.txt && \
    apk del build-base libffi-dev openssl-dev

# Copy the application code
COPY . .

# Expose the port that Flask will run on
EXPOSE 5000
ENV FLASK_APP=app.py

# Run the application
CMD ["flask", "run", "--host", "0.0.0.0"]

