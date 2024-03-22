from flask import Flask, request, jsonify

app = Flask(__name__)
app.idNum = 1
app.users = {}

@app.route("/sign-up", methods=['POST'])
def sign_up():
    newUser = request.json
    newUser["idNum"] = app.idNum
    app.users[app.idNum] = newUser
    app.idNum = app.idNum
    return jsonify(newUser)

@app.route("/check-users", methods=['GET'])
def check_users():
    return app.users

if '__main__' == __name__ :
    app.run()