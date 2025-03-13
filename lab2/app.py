from flask import Flask, render_template, request, json
from cipher.caesar import CaesarCipher

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/caesar")
def caesar():
    return render_template("caesar.html")

@app.route("/encrypt", methods=['POST'])
def encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['key'])
    caesar_cipher = CaesarCipher()
    encrypted_text = caesar_cipher.encrypt_text(text, key)
    return f"text: {text}<br/>key, key: {key}<br/>encrypted_text: {encrypted_text}"

@app.route("/decrypt", methods=['POST'])
def decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['key'])
    caesar_cipher = CaesarCipher()
    decrypted_text = caesar_cipher.decrypt_text(text, key)
    return f"text: {text}<br/>key, key: {key}<br/>decrypted_text: {decrypted_text}"

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 5050, debug = True)