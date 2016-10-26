from dbhelper import DBHelper
from flask import Flask
from flask import redirect
from flask import render_template
from flask import make_response
from flask import request
from flask import url_for
from flask import jsonify
from flask_restful import Api
from flask_restful import Resource, reqparse, abort
from flask_cors import CORS, cross_origin

import json
import sys
import os
import site
import datetime
import logging
from base64 import b64encode




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

fh = logging.FileHandler('/tmp/mylogfile')
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
app.logger.setLevel(logging.INFO)
app.logger.addHandler(fh)


# CORS(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

DB = DBHelper()

api = Api(app)


Userids = {
    1,
    
}

Patientids = {
    1,
    2,
    3
}


def abort_if_todo_doesnt_exist(userid):
    if userid not in Userids:
        abort(404, message="user's data {} doesn't exist".format(userid))

def abort_if_patient_doesnt_exist(patientid):
    if patientid not in Patientids:
        abort(404, message="patients's data {} doesn't exist".format(patientid))

parser = reqparse.RequestParser()
parser.add_argument('rawdata')
parser.add_argument('whicheye')
parser.add_argument('patientid')

parser_baseline = reqparse.RequestParser()
parser_baseline.add_argument('data')
parser_baseline.add_argument('patientid')


class ChildMeasure(Resource):
        def get(self, patientid):
            app.logger.info('patientid=', patientid)
            args = parser.parse_args()
            app.logger.info('#'*10,args)

            data = DB.get_rawmeasure(str(patientid))
            app.logger.info(('abel::',data))
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
            myresult = jsonify(res)            
            app.logger.info('abel##:',myresult)
            return myresult

        def post(self, patientid):
           # Create a new product
            args = parser.parse_args()
            app.logger.info('#',args)
            app.logger.info(args['patientid'],'@@',args['rawdata'],'@@',args['whicheye'],'#',args)
            DB.add_rawmeasure(args)
            abort_if_patient_doesnt_exist(patientid)
            return 201

        # def put(self, userid):
        #    # Update the product with given id
        #     return 'This is a PUT response'

        # def delete(self, userid):
        #    # Delete the product with given id
        #     return 'This is a DELETE response'

class UserChildApi(Resource):
        def get(self, userid):
            app.logger.info(('userid=', userid))
            args = parser.parse_args()
            app.logger.info('#'*5,args)

            data = DB.get_children(str(userid))
            # app.logger.info(('abel child::',type(data[0][4])))
            res = []
            for m in data:
                d =  {
                    'patientid': m[0],
                    'name': m[1],
                    'sex': m[2],
                    'birthday': str(m[3]),
                    
                    'createdate': str(m[5])
                }
                res.append(d)

            myresult = jsonify(res)            
            # app.logger.info('abel child##:',myresult)
            return myresult

        def post(self, userid):

            return 'post child data'

class ChildPicture(Resource):
        def get(self, patientid):
            data = DB.get_childrenPicture(str(patientid))
            print('# in picture:',data)

            ENCODING = 'utf-8'
            base64_bytes = b64encode(data[0][0])
            base64_string = base64_bytes.decode(ENCODING)
            raw_data = {'IMAGE_DATA': base64_string}
            return raw_data  


class ChildBaseline(Resource):
        def get(self, patientid):
            # app.logger.info('ChildBaseline:#patientid=',patientid)
            data = DB.get_measurebaseline(str(patientid))
            app.logger.info('ChildBaseline::',data)
            print('#data:',data)
            left = -1
            right = -1
            for m in data:
                if m[0] == 0:
                    left = m[1]
                if m[0] == 1:
                    right = m[1] 
            raw_data = {'left': left, 'right':right}         
            app.logger.info('abel##:',raw_data)
            return raw_data


        def post(self, patientid):
            args = parser_baseline.parse_args()
            if not args['patientid']:
                args['patientid'] = patientid
            app.logger.info('ChildBaseline #args:',args)
            DB.add_measurebaseline(args)
            abort_if_patient_doesnt_exist(patientid)
            return 201

class UserAPI(Resource):
        def get(self, userid):
            data = DB.get_user(str(userid))
            print('# in UserAPI:',data)
            abort_if_todo_doesnt_exist(userid)
            raw_data = {'putao_name': data[0][0]}
            
            return raw_data  

api.add_resource(UserAPI,'/api/user/<int:userid>')
api.add_resource(UserChildApi,'/api/userchild/<int:userid>')
api.add_resource(ChildMeasure,'/api/childmeasure/<int:patientid>')
api.add_resource(ChildBaseline,'/api/childbaseline/<int:patientid>')
api.add_resource(ChildPicture,'/api/childpicture/<int:patientid>')


@app.route("/clear")
def clear():
    try:
        DB.clear_all()
    except Exception as e:
        app.logger.info(e)
    return home()

# --------------website-----------------

DEFAULTS = {'email': 'abel',
            'password': 'test1024',
            'receive_putao_user':''
            }

def get_value_with_fallback(key):
    if request.args.get(key):
        return request.args.get(key)
    if request.cookies.get(key):
        return request.cookies.get(key)
    return DEFAULTS[key]

@app.route("/login", methods=["POST"])
def login():
    email = get_value_with_fallback("email")
    password = get_value_with_fallback("password")
    if  email  and  password:
        return redirect(url_for('childrenlist'))
    return home()

@app.route("/logout")
def logout():
    # logout_user()
    app.logger.info('logout')
    return redirect(url_for("home"))


@app.route("/measure")
def measure():
    return render_template("measure.html")

@app.route("/childrenlist")
def childrenlist():

    return render_template("childrenlist.html")

@app.route("/history")
def history():
    return render_template("history.html")
    
@app.route("/appdownload")
def appdownload():
    return render_template("appdownload.html")


@app.route("/register", methods=["POST"])
def register():
    email = request.form.get("email")
    pw1 = request.form.get("password")
    pw2 = request.form.get("password2")
    if not pw1 == pw2:
        return redirect(url_for('home'))
    return redirect(url_for('home'))

 
@app.route("/receive_putao_user", methods=["GET","POST"])
def receive_putao_user():
    if request.method == "POST":
        # from flask import jsonify
        app.logger.info("receive_putao_user/ I am printing: " ,request.values)
        DEFAULTS['receive_putao_user'] = str(request.values)
        status_dict  = {'http_code': 200,
            'msg': 'ok',
            'data':[]
            }
        return jsonify(status_dict), 200
    if request.method == "GET":
        app.logger.info('#in get:',request.values )
        return str(request.values )+' #show:'+  DEFAULTS['receive_putao_user']




@app.route("/")
def home():
    email = get_value_with_fallback("email")
    password = get_value_with_fallback("password")
    if  email  and  password:
        return redirect(url_for('childrenlist'))
    expires = datetime.datetime.now() + datetime.timedelta(days=365)
    response.set_cookie("email", email, expires=expires)
    response.set_cookie("password", password, expires=expires)
    # save cookies and return template
    response = make_response(render_template("home.html", email=email,
                                             password=password))
    return response

if __name__ == '__main__':
    # create logger with 'spam_application'
    print('app.debug=',app.debug)
    # logger = logging.getLogger('luminagic')

    # fh = logging.FileHandler('/tmp/mylogfile')
    # fh.setLevel(logging.DEBUG)
    # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # fh.setFormatter(formatter)
    # app.logger.setLevel(logging.WARNING)
    # app.logger.addHandler(fh)
    # app.logger.info('hello world')

    # create file handler which logs even debug messages

    # create formatter and add it to the handlers

    # add the handlers to the logger



    app.run(port=5000, debug=True)


