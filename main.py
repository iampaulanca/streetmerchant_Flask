from flask import Flask, request, jsonify
import os
import subprocess

app = Flask(__name__)

streetmerchant_dir = "/Users/paulancajima/Desktop/streetmerchant"
# ps aux | grep {streetmerchant_dir}


@app.route('/', methods=['GET'])
def hello_world():
    return "hello world"


@app.route('/getConfig', methods=['GET'])
def get_config():
    # read lines from dotenv file
    filepath = os.path.join(f'{streetmerchant_dir}', 'dotenv')
    if not os.path.exists(f'{streetmerchant_dir}'):
        os.makedirs(f'{streetmerchant_dir}')
    f = open(filepath, "r")
    lines = f.readlines()

    # get current configurations from dotenv
    current_config = {}
    for index, line in enumerate(lines):
        _line = line.split("=")
        current_config[_line[0]] = _line[1].replace("\n", "")

    return jsonify(current_config)


@app.route('/updateConfig', methods=['POST'])
def update_config():
    if request.method == 'POST':
        data = request.json
    else:
        return jsonify({"error": "something bad happened"})

    # read lines from dotenv file
    filepath = os.path.join(f'{streetmerchant_dir}', 'dotenv')
    if not os.path.exists(f'{streetmerchant_dir}'):
        os.makedirs(f'{streetmerchant_dir}')
    f = open(filepath, "r")
    lines = f.readlines()

    # iterate and update lines from received json data
    for index, line in enumerate(lines):
        key_value = line.split('=')
        if key_value[0] in data:
            lines[index] = f'{key_value[0]}={data[key_value[0]]}\n'

    f = open(filepath, "w")
    f.writelines(lines)
    f.close()

    # kill existing streetmerchant script
    os.system(f"kill -9 $(pgrep -f '{streetmerchant_dir}')")

    # start new script
    subprocess.Popen(["npm", "start"], cwd=f"{streetmerchant_dir}", stdout=subprocess.DEVNULL)

    return jsonify(data)


@app.route('/killScript', methods=['GET'])
def kill_script():
    # kill streetmerchant script
    os.system(f"kill -9 $(pgrep -f '{streetmerchant_dir}')")
    return "Street merchant has been murdered"


if __name__ == '__main__':
    app.run()
