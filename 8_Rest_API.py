from flask import Flask, request, jsonify
import sys
import json
import hgtk

app = Flask(__name__)

@app.route('/my_rest', methods=['GET', 'POST'])
def my_rest():
    sentence = ''
    if request.method == 'POST':
        json_data = request.get_json(force=True)
        sentence = json_data['sentence']
    else:
        sentence = request.args.get('sentence')
    if hgtk.josa.attach(sentence, hgtk.josa.I_GA) == sentence+'이':
        sentence += '이'
    sentence += '라고 말함~'
    return json.dumps({"input_sentence":sentence}, ensure_ascii=False)  
        
if __name__ == '__main__':
    port_num = 9090
    app.run(host = '0.0.0.0', port=port_num, threaded=False)
