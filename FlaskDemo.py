from flask import Flask, request
import socket

app = Flask(__name__)

@app.route('/')
def hello_world():
    # Get the IP address of the server
    server_ip = socket.gethostbyname(socket.gethostname())
    return f"Hello, World! Your server IP is: {server_ip}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)  # Run the app on all network interfaces and port 80 (HTTP)

