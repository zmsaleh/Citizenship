from flask import Flask,redirect, request, render_template, make_response, send_from_directory

app = Flask(__name__)


@app.after_request
def apply_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response

@app.route('/')
def hello_world():
    return render_template('login.html')

@app.route('/register.html')
def register():
    return render_template('register.html')

@app.route('/login.html')
def login():
    return render_template('login.html')

@app.route('/style.css')
def css():
    return send_from_directory('static', 'style.css', mimetype='text/css')


@app.route('/image.jpg')
def image():
    return send_from_directory('static', 'image.jpg', mimetype='image/jpeg')

@app.route('/script.js')
def js():
    return send_from_directory('static', 'script.js', mimetype='application/javascript')

@app.route('/visit-counter')
def visit_counter():
    if request.cookies.get('Cookie',False)==False:
        response=make_response('1')
        response.set_cookie('Cookie','1',max_age=3600)
    else:
        value = request.cookies.get('Cookie')
        nextval=int(value)+1
        response = make_response(f'{nextval}')
        response.set_cookie('Cookie', f'{nextval}', max_age=3600)
    return response

@app.route('/cookie_show')
def cookie_show():
    values=request.cookies.get('Cookie')
    values=values
    return values

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)