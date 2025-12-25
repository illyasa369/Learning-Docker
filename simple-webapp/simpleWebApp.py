from flask import Flask 


webApp = Flask(__name__) 

@webApp.route('/')
def hello():
    return 'Hello from a Docker container!\n'


if  __name__ == '__main__':
    webApp.run(host='0.0.0.0', port=5000)
