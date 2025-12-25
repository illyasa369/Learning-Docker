# This page defines the format for Docker compose files.

Note:
- File extension should be .yml
- Images can be built with docker files (see service1) or pre-built images can be used (see service2).

<br> 

```  yml
# Docker Compose file format version
version: "3.8"

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

  # Second service definition
  service2:
    # Use a pre-built image instead of building one
    image: image-name
```
