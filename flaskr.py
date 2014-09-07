from flask import Flask
from flask import request
from predict import getGoogleData
from predict import getFBMSG
from predict import pred
import bloomberg
import json
from flask import render_template
app = Flask(__name__)
app.config['DEBUG'] = True


def alterMonies(adjustment):
    


@app.route('/')
def index():
    return render_template('landing.html')

@app.route('/dashboard/', methods = ['GET'])
def sentiment():
    vars = request.args.items()
    googpred=pred(getGoogleData(vars[0]))
    print googpred
    fbpred=pred(getFBMSG(vars[1]))
    print fbpred
    
    vti = bloomberg.getPrice("VTI US EQUITY", "2014", "09", "05")
    bnd = bloomberg.getPrice("BND US EQUITY", "2014", "09", "05")
    
    googpred = 2 * (googpred - 0.5)
    fbpred = 2 * (fbpred - 0.5)
    
    turmoil = googpred + fbpred;
    
    jso=json.dumps({"turmoil":turmoil, "VTI":vti, "BND":bnd})
    return render_template('dashboard.html', vti=vti, bnd=bnd, turmoil=tirmoil)


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=80)
