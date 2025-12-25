# Flask Web App Connected to MySQL via Docker Network

## Steps to run the web app:
```
# Create the Docker network.
docker network create my-network

# Run an SQL image which the web app container will connect to.
docker run -d --name mydb --network my-network -e MYSQL_ROOT_PASSWORD=my-secret-pw mysql:8

# Build the image of the web app.
docker build -t webapp-with-db .

# Run a container from the Docker image.
docker run -d --network my-network --name webapp2 -p 5001:5001 webapp-with-db

View the result at http://localhost:5001
```
<img width="1482" height="274" alt="Image" src="https://github.com/user-attachments/assets/0d889a9f-4ffc-44b8-b8cb-c229fec29f4c" />
