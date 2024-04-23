from zipCode import getWeather
from zipCode import get_db_zips
from flask import Flask, jsonify, request 
  
app = Flask(__name__) 
  
  
@app.route('/weather', methods=['GET']) 
def helloworld(): 
    if(request.method == 'GET'): 
        args = request.args
        print(len(args))
        if len(args) > 1:
            return "Request malformed: too many query parameters", 400
        if len(args) > 0:
            queryZip = args['zip']
            data = getWeather(queryZip)
            return jsonify(data) 
        else:
            data = get_db_zips()
            return jsonify(data)
  
@app.errorhandler(Exception)
def exception_handler(error):
    return "!!!!" + repr(error)

if __name__ == '__main__': 
    app.run(debug=True) 
