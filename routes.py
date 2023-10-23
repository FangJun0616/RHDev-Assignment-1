from flask import Flask, Blueprint, jsonify, request

main = Blueprint('main', __name__)

@main.route('/', methods = ["GET"])
def show():
    try:
        if request.method == "GET":
            return "Hello Backend", 201
    except Exception as e:
        print(f"Error:{e}")
        return "Error", 404

@main.route('/about_me', methods = ['POST'])
def about_me():
    try:
        if request.method == "POST":
            details = {
                "Name": "Lim Fang Jun",
                "Course": "Math",
                "Year": "Year 1",
                "List all your CCA's": "Road Relays, RHDevs, SETS"
            }
            return jsonify(details), 201
    except Exception as e:
        print(f"Error:{e}")
        return "Can't see", 404
        