# 🔐 2FA Codes Generator

Welcome to the **2FA Codes Generator** repository! This project provides a simple and efficient way to generate and verify HOTP and TOTP codes using Python and Flask.

## ✨ Features

- 🔑 Generate random secrets for 2FA
- 🔢 Generate HOTP (HMAC-based One-Time Password) codes
- ⏰ Generate TOTP (Time-based One-Time Password) codes
- ✅ Verify HOTP and TOTP codes
- 🔗 Generate OTPAuth URLs for easy integration with authenticator apps

## 📦 Installation
1. ⭐ First give me a star

2. Clone the repository:
  ```bash
  git clone https://github.com/xe-4f14-5d3-6s2/2fa-codes-generator.git
  cd 2fa-codes-generator
  ```

3. Create a virtual environment and activate it:
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

4. Install the required dependencies:
  ```bash
  pip install -r requirements.txt
  ```

## 🚀 Usage

1. Run the Flask application:
  ```bash
  flask run
  ```

2. Use the following endpoints to generate and verify codes:

### 🔗 Endpoints

- **Generate Secret**
  ```http
  GET /generate/secret?length=<length>
  ```
  - `length`: Length of the secret (default: 32)

- **Generate TOTP**
  ```http
  GET /generate/totp?secret=<secret>&digits=<digits>&period=<period>
  ```
  - `secret`: The secret key
  - `digits`: Number of digits in the OTP (default: 6)
  - `period`: Time period in seconds (default: 30)

- **Generate HOTP**
  ```http
  GET /generate/hotp?secret=<secret>&counter=<counter>&digits=<digits>
  ```
  - `secret`: The secret key
  - `counter`: Counter value
  - `digits`: Number of digits in the OTP (default: 6)

- **Generate OTPAuth URL**
  ```http
  GET /generate/url?secret=<secret>&label=<label>&issuer=<issuer>&algorithm=<algorithm>&digits=<digits>&period=<period>&type=<type>
  ```
  - `secret`: The secret key
  - `label`: Label for the OTP
  - `issuer`: Issuer name (optional)
  - `algorithm`: Hash algorithm (default: SHA1)
  - `digits`: Number of digits in the OTP (default: 6)
  - `period`: Time period in seconds (default: 30)
  - `type`: Type of OTP (totp or hotp, default: totp)

- **Verify TOTP**
  ```http
  GET /verify/totp?secret=<secret>&token=<token>&digits=<digits>&period=<period>&window=<window>
  ```
  - `secret`: The secret key
  - `token`: The OTP token to verify
  - `digits`: Number of digits in the OTP (default: 6)
  - `period`: Time period in seconds (default: 30)
  - `window`: Verification window (default: 1)

- **Verify HOTP**
  ```http
  GET /verify/hotp?secret=<secret>&token=<token>&counter=<counter>&digits=<digits>&window=<window>
  ```
  - `secret`: The secret key
  - `token`: The OTP token to verify
  - `counter`: Counter value
  - `digits`: Number of digits in the OTP (default: 6)
  - `window`: Verification window (default: 1)

## 🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## 🙏 Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [Python](https://www.python.org/)

Thank you for using **2FA Codes Generator**! If you have any questions or feedback, feel free to reach out. 2FA Codes Generator