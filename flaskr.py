from flask import Flask
from flask import request
from predict import getGoogleData
from predict import getFBMSG
from predict import pred
import json
import bloomberg
from flask import render_template
app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template('landing.html')

@app.route('/dashboard/', methods = ['GET'])
def sentiment():
    vars = request.args.items()
    googpred=pred(getGoogleData('ya29.eQCnabTuxqmxPBwAAAB2AZe6wAdMBSKEvMO7GjvKRuSQsfpiJz2KrnWFA_KnCg','my-user-agent/1.0'))
    print googpred
    fbpred=pred(getFBMSG('a10cf4775b52e5412537f495696b3a15'))
    print fbpred
    jso=json.dumps({"google":googpred,"facebook":fbpred})
    return render_template(jso)
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=80)
