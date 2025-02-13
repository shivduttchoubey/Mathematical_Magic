from flask import Flask, send_file
import qrcode
from io import BytesIO
import time

app = Flask(__name__)

# Global variable to store the key
key = "key"

# Function to generate QR code
def generate_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save image to bytes buffer
    buffer = BytesIO()
    img.save(buffer, format='PNG')
    buffer.seek(0)
    return buffer

@app.route('/')
def home():
    return f'''
    <html>
        <head>
            <title>Dynamic QR Code</title>
            <script>
                function updateQR() {{
                    const img = document.getElementById('qr-code');
                    img.src = '/qr-code?' + new Date().getTime();
                }}
                
                // Refresh QR code every 5 seconds
                setInterval(updateQR, 5000);
            </script>
        </head>
        <body>
            <h1>Current Key: {key}</h1>
            <img id="qr-code" src="/qr-code" alt="QR Code">
            <p>QR code updates automatically every 5 seconds</p>
        </body>
    </html>
    '''

@app.route('/qr-code')
def serve_qr_code():
    # Generate QR code from current key
    buffer = generate_qr_code(key)
    return send_file(buffer, mimetype='image/png')

@app.route('/update/<new_key>')
def update_key(new_key):
    global key
    key = new_key
    return f"Key updated to: {key}"

if __name__ == '__main__':
    app.run(debug=True)