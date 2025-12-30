# This page defines the format for Docker compose files.

Note:
- Docker compose files should be named 'docker-compose.yml' as this is the file that is looked for when running docker compose.
- Images can be built with Docker files (see service1) or pre-built images can be used (see service2).

<br> 

```  yml
# Defines all containers that make up the application
services:

  # First service definition
  service1:

    # Build the image using a Dockerfile located in the specified directory. Pre-built images can be used instead (see service2).
    build: /dir/of/Dockerfile

    # Map a port on the host machine to a port inside the container
    ports:
      - "localPort:containerPort"

    # This service depends on service2, Docker compose ensures service2 is started before service1.
    depends_on:
      - service2

    # This service uses volumes defined below.
    volumes:
      # Mount a named volume to a path inside the container. If the volume does not exist, it is created.
      - volume-name:/path/in/container

  # Second service definition
  service2:
    # Use a pre-built image instead of building one.
    image: image-name

    # Expose a port inside the container for internal communication.
    # Not accessible by the host.
    expose:
      - "containerPort"

    # Overwrites a file in the container with the version from the host machine.
    volumes:
      - ./file.txt:/app/file.txt

    # Creates environment variables usable inside the container.
    environment:
      variable-name: value
    
# Define named volumes used by services
volumes:
  # Create a named volume with default settings
  volume-name:
