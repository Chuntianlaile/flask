from flask import Flask, render_template, abort
import os, json

app = Flask(__name__)

file_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'files'))
file_list = os.listdir(file_dir)
files = []
for file_name in file_list:
    with open(os.path.join(file_dir, file_name)) as f:
        files.append(json.load(f))

@app.route('/')
def index():
    return render_template('index.html', files=files)

@app.route('/files/<filename>')
def file(filename):
    if os.path.exists(os.path.join(file_dir, '{}.json'.format(filename))):
        with open(os.path.join(file_dir, '{}.json'.format(filename))) as f:
            _file = json.load(f)
        return render_template('file.html', file=_file)
    abort(404)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404
if __name__ == '__main__':
    print(files)
