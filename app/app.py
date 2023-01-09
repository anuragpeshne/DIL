#!/usr/bin/env python3

from flask import Flask, request, abort, render_template
from os import listdir

app = Flask(__name__)

ROOT = "/data/"

@app.route("/")
def ui():
    files = listdir(ROOT)
    return render_template('ui.html', later_list=files)

@app.route("/<path:path>", methods=["GET", "POST"])
def record(path):
    payload = request.form or request.args
    if not payload or not payload['data']:
        return abort(400) # bad request

    data = payload['data'].strip() + '\n'
    with open(ROOT + path, "a") as taskfile:
        taskfile.write(data)

    return "Saved data in " + path



if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000)
