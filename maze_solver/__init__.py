from flask import Flask
app = Flask(__name__)

from maze_solver import routes
