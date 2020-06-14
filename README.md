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

### Technologies chosen

The programming language **Python** and the database **Mongo**

## Install and deploy

### Requered

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

### Or Docker

The project is ready to install and deploy in a Docker container.

```sh
docker-compose -f "apiGeoPartner/docker-compose.yml" up -d --build
```

### Index Geo database

```sh
db.getCollection("partner").createIndex({ "coverageArea": "2dsphere" });
db.getCollection("partner").createIndex({ "address": "2dsphere" })
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

## Tests Output

### Unit Test with Nose

```sh
nosetests --verbosity=2
```

### Result

```
Test check is found ... ok
Test check is not found ... ok
Test check is requered ... ok
Test check is not requered ... ok
Test check is longitude ... ok
Test check is not longitude ... ok
Test check is latitude ... ok
Test check is not latitude ... ok
Test check is string ... ok
Test check is not string ... ok
Test check is int ... ok
Test check is not int ... ok
Test check is disc ... ok
Test check is not disc ... ok
Test check is list ... ok
Test check is not list ... ok
Test check is min length ... ok
Test check is not min length ... ok
Test check is length ... ok
Test check is not length ... ok
Test check is cnpj ... ok
Test check is not cnpj ... ok
Test valid id ... ok
Test valid id not found ... ok
Test valid id not requered ... ok
Test valid id not number ... ok
Test valid tradingName ... ok
Test valid tradingName not found ... ok
Test valid tradingName not requered ... ok
Test valid tradingName not string ... ok
Test valid tradingName not min length ... ok
Test valid ownerName ... ok
Test valid ownerName not found ... ok
Test valid ownerName not requered ... ok
Test valid ownerName not string ... ok
Test valid ownerName not min length ... ok
Test valid document ... ok
Test valid document not found ... ok
Test valid document not requered ... ok
Test valid document not string ... ok
Test valid document not length ... ok
Test valid document not cnpj ... ok
Test valid coverageArea ... ok
Test valid coverageArea not found ... ok
Test valid coverageArea not dict ... ok
Test valid coverageArea not requered ... ok
Test valid item coverageArea type not found ... ok
Test valid item coverageArea type not requered ... ok
Test valid item coverageArea type not incorrect ... ok
Test valid item coverageArea coordinates not found ... ok
Test valid item coverageArea coordinates not requered ... ok
Test valid item coverageArea coordinates not list ... ok
Test valid address ... ok
Test valid address not found ... ok
Test valid address not requered ... ok
Test valid address not dict ... ok
Test valid item address type not found ... ok
Test valid item address type not requered ... ok
Test valid item address type not incorrect ... ok
Test valid item address coordinates not found ... ok
Test valid item address coordinates not requered ... ok
Test valid item address coordinates not list ... ok
Test valid item address coordinates not length ... ok
Test valid item address coordinates not longitude ... ok
Test valid item address coordinates not latitude ... ok

----------------------------------------------------------------------
Ran 65 tests in 0.162s

OK
```
