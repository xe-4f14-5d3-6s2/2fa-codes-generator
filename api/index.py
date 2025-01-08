from flask import Flask, request, jsonify
from lib.otp import *

app = Flask(__name__)

@app.route('/generate/secret')
def generate_secret():
    try:
        length = int(request.args.get('length', 32))
        if length <= 0:
            raise ValueError("Length must be a positive integer")
        return jsonify(secret(length))
    except ValueError as e:
        return jsonify({"error": 400, "reason": str(e)}), 400

@app.route('/generate/totp')
def generate_totp():
    secret = request.args.get('secret')
    if not secret:
        return jsonify({"error": 400, "reason": "Please provide a secret"}), 400
    try:
        digits = int(request.args.get('digits', 6))
        period = int(request.args.get('period', 30))
        if digits <= 0 or period <= 0:
            raise ValueError("Digits and period must be positive integers")
        return jsonify(totp(secret, digits, period))
    except ValueError as e:
        return jsonify({"error": 400, "reason": str(e)}), 400

@app.route('/generate/hotp')
def generate_hotp():
    secret = request.args.get('secret')
    counter = request.args.get('counter')
    if not secret or not counter:
        return jsonify({"error": 400, "reason": "Please provide a secret and a counter"}), 400
    try:
        counter = int(counter)
        digits = int(request.args.get('digits', 6))
        if counter < 0 or digits <= 0:
            raise ValueError("Counter must be non-negative and digits must be positive")
        return jsonify(hotp(secret, counter, digits))
    except ValueError as e:
        return jsonify({"error": 400, "reason": str(e)}), 400

@app.route('/generate/url')
def generate_url():
    secret = request.args.get('secret')
    label = request.args.get('label')
    if not secret or not label:
        return jsonify({"error": 400, "reason": "Please provide a secret and a label"}), 400
    try:
        issuer = request.args.get('issuer')
        algorithm = request.args.get('algorithm', 'SHA1')
        digits = int(request.args.get('digits', 6))
        period = int(request.args.get('period', 30))
        type = request.args.get('type', 'totp')
        if digits <= 0 or period <= 0:
            raise ValueError("Digits and period must be positive integers")
        return jsonify(url(secret, label, issuer, algorithm, digits, period, type))
    except ValueError as e:
        return jsonify({"error": 400, "reason": str(e)}), 400

@app.route('/verify/totp')
def validate_totp():
    secret = request.args.get("secret")
    token = request.args.get("token")
    if not secret or not token:
        return jsonify({"error": 400, "reason": "Please provide a secret and a token"}), 400
    try:
        digits = int(request.args.get('digits', 6))
        period = int(request.args.get('period', 30))
        window = int(request.args.get('window', 1))
        if digits <= 0 or period <= 0 or window < 0:
            raise ValueError("Digits and period must be positive and window must be non-negative")
        return jsonify(verify_totp(secret, token, digits, period, window))
    except ValueError as e:
        return jsonify({"error": 400, "reason": str(e)}), 400

@app.route('/verify/hotp')
def validate_hotp():
    secret = request.args.get("secret")
    token = request.args.get("token")
    counter = request.args.get("counter")
    if not secret or not token or not counter:
        return jsonify({"error": 400, "reason": "Please provide a secret, token and a counter"}), 400
    try:
        counter = int(counter)
        digits = int(request.args.get('digits', 6))
        window = int(request.args.get('window', 1))
        if counter < 0 or digits <= 0 or window < 0:
            raise ValueError("Counter must be non-negative, digits must be positive and window must be non-negative")
        return jsonify(verify_hotp(secret, token, counter, digits, window))
    except ValueError as e:
        return jsonify({"error": 400, "reason": str(e)}), 400