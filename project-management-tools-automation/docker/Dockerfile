# Dockerfile for deploying the project

# Base image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy all project files
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Run the data collection script
CMD ["python", "automation/data_collection.py"]
