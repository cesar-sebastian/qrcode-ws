# Active environment
`. activate`

# Run app
`export FLASK_APP=qr.py`

`python -m flask run`

# Freeze app

`pip freeze requirements.txt`

# Generate app

`pip install -r requirements.txt`

# Use app

GET 

http://127.0.0.1:5000/qr-generate-url?data=https://www.google.com

Return 

image/png



