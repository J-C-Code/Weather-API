from zipCode import getWeather
from zipCode import checkZips
from flask import Flask, jsonify, request 
  
app = Flask(__name__) 
  
  
@app.route('/hello', methods=['GET']) 
def helloworld(): 
    if(request.method == 'GET'): 
        args = request.args
        if len(args) > 0:
            queryZip = args['zip']
            data = getWeather(queryZip)
            return jsonify(data) 
        else:
            data = checkZips()
            return jsonify(data)
  
  
if __name__ == '__main__': 
    app.run(debug=True) 
