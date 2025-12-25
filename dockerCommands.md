# Docker commands

```
docker system prune ||| Removes all unused containers, images, networks and cache.
```

## Image commands
```
docker build -t image-name . ||| Builds an image in the directory of the Dockerfile specifed by . (current directory)

docker build -t dockerhub-username/repository:tag . ||| Builds a Docker image and tags it for Docker Hub.

docker images |||  Shows created images. Can be used to verify that an image has been built.

docker inspect image-ID ||| Shows comprehensive information about an image.

docker rmi image-name ||| Removes a Docker image.

docker rmi -f image-name ||| Forcefully removes a Docker image.
```

## Container commands
```
docker run image-name ||| Runs an image
docker run -d --name container-name --network network-name -p localPort:containerPort image-name ||| -d tag runs the image in the background.
                                                                                                 ||| -p allows the container's port to map to the host's port.
                                                                                                 ||| --name allows the name of the container to be specified.
                                                                                                 ||| --network specifies which network the container should be assigned to.
docker ps ||| Shows containers that are currently running.
docker ps -a ||| Shows all containers (including stopped ones).

docker stop [containerID or name] ||| Stops a container.

docker rm [containerID or name] ||| Removes a container.
docker container prune ||| Removes all containers.
```

## Network commands
```
docker network create network-name ||| Creates a Docker network.

docker network connect network-name container-name ||| Connects the specified container to the specified network.

docker network ls ||| Lists all Docker networks.

docker network rm network-name ||| Removes the specified network. 
```

## Compose commands
```
docker compose up -d ||| Starts all services defined in your docker-compose.yml in the background (due to -d tag).

docker compose ps ||| Lists running containers from the Compose project.

docker compose down ||| Stops and removes all containers, networks and volumes created from 'docker compose up' command.

docker compose stop ||| Stops running containers.

docker compose start ||| Restarts running containers.
```

## Docker Hub commands
```
docker login ||| Log in to Docker Hub.

docker push dockerhub-username/repository:tag ||| Pushes a local image to your Docker Hub repository.

docker pull dockerhub-username/repository:tag ||| Pulls an image from Docker Hub.
```
