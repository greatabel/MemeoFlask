from dbhelper import DBHelper
from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from flask_restful import Api
from flask_restful import Resource, reqparse, abort
import json
import sys
import os
import site

# if is on ecs server 
if sys.platform == 'linux':
    # Add the site-packages of the chosen virtualenv to work with
    site.addsitedir('/var/www/env1/lib/python3.4/site-packages')
    # Activate your virtual env
    activate_env=os.path.expanduser("/var/www/env1/bin/activate_this.py")
    # execfile(activate_env, dict(__file__=activate_env))
    # exec(compile(open(activate_env, "r").read(), activate_env, 'exec'), dict(__file__=activate_env))
    with open(activate_env) as f:
        code = compile(f.read(), activate_env, 'exec')
        exec(code, dict(__file__=activate_env))

#----------------------


app = Flask(__name__)

DB = DBHelper()

api = Api(app)

Userids = {
    0,
    1,
    2
}

def abort_if_todo_doesnt_exist(userid):
    if userid not in Userids:
        abort(404, message="user's data {} doesn't exist".format(userid))

parser = reqparse.RequestParser()
parser.add_argument('rawdata')
parser.add_argument('whicheye')

class UserApi(Resource):
        def get(self, userid=None):
            print('userid=', userid)
            data = DB.get_rawmeasure(str(userid))
            print('abel::',data)
            res = []
            for m in data:
                d =  {
                    'orderid': m[0],
                    'rawdata': m[1],
                    'patientid': m[2],
                    'whicheye': str(m[3]),
                    'createdate': str(m[4])
                }
                res.append(d)
            myresult = json.dumps(res)
            print('abel##:',myresult)
            return myresult

        def post(self, userid):
           # Create a new product
            args = parser.parse_args()
            print('#',args)
            print(args['rawdata'],'@@',args['whicheye'],'#',args)
            DB.add_rawmeasure(args)
            abort_if_todo_doesnt_exist(userid)
            return 201

        def put(self, userid):
           # Update the product with given id
            return 'This is a PUT response'

        def delete(self, userid):
           # Delete the product with given id
            return 'This is a DELETE response'


api.add_resource(
    UserApi,
    '/api/user',
    '/api/user/<int:userid>/measures',

)


@app.route("/clear")
def clear():
    try:
        DB.clear_all()
    except Exception as e:
        print(e)
    return home()

# --------------website-----------------
@app.route("/login", methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")
    print('#',email,password)

    if  email  and  password:
        return redirect(url_for('measure'))
    return home()

@app.route("/logout")
def logout():
    # logout_user()
    print('logout')
    return redirect(url_for("home"))


@app.route("/measure")
def measure():
    return render_template("measure.html")

@app.route("/history")
def history():
    return render_template("history.html")


@app.route("/register", methods=["POST"])
def register():
    email = request.form.get("email")
    pw1 = request.form.get("password")
    pw2 = request.form.get("password2")
    if not pw1 == pw2:
        return redirect(url_for('home'))
    return redirect(url_for('home'))

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == '__main__':
    app.run(port=5000, debug=True)