from flask import Flask, render_template, request
from Cipher import encrypt_message, decrypt_message


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/encrypt")
def encryption_page():
    return render_template("encrypt.html")


@app.route("/decrypt")
def decryption():
    return render_template("decrypt.html")


@app.route("/secure_text", methods=["GET", "POST"])
def secure():
    message = request.form.get("message")
    password = request.form.get("password")
    print("Your message is :", message)
    print("Your password is :", password)
    enc_msg = encrypt_message(message, password)
    print("Your encrypted message is :", enc_msg)
    return render_template("message.html", code=enc_msg)


@app.route("/decode_mssg", methods=["POST", "GET"])
def decrypt():
    message = request.form.get("mssg")
    password = request.form.get("passwd")
    print(request.form)
    print(message, password)
    try:
        plain_text = decrypt_message(message, password)
    except:
        plain_text = "Error"
    return render_template("message.html", code=plain_text)


if __name__ == "__main__":
    app.run()


# gAAAAABiC7iQFOD9VGuX1iv0Ftnrm9-tDbhOkUI7nbq2F0M9w5UUTtsl-OZmq0tG9TMP1VQzU30q_oN0gUGEfJRnNIKxyU-mSQ==
