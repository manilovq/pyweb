from flask import Flask

app = Flask(__name__)

from app.handler import index

