##### Note: 'Dockerfile' is the default name for Docker files and is strongly recommended.<br><br>

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
