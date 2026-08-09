from flask import Flask, request, jsonify

app = Flask(__name__)

VALID_API_KEY = "Badge-12345-Admin" # Our secret ID badge

@app.route('/')
def secrets():
    # ZERO TRUST: Check for ID badge EVERY TIME
    provided_key = request.headers.get('X-API-Key')
    
    if provided_key == VALID_API_KEY:
        return "Welcome Admin! Here is the company's secret data: Password123!"
    else:
        # No badge? Get out!
        return jsonify({"error": "Unauthorized! Zero Trust means you must identify yourself."}), 401

if __name__ == '__main__':
    app.run(port=5000)