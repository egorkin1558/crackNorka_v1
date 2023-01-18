import requests
from flask import Flask, jsonify,request
app = Flask(__name__)
@app.route('/md5.php', methods=['POST','GET'])
def crack():
    return "//match/"

@app.errorhandler(404)
def not_found(error):
    return '{"ok":true,"code":200,"message":"Sussec","forever":false,"timestamp":1676610130,"datetime":"2023-02-18T21:50:30.000000Z"}'

context = ('serf.crt', 'key.key')#cs
app.run(debug=True,host="0.0.0.0",port=443,ssl_context=context)
