from zipCode import getWeather, get_db_zips, get_key
from flask import Flask, jsonify, request 
  
app = Flask(__name__) 
  



  # Route for /weather 
@app.route('/weather', methods=['GET'])
def get_weather():
    if request.method == 'GET':
        args = request.args
        if len(args) > 2:
            return jsonify({"error": "Request malformed: too many query parameters"}), 400
        if 'key' in args and 'zip' in args:
            key = args['key']
            queryZip = args['zip']
            if get_key(key):
                data = getWeather(queryZip)
                return jsonify(data)
            else:
                return jsonify({"error": "Key not verified"}), 401
        else:
            return jsonify({"error": "You must enter a key and zip"}), 400

        #     dataBaseZips = []
        #     data = get_db_zips()
        #     for i in data:
        #         zip = i[0]
        #         temperature = getWeather(zip)
        #         dataBaseZips.append(f"{temperature}")
        # return jsonify(dataBaseZips)
        

  
@app.errorhandler(Exception)
def exception_handler(error):
    if KeyError:
        return "<h1 style='text-align: center'>Key Error</h1><p style='text-align: center; font-size: 12pt;'>" + repr(error) + "</p>"
    else:
        return "!!!!" + repr(error)

if __name__ == '__main__': 
    app.run(debug=True) 
