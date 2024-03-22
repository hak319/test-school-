@app.route("/sign-up", methods=['POST'])
def sign_up():
    newUser = request.json
    newUser["idNum"] = app.idNum
    app.users[app.idNum] = newUser
    app.idNum = app.idNum
    return jsonify(newUser)

if '__main__' == __name__ :
    app.run()