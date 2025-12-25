# Commands for pushing and pulling images to and from an AWS ECR repository.

##### Ensure you have authenticated your Docker client to the Amazon ECR registry using the AWS CLI before attempting to push or pull images.
##### See the “View push commands” section in the ECR management console for the required login command.
<br>

### 1. Build the Docker image with the following command.
```
docker build -t repository-name . #
```
###### Note: If no tag is specified (```repository-name:tag```), the default tag ```latest``` is used.
<br>

### 2. Tag the image.
```
docker tag repository-name:tag ECR-image-URI:tag
```
###### Note:
- See AWS ECR for the image URI.
- Ensure the image tag is included after the ECR image URI (ECR-image-URI:tag).
<br>

### 3. Push the image to the AWS repository.
```
docker push repository-name:tag
```

### To pull an image from your ECR repository use the following command.
```
docker pull repository-name:tag
```
