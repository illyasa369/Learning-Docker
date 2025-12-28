### This solution runs a Redis database and the Flask web app locally.
- Install Redis.
```
sudo apt install redis-server
```
<br>
- Start the Redis server and verify it is running.

```
sudo service redis-server start
redis-cli ping # Should return PONG
```

<br>
- Run the python app.

```
python3 webapp.py
```

<br>
<img width="1917" height="437" alt="Image" src="https://github.com/user-attachments/assets/5f26f140-0cba-4218-8b9e-f6b66b1549ef" />
