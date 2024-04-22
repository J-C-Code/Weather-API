from zipCode import getWeather
from flask import Flask, jsonify, request 
  
app = Flask(__name__) 
  
  
@app.route('/hello', methods=['GET']) 
def helloworld(): 
    if(request.method == 'GET'): 
        args = request.args
        queryZip = args['zip']
        data = getWeather(queryZip)
        return jsonify(data) 
  
  
if __name__ == '__main__': 
    app.run(debug=True) 
