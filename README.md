# Api Geo Partner
Autor: Gabriel Castorino 

Linkedin: https://www.linkedin.com/in/gabriel-castorino/

## Object
Objective to develop that provides API using REST, with the following endpoints:

  - Create partner

      - All fields are required and must follow the rules set above.

      - POST - http://localhost:5000/partner/

  - Get partner by id

      - Get a specific partner by its `id`.

      - GET - http://localhost:5000/partner/{id}

  - Search partner

      - Given a specific location (coordinates `lng` and `lat`), search the nearest partner considering each partner's coverage area.

      - GET - http://localhost:5000/search-partner/{lnt}/{lat}

## Technologies chosen

The programming language **Python** and the database **Mongo**

## Requered

```
Install Python version 3.6
Service MongoDB 
```

### To Setup and Start

```
pip install -r requirements.txt 
# Create file .env and set parameters information in ENV 
set -a; source .env; set +a   
python app.py
```

## To Setup by docker

```sh
docker-compose -f "apiGeoPartner/docker-compose.yml" up -d --build
```

## create index database

```sh
db.partner.createIndex("coverageArea","2dsphere");
```

## ENV

```sh
PORT="80"
DBAAS_MONGODB_DATABASE={name_database}
DBAAS_MONGODB_ENDPOINT="mongodb://{host_database}:27017/{name_database}"
FIELD_ID="id"
FIELD_ADDRESS="address"
FIELD_COVERAGE_AREA="coverageArea"
FIELD_DOCUMENT="document"
FIELD_OWNER_NAME="ownerName"
FIELD_TRADING_NAME="tradingName"
ERROR_TEXT_GEO="Cant extract geo keys"
ERROR_TEXT_NOT_FOUND="Not found"
ERROR_TEXT_REQUIRED="Required field"
ERROR_TEXT_STRING="Type requered string"
ERROR_TEXT_NUMBER="Type requered number"
ERROR_TEXT_OBJECT="Type requered object valid"
ERROR_TEXT_LIST="Type requered list valid"
ERROR_TEXT_DOCUMENT="Document invalid"
ERROR_TEXT_MIN_LENGTH="Min length"
ERROR_TEXT_LENGTH="Length"
ERROR_TEXT_INCORRECT="incorrect"
```

### Unit Test with Nose

Command:
```sh
nosetests --verbosity=2
```

## Tests Output

Command:
```sh
nosetests --verbose --nocapture
```

Result:
```
Test util check is found ... ok
Test util check is not found ... ok
Test util check is requered ... ok
Test util check is not requered ... ok
Test util check is string ... ok
Test util check is not string ... ok
Test util check is int ... ok
Test util check is not int ... ok
Test util check is disc ... ok
Test util check is not disc ... ok
Test util check is list ... ok
Test util check is not list ... ok
Test util check is min length ... ok
Test util check is not min length ... ok
Test util check is length ... ok
Test util check is not length ... ok
Test util check is cnpj ... ok
Test util check is not cnpj ... ok
Test valid id ... ok
Test not valid id found ... ok
Test not valid id requered ... ok
Test not valid id number ... ok
Test valid tradingName ... ok
Test not valid tradingName found ... ok
Test not valid tradingName requered ... ok
Test not valid tradingName string ... ok
Test not valid tradingName min_length ... ok
Test valid ownerName ... ok
Test not valid ownerName found ... ok
Test not valid ownerName requered ... ok
Test not valid ownerName string ... ok
Test not valid ownerName min_length ... ok
Test valid document ... ok
Test not valid document found ... ok
Test not valid document requered ... ok
Test not valid document string ... ok
Test not valid document length ... ok
Test not valid document cnpj ... ok
Test valid coverageArea ... ok
Test not valid coverageArea found ... ok
Test not valid coverageArea dict ... ok
Test not valid coverageArea requered ... ok
Test not valid item coverageArea type found ... ok
Test not valid item coverageArea type requered ... ok
Test not valid item coverageArea type incorrect ... ok
Test not valid item coverageArea coordinates found ... ok
Test not valid item coverageArea coordinates requered ... ok
Test not valid item coverageArea coordinates list ... ok
Test valid address ... ok
Test not valid address found ... ok
Test not valid address requered ... ok
Test not valid address dict ... ok
Test not valid item address type found ... ok
Test not valid item address type requered ... ok
Test not valid item address type incorrect ... ok
Test not valid item address coordinates found ... ok
Test not valid item address coordinates requered ... ok
Test not valid item address coordinates list ... ok

----------------------------------------------------------------------
Ran 58 tests in 0.222s

OK
```
