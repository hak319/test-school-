from flask import Flask, jsonify, request 

app = Flask(__name__)
app.user = {}
app.posts = []
app.idCnt = 1

@app.route('/')
def root():
    return "<h1>root directory</h1>"

if __name__ == '__main__':
    app.run()