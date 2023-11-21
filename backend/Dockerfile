# Use a base image
FROM python:3-alpine3.15

# Set the working directory
WORKDIR /app

# Copy the app files to the working directory
COPY . /app
# upgrade pip 
RUN pip install --upgrade pip
# Install the dependencies
RUN pip install --no-cache-dir flask

# Expose the Flask app's port
EXPOSE 5000

# Set the entrypoint command
CMD ["python", "app.py"]