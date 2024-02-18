import flask
from flask import Flask
from flask import request

app = Flas(_name__, static_url_path='')

@app.route('/')
def root():
	return app.send_static_file('/public/index.html')
