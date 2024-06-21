@app.route('/main', methods=['GET'])

@app.route('/sing-up', methods = ['GET'])

def singUpPage() :
    return render_template('signup.html')

@app.route('/sign-up', methods=['post'])