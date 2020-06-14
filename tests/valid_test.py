"""The tests to run in this project.
To run the tests type,
$ nosetests --verbose
"""

from nose.tools import assert_true, assert_false, assert_equal
from business.is_valid_partner import ValidPartner
import os

PAYLOAD = {
    "id": 1,
    "tradingName": "Adega da Cerveja - Pinheiros",
    "ownerName": "Zé da Silva",
    "document": "23.485.957/0001-70",
    "coverageArea": {
        "type": "MultiPolygon",
        "coordinates": [
                [[[30, 20], [45, 40], [10, 40], [30, 20]]],
                [[[15, 5], [40, 10], [10, 20], [5, 10], [15, 5]]]
        ]
    },
    "address": {
        "type": "Point",
        "coordinates": [-46.57421, -21.785741]
    },
}
PAYLOAD_NOT_VALID_STRING = {
    "tradingName": 2.3,
    "ownerName": 2,
    "document": 20,
}
PAYLOAD_NOT_VALID_REQUERED = {
    "id": "",
    "tradingName": "",
    "ownerName": "",
    "document": "",
    "coverageArea": "",
    "address": "",
}
PAYLOAD_NOT_VALID_MIN_LENGTH = {
    "tradingName": "Zé",
    "ownerName": "Zé"
}


# is valid id
# - exist
# - requered
# - type number

def test_id_valid():
    "Test valid id"
    valid = ValidPartner(PAYLOAD)
    error = False
    if valid.errors:
        for item in valid.errors:
            if 'id' in item.keys():
                error = True

    assert_false(error)


def test_id_not_found():
    "Test valid id not found"
    valid = ValidPartner({})
    if valid.errors:
        error = ''
        for item in valid.errors:
            if 'id' in item.keys():
                error = item['id']
        assert_equal(error, os.getenv('ERROR_TEXT_NOT_FOUND'))


def test_id_not_requered():
    "Test valid id not requered"
    valid = ValidPartner(PAYLOAD_NOT_VALID_REQUERED)
    if valid.errors:
        error = ''
        for item in valid.errors:
            if 'id' in item.keys():
                error = item['id']
        assert_equal(error, os.getenv('ERROR_TEXT_REQUIRED'))


def test_id_not_int():
    "Test valid id not number"
    valid = ValidPartner({
        "id": "s3"
    })
    if valid.errors:
        error = ''
        for item in valid.errors:
            if 'id' in item.keys():
                error = item['id']
        assert_equal(error, os.getenv('ERROR_TEXT_NUMBER'))


# is valid tradingName
# - exist
# - requered
# - type string
# - min length


def test_tradingName_valid():
    "Test valid tradingName"
    valid = ValidPartner(PAYLOAD)
    error = False
    if valid.errors:
        for item in valid.errors:
            if 'tradingName' in item.keys():
                error = True

    assert_false(error)


def test_tradingName_not_found():
    "Test valid tradingName not found"
    valid = ValidPartner({})
    if valid.errors:
        error = ''
        for item in valid.errors:
            if 'tradingName' in item.keys():
                error = item['tradingName']
        assert_equal(error, os.getenv('ERROR_TEXT_NOT_FOUND'))


def test_tradingName_not_requered():
    "Test valid tradingName not requered"
    valid = ValidPartner(PAYLOAD_NOT_VALID_REQUERED)
    if valid.errors:
        error = ''
        for item in valid.errors:
            if 'tradingName' in item.keys():
                error = item['tradingName']
        assert_equal(error, os.getenv('ERROR_TEXT_REQUIRED'))


def test_tradingName_not_string():
    "Test valid tradingName not string"
    valid = ValidPartner(PAYLOAD_NOT_VALID_STRING)
    if valid.errors:
        error = ''
        for item in valid.errors:
            if 'tradingName' in item.keys():
                error = item['tradingName']
        assert_equal(error, os.getenv('ERROR_TEXT_STRING'))


def test_tradingName_not_min_length():
    "Test valid tradingName not min length"
    valid = ValidPartner(PAYLOAD_NOT_VALID_MIN_LENGTH)
    if valid.errors:
        error = ''
        for item in valid.errors:
            if 'tradingName' in item.keys():
                error = item['tradingName']
        assert_equal(error, os.getenv('ERROR_TEXT_MIN_LENGTH') + ' 5')


# is valid ownerName
# - exist
# - requered
# - type string
# - min length


def test_ownerName_valid():
    "Test valid ownerName"
    valid = ValidPartner(PAYLOAD)
    error = False
    if valid.errors:
        for item in valid.errors:
            if 'ownerName' in item.keys():
                error = True
    assert_false(error)


