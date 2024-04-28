# Base image - Use a slim Python image for efficiency
FROM python:3.9-slim

# Set a working directory inside the container
WORKDIR /app/app

# Copy the requirements file first (optimizes caching)
COPY requirements.txt ./

# Install Python packages from requirements
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy the rest of your project files
COPY . /app

# Google Cloud Run will set the PORT environment variable to tell you what port to listen to
ENV PORT=8080

# Expose the port your FastAPI app will listen on
EXPOSE $PORT

# Command to start the application (using uvicorn)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--reload", "--log-config=log_conf.yaml"]
