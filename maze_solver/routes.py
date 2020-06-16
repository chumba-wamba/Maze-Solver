from flask import jsonify
from maze_solver import app
from algo.bfs import BreadthFirstSearch
from algo.dfs import DepthFirstSearch
from algo.a_star import AStar


@app.route("/")
def index():
    return "Hello, world!"
