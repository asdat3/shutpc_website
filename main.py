from flask import Flask, request
import os,socket
app = Flask(__name__)

print([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0])


@app.route('/')
def index():
    return('<center><a href="/shutdown">shutdown</a></center>')

@app.route('/shutdown', methods=['POST','GET'])
def shutdown_clicked():
    os.system("shutdown /s /t 1")
    return 'Button clicked!'

if __name__ == '__main__':
    app.run(host="192.168.178.128",port=508899)