# Get Weather Information based on zip code anywhere in the US

## Local development
1. Create and activate Python virtual environment
   ```python
   python -m venv venv
   source venv/bin/activate # This works on Mac/Linux. Windows has another /bin/ file that is used to activate the Python virtual environment
   ```
2. Install requirements
   ```python
   pip install -r requirements.txt
   ```
3. Create secrets file (make sure you have an API key from https://api.openweathermap.org)
   ```shell
   export api_key=<your api key>
   echo 'apiKey = "$api_key"' > secretToken.py
   ```
4. Before running your app, you must create a postgres database!
   * In your secrets file, add a user and password into file after creating database. 
   * You will need one table for zip codes, and one for keys with the correct columns listed in zipCode.py
5. Now run your app!
   * Debug: Press `F5` or click the debug icon in your IDE
   * From terminal: Run `python main.py`
6. API can now be accessed from http://localhost:5000/
7. When using the API, you will notice it requires a zip code **AND** a key. To get a key, do http://localhost:5000/request which will generate a key.
8. Example of usage: http://localhost:5000/zip=74012&key="KEYHERE" 
# Integrating New Relic 
* When integrating New Relic, you must change the new relic license key to your own.