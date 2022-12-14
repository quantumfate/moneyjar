# Start from a base image with Python and the Flask web framework installed
FROM python:3.8-slim-buster

# Install the dependencies for the backend
RUN pip install -r backend/requirements.txt

# Install the dependencies for the frontend
RUN npm install -g create-react-app react-native typescript

# Copy the code for the backend and frontend into the image
COPY backend /app/backend
COPY frontend /app/frontend

# Set the working directory to the backend code
WORKDIR /app/backend

# Expose the port where the backend will be listening for requests
EXPOSE 5000

# Set the default command to run when the container starts
CMD ["python", "app.py"]