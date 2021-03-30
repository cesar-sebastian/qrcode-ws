# Run app
`export FLASK_APP=qr.py`

`py -m flask run`

# Active environment
`. activate`

# Freeze app
`pip freeze requirements.txt`

# Generate app
`pip install -r requirements.txt`

# Use app
GET 

http://127.0.0.1:5000/qr-generate?data=https://www.google.com

Return 

image/png



