# Use an image with Python 3.8 installed.
# -slim tag specifies a minimal image to be used.
FROM python:3.8-slim

# Specifies the /app as the working directory in the container.
WORKDIR /app

# Copies the content of the current directory (where the docker file is)
# to the the current directory of the container (at this point the current directory
# of the container is /app).
COPY . .

# Installs flask inside the container.
RUN pip install flask

# Document that the app listens on port 5000.
EXPOSE 5000

# 'python simpleWebApp.py' is ran when the container start which runs the python application.
CMD ["python", "simpleWebApp.py"]
