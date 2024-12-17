from flask import Flask
from flask import send_file
from flask import request
import pyqrcode
from sss import scrap

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

@app.route('/sss', methods=['POST'])
def sss():
    data = request.get_json()

    user = data.get('user')
    password = data.get('password')
    cuit = data.get('cuit')

    if not user or not password or not cuit:
        return 'Faltan valores', 400

    try:
        dataScrap = scrap(user, password, cuit)
        return dataScrap
    except Exception as e:
        return f"Error: {str(e)}", 500

    