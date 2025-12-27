from flask import Flask
import redis

app = Flask(__name__)
r = redis.Redis(host="localhost", port=6379, decode_responses=True)

r.set("sessionCount", 1)

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
