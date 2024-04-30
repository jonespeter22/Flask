from flask import Flask, request
from PyQt5.QtWebEngineWidgets import QWebEngineView
app = Flask(__name__)

bus1_status = "Not Present"
bus2_status = "Not Present"

@app.route('/update', methods=['GET'])
def update_status():
    bus = request.args.get('bus')
    card_uid = request.args.get('cardUID')

    global bus1_status, bus2_status
    if bus == "bus1":
        bus1_status = "Present at Bus Stand: " + card_uid
    elif bus == "bus2":
        bus2_status = "Present at Bus Stand: " + card_uid

    return "Status Updated Successfully"

@app.route('/')
def display_status():
    return f"Bus1: {bus1_status}<br>Bus2: {bus2_status}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
