# Docker commands

## Image commands
```
docker build -t image-name . ||| Builds an image in the directory of the Dockerfile specifed by . (current directory)
docker images |||  Shows created images. Can be used to verify that an image has been built.
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
```

## Network commands
```
docker network create network-name ||| Creates a docker network.
docker network list ||| Lists all Docker networks.

```
