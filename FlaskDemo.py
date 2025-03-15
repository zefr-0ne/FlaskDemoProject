from flask import Flask
import requests
import socket

app = Flask(__name__)

def get_instance_metadata(path):
    """Fetch metadata from AWS metadata service"""
    try:
        response = requests.get(f"http://169.254.169.254/latest/meta-data/{path}", timeout=2)
        return response.text
    except requests.exceptions.RequestException:
        return "Unavailable"

@app.route('/')
def hello():
    # Get Public IP from AWS metadata
    public_ip = get_instance_metadata("public-ipv4")

    # Get Private IP
    private_ip = socket.gethostbyname(socket.gethostname())

    return f"Hello, World! Public IP: {public_ip}, Private IP: {private_ip}"

@app.route('/info')
def instance_info():
    """Returns AWS EC2 instance metadata"""
    instance_id = get_instance_metadata("instance-id")
    public_ip = get_instance_metadata("public-ipv4")
    private_ip = socket.gethostbyname(socket.gethostname())
    az = get_instance_metadata("placement/availability-zone")

    return {
        "Instance ID": instance_id,
        "Public IP": public_ip,
        "Private IP": private_ip,
        "Availability Zone": az
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
