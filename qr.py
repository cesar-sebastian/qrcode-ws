from flask import Flask
from flask import send_file
from flask import request
import pyqrcode


app = Flask(__name__)


@app.route('/qr-generate', methods=['GET'])
def qr():
    data = request.args.get('data')

    if data == '':
        raise Exception(f'Not found value to generate QR')

    filename = "qr.png"
    qr = pyqrcode.create(data)
    qr.png(filename, scale=6)

    return send_file(filename, mimetype='image/png')