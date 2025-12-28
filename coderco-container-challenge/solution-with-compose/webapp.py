from flask import Flask
import redis
import os

rHost = os.environ.get("redis-host", "redisdb") # Gets the first string, second value acts as the default value if no rHost = os.environ.get("redis-host", "redisdb")  # Gets the value of "redis-host"; defaults to "redisdb" if not set
rPort = os.environ.get("redis-port", 6379)

app = Flask(__name__)
r = redis.Redis(host=rHost, port=rPort , decode_responses=True)

r.set("sessionCount", 0)

@app.route("/")
def welcome():
	return '''
<h1>Welcome to my web counter page</h1>
<a href="/count">Go to counter</a>
'''

@app.route("/count")
def showCount():
	r.incr("sessionCount")
	r.incr("alltimeCount")
	return f"""
Session visit count:{r.get("sessionCount")}
<br>
All time visit count:{r.get("alltimeCount")}
<br>
<a href="/">Return</a>
"""

if __name__=="__main__":
	app.run(host="0.0.0.0", port=5000)
