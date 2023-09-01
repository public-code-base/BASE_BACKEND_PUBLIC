# Use the official Python base image
FROM python:3.10

# Set the working directory
WORKDIR /app

# Copy only the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

# Copy the application files into the container
COPY . /app

# Install required dependencies (if any)
RUN pip install -r requirements.txt

# Expose the port the app runs on
# EXPOSE 8989

# Start the application
CMD ["python", "initialize_main.py"]
