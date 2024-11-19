# Use an official Python runtime as a parent image
FROM python:3.10.12

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the application code and requirements.txt to the container
COPY . .

# Upgrade pip
RUN pip install --upgrade pip

# Install the dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port FastAPI will run on
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