def test_ownerName_not_found():
    "Test valid ownerName not found"
    valid = ValidPartner({})
    if valid.errors:
        error = ''
        for item in valid.errors:
            if 'ownerName' in item.keys():
                error = item['ownerName']
        assert_equal(error, os.getenv('ERROR_TEXT_NOT_FOUND'))


def test_ownerName_not_requered():
    "Test valid ownerName not requered"
    valid = ValidPartner(PAYLOAD_NOT_VALID_REQUERED)
    if valid.errors:
        error = ''
        for item in valid.errors:
            if 'ownerName' in item.keys():
                error = item['ownerName']
        assert_equal(error, os.getenv('ERROR_TEXT_REQUIRED'))


def test_ownerName_not_string():
    "Test valid ownerName not string"
    valid = ValidPartner(PAYLOAD_NOT_VALID_STRING)
    if valid.errors:
        error = ''
        for item in valid.errors:
            if 'ownerName' in item.keys():
                error = item['ownerName']
        assert_equal(error, os.getenv('ERROR_TEXT_STRING'))


def test_ownerName_not_min_length():
    "Test valid ownerName not min length"
    valid = ValidPartner(PAYLOAD_NOT_VALID_MIN_LENGTH)
    if valid.errors:
        error = ''
        for item in valid.errors:
            if 'ownerName' in item.keys():
                error = item['ownerName']
        assert_equal(error, os.getenv('ERROR_TEXT_MIN_LENGTH') + ' 5')


# is valid document
# - exist
# - requered
# - type string
# - length
# - cnpj

def test_document_valid():
    "Test valid document"
    valid = ValidPartner(PAYLOAD)
    error = False
    if valid.errors:
        for item in valid.errors:
            if 'document' in item.keys():
                error = True

    assert_false(error)


def test_document_not_found():
    "Test valid document not found"
    valid = ValidPartner({})
    if valid.errors:
        error = ''
        for item in valid.errors:
            if 'document' in item.keys():
                error = item['document']
        assert_equal(error,  os.getenv('ERROR_TEXT_NOT_FOUND'))


def test_document_not_requered():
    "Test valid document not requered"
    valid = ValidPartner(PAYLOAD_NOT_VALID_REQUERED)
    if valid.errors:
        error = ''
        for item in valid.errors:
            if 'document' in item.keys():
                error = item['document']
        assert_equal(error,  os.getenv('ERROR_TEXT_REQUIRED'))


def test_document_not_string():
    "Test valid document not string"
    valid = ValidPartner(PAYLOAD_NOT_VALID_STRING)
    if valid.errors:
        error = ''
        for item in valid.errors:
            if 'document' in item.keys():
                error = item['document']
        assert_equal(error, os.getenv('ERROR_TEXT_STRING'))


def test_document_not_length():
    "Test valid document not length"
    valid = ValidPartner({
        "document": '23485957000170'
    })
    if valid.errors:
        error = ''
        for item in valid.errors:
            if 'document' in item.keys():
                error = item['document']
        assert_equal(error,  os.getenv('ERROR_TEXT_LENGTH') + ' 18')


def test_document_not_cnpj():
    "Test valid document not cnpj"
    valid = ValidPartner({
        "document": '1432132123891/0001'
    })
    if valid.errors:
        error = ''
        for item in valid.errors:
            if 'document' in item.keys():
                error = item['document']
        assert_equal(error, os.getenv('ERROR_TEXT_DOCUMENT'))


# is valid coverageArea
# - exist
# - requered
# - object
# - item - type - exist
# - item - type - requered
# - item - type - MultiPolygon
# - item - coordinates - exist
# - item - coordinates - requered
# - item - coordinates - list

PAYLOAD_NOT_VALID_TYPE = {
    "coverageArea": {
        "type": "Point",
        "coordinates": [10, 10]
    },
    "address": {
        "type": "MultiPolygon",
        "coordinates": [10, 10]
    }
}

PAYLOAD_NOT_VALID_LIST = {
    "coverageArea": {
        "type": "MultiPolygon",
        "coordinates": "[10,10]"
    },
    "address": {
        "type": "Point",
        "coordinates": "[10,10]"
    }
}
PAYLOAD_NOT_VALID_DICT = {
    "coverageArea": 2.3,
    "address": 2
}
PAYLOAD_NOT_FOUND_ITEM_TYPE = {

    "coverageArea": {
        "coordinates": [10, 10]
    },
    "address": {
        "coordinates": [10, 10]
    }
}
PAYLOAD_NOT_FOUND_ITEM_COORDINATES = {
    "coverageArea": {
        "type": "MultiPolygon"
    },
    "address": {
        "type": "Point"
    }
}
PAYLOAD_NOT_VALID_REQUERED_ITEM_TYPE = {

    "coverageArea": {
        "type": "",
        "coordinates": [10, 10]
    },
    "address": {
        "type": "",
        "coordinates": [10, 10]
    }
}
PAYLOAD_NOT_VALID_REQUERED_ITEM_COORDINATES = {
    "coverageArea": {
        "type": "MultiPolygon",
        "coordinates": []
    },
    "address": {
        "type": "Point",
        "coordinates": []
    }
}


