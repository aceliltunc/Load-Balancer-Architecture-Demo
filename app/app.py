from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
def hello():
    # Bu kod, hangi konteynerin cevap verdiğini gösterir.
    return f"Merhaba! Ben {socket.gethostname()} isimli sunucuyum."

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
