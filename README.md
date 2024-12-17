# Setup

```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
export FLASK_APP=qr.py
python3 -m flask run
```

# Freeze one lib
```
pip freeze | grep requests >> requirements.txt
```

# Use app

## qr
```
GET  http://127.0.0.1:5000/qr-generate?data=https://www.google.com
```

## sss
```
POST http://127.0.0.1:5000/sss
{
    "user": "",
    "password": "",
    "cuit": ""
}
```