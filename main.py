from zipCode import getWeather
from zipCode import get_db_zips
from flask import Flask, jsonify, request 
  
app = Flask(__name__) 
  
  # Route for /weather 
@app.route('/weather', methods=['GET']) 
def helloworld(): 
    if(request.method == 'GET'): 
        args = request.args
        if len(args) > 1:
            return "Request malformed: too many query parameters", 400
        if len(args) > 0:
            queryZip = args['zip']
            data = getWeather(queryZip)
            return jsonify(data) 
        else:
            dataBaseZips = []
            data = get_db_zips()
            for i in data:
                zip = i[0]
                temperature = getWeather(zip)
                dataBaseZips.append(f"{temperature}")
        return jsonify(dataBaseZips)
        

  
@app.errorhandler(Exception)
def exception_handler(error):
    if KeyError:
        return "<h1 style='text-align: center'>Key Error</h1><p style='text-align: center; font-size: 12pt;'>" + repr(error) + "</p>"
    else:
        return "!!!!" + repr(error)

if __name__ == '__main__': 
    app.run(debug=True) 
