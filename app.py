from flask import Flask, request, render_template, jsonify
from flask_jwt_extended import *
from DB_dao import *
from dto import *
from Elk_python import *
# from memo import memo

app = Flask(__name__)

app.config.update(
    DEBUG=True,
    JWT_SECRET_KEY="I'M IML"
)

jwt=JWTManager(app)



@app.route('/', methods=["GET", "POST"])
def index():
    if request.method=="GET":
        return render_template('index.html')
    elif request.method == "POST":
        data = book(request.form.get("id"))
        data = jsonify(data)
        print(type(data))
        return data

@app.route('/info2', methods=['POST'])
def about2():
    data1 = info()
    return jsonify(data1)


@app.route('/info', methods=['GET', 'POST'])
def about():
    if request.method == "GET":
        return render_template('info.html')

    elif request.method == "POST":
        return '{"img01" : "http://localhost:5601/goto/9bc00ce7159558ceb9864d06d845b86f"}'

@app.route('/info1', methods=['GET', 'POST'])
def about1():

    if request.method == "POST":
        return '{"img02" : "http://localhost:5601/goto/e660241fa417e58a78414d910c158ac0"}'



@app.route('/join', methods=['GET','POST'])
def join1():
    if request.method =="GET":

        return render_template('join.html')
    else:
        dao = InfoDAO()
        dto = userjoindto(request.form.get("userid"), request.form.get("userpw"), request.form.get("username"))
        dao.insertjoin(dto)
        return render_template('join.html')


@app.route('/login', methods=['GET'])
def move():
    return render_template('login.html')



@app.route('/login', methods=['POST'])
def login1():
    id = request.form.get("userid")
    pw = request.form.get("userpw")
    dao= InfoDAO()

    if id == dao.login(request.form.get("userid")) & pw == dao.login(request.form.get('userpw')):
        return jsonify(
            result="200",
            access_token=create_access_token(identity=id)
        )
    





@app.route('/map', methods=['GET'])
def map():
    return render_template('map.html')

@app.route('/memo', methods=['POST'])
def parse():
    return memo()



if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port='5000')