# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return "Hello from Flask in Docker!"

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ Hello! Flask is running inside Docker."

if __name__ == "__main__":
    # IMPORTANT: listen on 0.0.0.0 so Docker can expose it
    app.run(host="0.0.0.0", port=5000)

