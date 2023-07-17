from flask import Flask, session, request, render_template, redirect, url_for, flash
from itsdangerous import URLSafeTimedSerializer

app = Flask(__name__)
app.secret_key = 'my-super-duper-secret-key'


def decrypt_data(encrypted_data, secret_key):
    """ 
    Takes encrypted data and secret key as arguments
    returns the decrypted data
    """
    serializer = URLSafeTimedSerializer(secret_key)
    decrypt_data = serializer.loads(encrypted_data)
    return decrypt_data

# register the filter or add it to filters dict in other words
app.jinja_env.filters['decrypt'] = decrypt_data
# Serializer for encryption and decryption
serializer = URLSafeTimedSerializer(app.secret_key)

@app.route('/', methods=['POST', 'GET'])
def index():
    session.clear()
    if request.method =='POST':
        # Encrypt data and store in session
        data = request.form.get('data')
        
        
        if not data.strip():
            flash('At least enter One char!')
            return redirect(url_for('index'))
        
        encrypted_data = serializer.dumps(data)
        session['encrypted_data'] = encrypted_data

    return render_template('index.html', key=app.secret_key)


if __name__ == '__main__':
    app.run(debug=True)
