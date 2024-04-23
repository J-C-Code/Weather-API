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
4. Now run your app!
   * Debug: Press `F5` or click the debug icon in your IDE
   * From terminal: Run `python main.py`
5. API can now be accessed from http://localhost:5000
