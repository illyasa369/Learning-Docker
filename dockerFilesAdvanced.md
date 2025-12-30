# This file contains more advanced concepts on Dockerfiles.
## More Dockerfile commands:

### Healthcheck
```
HEALTHCHECK CMD curl --fail http://localhost:port || exit 1
```

<br>

### Adding a group and user
```
RUN groupadd -r group-name && useradd -r -g group-name app-user-name
USER user-name
```

- Use of the -r option creates a system user.
- ```USER```changes the user.
- It is highly recommended that containers do not run as the root user.

<br>

### Entrypoint command
```
ENTRYPOINT ["<executable>", "<arg1>", "<arg2>"]
```

- Sets the main command for the container.
<br>

```
ENTRYPOINT ['python','app.py']
CMD ['--help']
 
# When the container starts, it runs: python app.py --help
```
- If used with CMD, CMD provides arguments for ENTRYPOINT.
<br>

```
ENTRYPOINT ['python','app.py']
CMD ['--help']

docker run image --version
# When the container starts, it runs: python app.py --version
```
- If ENTRYPOINT and CMD are used and an argument is passed when the image is ran, CMD is overridden.
<br>

### Environment variables
```
ENV variable-name=value
```
- Sets an environment variable for the container.
- Can be accessed by the container or program.
- It is encouraged to use environment variables instead of hardcoding values.
<br>

### Build-time variables
```
ARG variable-name=value
```
- Variable only available while building the image.
<br>

### Volumes
```
VOLUME ["/dir/in/container"]
```
- Creates a mount point for persistent or shared data in the container.
<br>

### Using a requirements.txt for Python dependencies

```
Flask
redis
numpy
requests
```
- When installing required dependencies in Python containers, it is best practice to list the dependencies in a requirements.txt file so builds are reproducible, maintainable, and efficient.

``` Dockerfile
RUN pip install --no-cache-dir -r requirements.txt
```
- --no-cache-dir option prevents packages from being cached, keeping the image smaller.
