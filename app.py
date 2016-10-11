from flask import Flask, jsonify,request
import json

import os



app = Flask(__name__)

def writing(file,d):
	try:
		json.dump(d, open(file,'w'))
	except Exception,e:
		print str(e)
	return

def reading(file):
    return  json.load(open(file))

@app.route('/')
def api_root():
    return 'Hollywood APP'


@app.route('/sale',methods=['GET'])
def allCinemas():
	listFile=os.listdir("/home/ubuntu/sale/")
	result=[]
	for l in listFile:
		result.append({"id":l})
	#print result
	return jsonify(sale=result)

@app.route('/sale/<articleid>',methods=['POST','DELETE'])
def tester(articleid):
    if request.method == 'POST':
	    if articleid in ["0003","0004","0005","0006","0007","0008","0009","0010"]:
	    	print "~/"+articleid
	    	writing("/home/ubuntu/sale/"+articleid,request.get_json())
	    	return "",201
	    else:
	    	return "id must be between 0003 and 0010",422
    if request.method == 'DELETE':
         if articleid in ["0003","0004","0005","0006","0007","0008","0009","0010"]:
             os.remove("/home/ubuntu/sale/"+articleid)
             return "",200


@app.route('/sale/<articleid>',methods=['GET'])
def getCinema(articleid):
	return jsonify(reading("/home/ubuntu/sale/"+articleid)),200

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)