from flask import Flask
from flask import render_template
from deep_daze import Imagine
from flask import request
import os
import threading

def threaded_function(requested_text):
    parent_dir = os.environ.get('STATIC_URL')
    path = os.path.join(parent_dir,requested_text)
    os.mkdir(path)
    os.chdir(path)
    imagine = Imagine(
        text=requested_text,
        save_every=4,
        save_progress=True,
        epochs=1,
        open_folder=False,
    )
    imagine()

app = Flask(__name__, static_url_path='/static')

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/new_image", methods=['GET', 'POST'])
def requests():
    text = request.form.get('text')
    print(text)
    x = threading.Thread(target=threaded_function, args=(text,))
    x.start()
    return 'Done!'