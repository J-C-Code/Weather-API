from zipCode import getWeather, get_db_zips, get_key, insert_key
from flask import Flask, jsonify, request 
import uuid
from flask_swagger_ui import get_swaggerui_blueprint
app = Flask(__name__) 
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Weather-API"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)


# Route to generate a unique key using uuid library
@app.route('/request', methods=['GET'])
def generate_key():
    new_key = str(uuid.uuid4())
    
    # Insert the key into the database
    insert_key(new_key)
    # Return the key to the user
    return jsonify({"key": new_key})
        

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
