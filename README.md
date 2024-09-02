# temperaturelogger
A very simple Python program to log temperature data to a SQL database.

The program stores the id of the temperature sensor (a string), the temperature (an integer) and a timestamp
into the database. 

It is often used as a backend for experiments with the DS18B20 digital temperature sensors running on an Arduino.
The Arduino (or any other client) simply issues a POST request with the temperature and the ID of the sensor to the
backend, which then stores the data plus a timestamp in the database. The database can then be queried from some other
program to generate reports etc.

## Usage
To build the program, edit temperaturelogger/settings.py:

* edit your host name in the ALLOWED_HOSTS property. Alternatively, make the property an empty list and set DEBUG = True .
* edit your database credentials in the DATABASES property.

After that, run:

```shell
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver [port]
```
To log a temperature value, send a POST request to the service with the variables "sensor" and "value".

Here is an example using curl:

```shell
curl -X POST http://127.0.0.1:8000/dbwrite/ -d "sensor=abc" -d "value=12345"
```

To access the data, run 

http://127.0.0.1:8000/db/

or
```sql
SELECT * from main_temperature
```

## To do
* There is no security whatsoever. Anyone can send a POST request to store data.
* if the database is large, access to http://127.0.0.1:8000/db/ will crash the server.