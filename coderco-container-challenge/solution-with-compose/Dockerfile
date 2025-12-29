FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

RUN apt update && apt install -y curl
HEALTHCHECK CMD curl --fail http://localhost:5000 || exit 1

RUN groupadd -r flask-group && useradd -r -g flask-group flask-app
USER flask-app

CMD ["python", "webapp.py"]
