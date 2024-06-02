import requests
import sys
from secretToken import apiKey, dbUser, dbPassword
import json
import psycopg2


# Function to connect to the PostgreSQL database
def connect_to_db():
    conn = psycopg2.connect(
        dbname="Zips", user=dbUser, password=dbPassword, host="localhost"
    )
    return conn


# Function to insert zip code into the database
def add_zip_to_db(zip_code, city):
    conn = connect_to_db()
    cur = conn.cursor()
    postgreSQL_select_Query = "SELECT * FROM public.zip_codes"
    cur.execute(postgreSQL_select_Query)
    records = cur.fetchall()
    try:
        cur.execute(
            'INSERT INTO zip_codes ("ZipCode", "City Name") VALUES (%s, %s)',
            (zip_code, city),
        )
        conn.commit()
        conn.close()
    except psycopg2.errors.UniqueViolation:
        print()


def get_db_zips():
    conn = connect_to_db()
    cur = conn.cursor()
    postgreSQL_select_Query = "SELECT * FROM public.zip_codes"
    cur.execute(postgreSQL_select_Query)
    records = cur.fetchall()
    conn.commit()
    conn.close()
    return records

def get_key(key):
    conn = None
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        select_query = "SELECT 1 FROM public.keys WHERE key = %s"
        cur.execute(select_query, (key,))
        result = cur.fetchone()
        cur.close()
        return result is not None
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    finally:
        if conn:
            conn.close()

def insert_key(key):
    conn = None
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        insert_query = "INSERT INTO public.keys (key) VALUES (%s)"
        cur.execute(insert_query, (key,))
        conn.commit()
        cur.close()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()

            
def main():
    if len(sys.argv) < 2:
        print("Not enough arguments")
    elif len(sys.argv) > 2:
        print("Too many arguments")
    elif not sys.argv[-1].isdigit():
        print("User did not enter zip code properly")
    else:
        data = getWeather(sys.argv[-1])
        city = data["city"]
        temperature = data["temperature"]
        print(f"It is currently {temperature} degrees in {city}")


def getWeather(zipCode):
    # Here we'll use requests.get to get info using format below
    weatherData = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?zip={zipCode},us&appid={apiKey}&units=imperial"
    ).json()
    # Gets temperature, rounds to nearest whole number.
    temperature = round(float(weatherData["main"]["temp"]))
    # Gets city name from API.
    city = weatherData["name"]
    # Creates object, which we then return from called function.
    returnInfo = {"city": city, "temperature": temperature}
    add_zip_to_db(zipCode, city)
    return returnInfo





if __name__ == "__main__":
    main()
