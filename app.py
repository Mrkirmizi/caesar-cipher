from flask import Flask, render_template, request
from encryption import encrypt
from deciphered import decrypt

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    encrypted_result = ""
    decrypted_result = ""
    
    if request.method == "POST":
        text = request.form["text"]
        shift = int(request.form["shift"])
        action = request.form["action"]
        
        if action == "encrypt":
            encrypted_result = encrypt(text, shift)
        elif action == "decrypt":
            decrypted_result = decrypt(text, shift)
        
    return render_template("index.html", encrypted_result=encrypted_result, decrypted_result=decrypted_result)

if __name__ == "__main__":
    app.run(debug=True)
