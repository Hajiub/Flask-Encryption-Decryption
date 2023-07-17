<h1 align="center">Flask Encryption/Decryption Project</h1>



<p align="center">
This Flask Encryption/Decryption project demonstrates a simple web application built with Flask that allows you to encrypt and decrypt data using a secret key.

</p>

## Features

- Encrypt data and store it in session
- Decrypt session data and display the original data
- Built with Flask framework
- Uses itsdangerous library for encryption/decryption

## Getting Started

### Prerequisites

- Python 3.x
- Flask

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Hajiub/Flask-Encryption-Decryption.git
```
2. Navigate to the project directory:
```bash
cd Flask-Encryption-Decryption
```
3. Install the dependencies:
```bash
pip install -r requirements.txt
```
## Usage

1. Set your Flask secret key in the `app.py` file:
```python
app.secret_key = 'your_secret_key'
```
Run the Flask application:
```bash
python app.py
```

Access the application in your web browser at http://localhost:5000.
## License

This project is licensed under the MIT License.
Feel free to customize the content, or to add more details.