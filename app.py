from flask import Flask, render_template, request, jsonify, send_file

app = Flask(__name__)

FLAG = "CSEC{steganography_master}"
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download')
def download():
    return send_file('file.txt', as_attachment=True)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    user_flag = data.get('flag', '').strip()
    
    if user_flag == FLAG:
        return jsonify({'correct': True, 'message': 'CORRECT! Flag accepted.'})
    else:
        return jsonify({'correct': False, 'message': ' WRONG. Keep investigating.'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)