def test_coverageArea_valid():
    "Test valid coverageArea"
    valid = ValidPartner(PAYLOAD)
    error = False
    if valid.errors:
        for item in valid.errors:
            if 'coverageArea' in item.keys():
                error = True

    assert_false(error)


def test_coverageArea_not_found():
    "Test valid coverageArea not found"
    valid = ValidPartner({})
    if valid.errors:
        error = ''
        for item in valid.errors:
            if 'coverageArea' in item.keys():
                error = item['coverageArea']
        assert_equal(error, os.getenv('ERROR_TEXT_NOT_FOUND'))


def test_coverageArea_not_dict():
    "Test valid coverageArea not dict"
    valid = ValidPartner(PAYLOAD_NOT_VALID_DICT)
    if valid.errors:
        error = ''
        for item in valid.errors:
            if 'coverageArea' in item.keys():
                error = item['coverageArea']
        assert_equal(error, os.getenv('ERROR_TEXT_OBJECT'))


def test_coverageArea_not_requered():
    "Test valid coverageArea not requered"
    valid = ValidPartner(PAYLOAD_NOT_VALID_REQUERED)
    if valid.errors:
        error = ''
        for item in valid.errors:
            if 'coverageArea' in item.keys():
                error = item['coverageArea']
        assert_equal(error, os.getenv('ERROR_TEXT_REQUIRED'))


def test_item_coverageArea_type_not_found():
    "Test valid item coverageArea type not found"
    valid = ValidPartner(PAYLOAD_NOT_FOUND_ITEM_TYPE)
    if valid.errors:
        error = ''
        for item in valid.errors:
            if 'coverageArea' in item.keys():
                error = item['coverageArea']
        assert_equal(error, 'type ' + os.getenv('ERROR_TEXT_NOT_FOUND'))


def test_item_coverageArea_type_not_requered():
    "Test valid item coverageArea type not requered"
    valid = ValidPartner(PAYLOAD_NOT_VALID_REQUERED_ITEM_TYPE)
    if valid.errors:
        error = ''
        for item in valid.errors:
            if 'coverageArea' in item.keys():
                error = item['coverageArea']
        assert_equal(error, 'type ' + os.getenv('ERROR_TEXT_REQUIRED'))


def test_item_coverageArea_type_incorrect():
    "Test valid item coverageArea type not incorrect"
    valid = ValidPartner(PAYLOAD_NOT_VALID_TYPE)
    if valid.errors:
        error = ''
        for item in valid.errors:
            if 'coverageArea' in item.keys():
                error = item['coverageArea']
        assert_equal(error, 'type ' + os.getenv('ERROR_TEXT_INCORRECT'))


def test_item_coverageArea_coordinates_not_found():
    "Test valid item coverageArea coordinates not found"
    valid = ValidPartner(PAYLOAD_NOT_FOUND_ITEM_COORDINATES)
    if valid.errors:
        error = ''
        for item in valid.errors:
            if 'coverageArea' in item.keys():
                error = item['coverageArea']
        assert_equal(error, 'coordinates ' + os.getenv('ERROR_TEXT_NOT_FOUND'))


def test_item_coverageArea_coordinates_not_requered():
    "Test valid item coverageArea coordinates not requered"
    valid = ValidPartner(PAYLOAD_NOT_VALID_REQUERED_ITEM_COORDINATES)
    if valid.errors:
        error = ''
        for item in valid.errors:
            if 'coverageArea' in item.keys():
                error = item['coverageArea']
        assert_equal(error, 'coordinates ' + os.getenv('ERROR_TEXT_REQUIRED'))


def test_item_coverageArea_coordinates_not_list():
    "Test valid item coverageArea coordinates not list"
    valid = ValidPartner(PAYLOAD_NOT_VALID_LIST)
    if valid.errors:
        error = ''
        for item in valid.errors:
            if 'coverageArea' in item.keys():
                error = item['coverageArea']
        assert_equal(error, 'coordinates ' + os.getenv('ERROR_TEXT_LIST'))


# is valid address
# - exist
# - requered
# - object
# - item - type - exist
# - item - type - requered
# - item - type - Point
# - item - coordinates - exist
# - item - coordinates - requered
# - item - coordinates - list
# - item - coordinates - length
# - item - coordinates - longitude
# - item - coordinates - latitude


def test_address_valid():
    "Test valid address"
    valid = ValidPartner(PAYLOAD)
    error = False
    if valid.errors:
        for item in valid.errors:
            if 'address' in item.keys():
                error = True

    assert_false(error)


