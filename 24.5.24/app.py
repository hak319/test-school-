from flask import Flask, jsonify, request
app = Flask(__name__)
app.user = {}
app.posts = []
app.idCnt = 1

@app.route('/sign-up' , methods=['POST'])
def signUp():
    newUser = request.json
    newUser['id'] = app.idCnt
    app.upsers[app.idCnt] = newUser
    app.idCnt += 1
    return jsonify(newUser)

if __name__ == '__main__' :
    app.run()