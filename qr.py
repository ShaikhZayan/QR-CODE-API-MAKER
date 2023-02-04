from flask import Flask, request, Response
import qrcode
from io import BytesIO

Developer = "Shaikh Zayan Siddiqui"
Api_Example ="http://localhost:5000/qr?url=YOUR_URL"
print(" * Developer :",Developer) ,
print(" * Example :",Api_Example)

app = Flask(__name__)

@app.route('/qr', methods=['GET'])
def qr_code():
    url = request.args.get('url') , 
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color='black', back_color='white')
    buf = BytesIO()
    img.save(buf, 'PNG')
    buf.seek(0)
    response = Response(buf.read(), mimetype='image/png')
    response.headers.set('Content-Disposition', 'attachment', filename='qr.png')
    return response
    
    response.headers.set('Content-Disposition', 'attachment', filename=f'qr_{url}.png')
   

if __name__ == '__main__':
    app.run(debug=True)
    

# API MADE BY ZAYAN 
# Licenced by SHAIKH ZAYAN
# http://localhost:5000/qr?url=YOUR_URL