##### See below for more information on Dockerfiles.<br><br>

## Dockerfile format for a basic image build.
 ```
# Choose the base image (usually a Linux image with a runtime installed)
FROM <base-image>

# Set (and create if needed) the working directory inside the container
WORKDIR <working-directory>

# Copy files from the host machine into the container image
COPY <source> <destination>

# Run a command at build time to prepare the image (e.g., install dependencies)
RUN <build-command>

# Document which port the application listens on inside the container
EXPOSE <port>

# Define the default command to run when the container starts
CMD ["executable", "arg1", "arg2"]
```
<br>

## Dockerfile format for a multistage build.
 ```
# Stage 1: Build
FROM <base-image> AS build
WORKDIR <working-directory>
COPY <source> <destination>
RUN <build-command>

# Stage 2: Production
FROM <base-image> # Same as stage 1.
WORKDIR <working-directory>
COPY --from=build <stage1-working-directory> <stage2-working-directory>
EXPOSE <port>
CMD ["executable", "arg1", "arg2"]
```
[View multistage demo](demo-screenshots/04.multistageImageBuild.md)
<br><br>

## More on Docker files:
- 'Dockerfile' is the default name for Docker files and is strongly recommended.

- In Dockerfiles, the following four commands are required to build an image:
  ```FROM```, ```COPY```, ```RUN```, ```CMD```

- Utilising other commands in Dockerfiles is key to building secure, efficient, and predictable container images.

- Not including ```WORKDIR``` means Docker uses the root directory (/) by default, which can lead to disorganized files and harder-to-maintain images.<br>

- COPY can be used to replace files in the container with a host's version by mapping the specific file to the container's file.

   ```COPY file.txt /app/file.txt```

- When installing system packages, use ```apt update && apt install -y package-name```.

- It is best practice to use ```EXPOSE```, although it has no effect, it serves as documentation for which ports the container listens on.
