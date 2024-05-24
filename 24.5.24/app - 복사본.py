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

@app.route('/post', methods=['POST'])
def post() : 
    payload = request.json
    userID = int(payload['id'])
    msg = payload['msg']

    if userID not in app.user:
        return '사용자가 존재하지 않습니다' , 400
    if len(msg) > 300:
        return '300자를 초과 했습니다' , 400
    
    app.posts.append({
        'user_id' : userID,
        'post' : msg
    })
    return '성공' , 200