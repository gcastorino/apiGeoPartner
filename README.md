# Api Geo Partner
API using REST for partner CRUD and partner search by geo location

start Project
docker-compose -f "apiGeoPartner/docker-compose.yml" up -d --build

Docker Run 
docker run -p 27017:27017 --name db-partner -d --network sizijaynetwork mongo

create index database
getCollectionIndexInfo("partner","coverageArea_2dsphere");

## Tests Units
Command  = nosetests --verbose --nocapture
'''
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
'''