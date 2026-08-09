from flask import Flask

app = Flask(__name__)

@app.route('/')
def secrets():
    # ANYONE on the network can see this! No ID badge checked!
    return "Welcome! Here is the company's secret data: Password123!"

if __name__ == '__main__':
    app.run(port=5000)