def test_address_not_found():
    "Test valid address not found"
    valid = ValidPartner({})
    if valid.errors:
        error = ''
        for item in valid.errors:
            if 'address' in item.keys():
                error = item['address']
        assert_equal(error, os.getenv('ERROR_TEXT_NOT_FOUND'))


def test_address_not_requered():
    "Test valid address not requered"
    valid = ValidPartner(PAYLOAD_NOT_VALID_REQUERED)
    if valid.errors:
        error = ''
        for item in valid.errors:
            if 'address' in item.keys():
                error = item['address']
        assert_equal(error, os.getenv('ERROR_TEXT_REQUIRED'))


def test_address_not_dict():
    "Test valid address not dict"
    valid = ValidPartner(PAYLOAD_NOT_VALID_DICT)
    if valid.errors:
        error = ''
        for item in valid.errors:
            if 'address' in item.keys():
                error = item['address']
        assert_equal(error, os.getenv('ERROR_TEXT_OBJECT'))


def test_item_address_type_not_found():
    "Test valid item address type not found"
    valid = ValidPartner(PAYLOAD_NOT_FOUND_ITEM_TYPE)
    if valid.errors:
        error = ''
        for item in valid.errors:
            if 'address' in item.keys():
                error = item['address']
        assert_equal(error, 'type ' + os.getenv('ERROR_TEXT_NOT_FOUND'))


def test_item_address_type_not_requered():
    "Test valid item address type not requered"
    valid = ValidPartner(PAYLOAD_NOT_VALID_REQUERED_ITEM_TYPE)
    if valid.errors:
        error = ''
        for item in valid.errors:
            if 'address' in item.keys():
                error = item['address']
        assert_equal(error, 'type ' + os.getenv('ERROR_TEXT_REQUIRED'))


def test_item_address_type_incorrect():
    "Test valid item address type not incorrect"
    valid = ValidPartner(PAYLOAD_NOT_VALID_TYPE)
    if valid.errors:
        error = ''
        for item in valid.errors:
            if 'address' in item.keys():
                error = item['address']
        assert_equal(error, 'type ' + os.getenv('ERROR_TEXT_INCORRECT'))


def test_item_address_coordinates_not_found():
    "Test valid item address coordinates not found"
    valid = ValidPartner(PAYLOAD_NOT_FOUND_ITEM_COORDINATES)
    if valid.errors:
        error = ''
        for item in valid.errors:
            if 'address' in item.keys():
                error = item['address']
        assert_equal(error, 'coordinates ' + os.getenv('ERROR_TEXT_NOT_FOUND'))


def test_item_address_coordinates_not_requered():
    "Test valid item address coordinates not requered"
    valid = ValidPartner(PAYLOAD_NOT_VALID_REQUERED_ITEM_COORDINATES)
    if valid.errors:
        error = ''
        for item in valid.errors:
            if 'address' in item.keys():
                error = item['address']
        assert_equal(error, 'coordinates ' + os.getenv('ERROR_TEXT_REQUIRED'))


def test_item_address_coordinates_not_list():
    "Test valid item address coordinates not list"
    valid = ValidPartner(PAYLOAD_NOT_VALID_LIST)
    if valid.errors:
        error = ''
        for item in valid.errors:
            if 'address' in item.keys():
                error = item['address']
        assert_equal(error, 'coordinates ' + os.getenv('ERROR_TEXT_LIST'))


def test_item_address_coordinates_not_length():
    "Test valid item address coordinates not length"
    valid = ValidPartner({
        "address": {
            "type": "Point",
            "coordinates": [190]
        }
    })
    if valid.errors:
        error = ''
        for item in valid.errors:
            if 'address' in item.keys():
                error = item['address']
        assert_equal(error, 'coordinates ' +
                     os.getenv('ERROR_TEXT_LENGTH') + ' 2')


def test_item_address_coordinates_not_longitude():
    "Test valid item address coordinates not longitude"
    valid = ValidPartner({
        "address": {
            "type": "Point",
            "coordinates": [190, 90]
        }
    })
    if valid.errors:
        error = ''
        for item in valid.errors:
            if 'address' in item.keys():
                error = item['address']
        assert_equal(error, 'longitude ' + os.getenv('ERROR_TEXT_INCORRECT'))


def test_item_address_coordinates_not_latitude():
    "Test valid item address coordinates not latitude"
    valid = ValidPartner({
        "address": {
            "type": "Point",
            "coordinates": [90, 900]
        }
    })
    if valid.errors:
        error = ''
        for item in valid.errors:
            if 'address' in item.keys():
                error = item['address']
        assert_equal(error, 'latitude ' + os.getenv('ERROR_TEXT_INCORRECT'))
