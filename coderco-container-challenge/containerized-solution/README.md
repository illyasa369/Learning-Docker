### This solution containerizes both the Redis database and the Python web app.
- It is important that a Docker network is created and both containers are connected to the same network.
```
docker network create challenge-network
```
<br>
- Redis container is run using a pre-built Redis image.

```
docker run -d -p 6379:6379 --name redisdb redis:alpine
docker network connect challenge-network redisdb
```

<br>
- Python container is built using the Dockerfile.

```
docker build -t webapp:latest .
docker run -d -p 5000:5000 --name pythonwebapp --network challenge-network  webapp:latest
```

<br>
<img width="1602" height="249" alt="Image" src="https://github.com/user-attachments/assets/38cf40dc-2015-43ea-bf89-ad4c6d9b714d" />
