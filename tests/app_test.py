"""The tests to run in this project.
To run the tests type,
$ nosetests --verbose
"""

from nose.tools import assert_true, assert_false, assert_equal
from business.util import Check
from business.is_valid_partner import ValidPartner
import requests
import os

BASE_URL = os.environ.get('BASE_URL')

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


# check found
PAYLOAD_NOT_FOUND = {}
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


def test_is_found():
    "Test util check is found"
    check = Check()
    checking = check._is_found('address', PAYLOAD)
    assert_true(checking)


def test_is_not_found():
    "Test util check is not found"
    check = Check()
    checking = check._is_found('address', PAYLOAD_NOT_FOUND)
    assert_false(checking)


# check requered
PAYLOAD_NOT_VALID_REQUERED = {
    "id": "",
    "tradingName": "",
    "ownerName": "",
    "document": "",
    "coverageArea": "",
    "address": "",
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


def test_is_requered():
    "Test util check is requered"
    check = Check()
    checking = check._is_requered(PAYLOAD['address'])
    assert_true(checking)


def test_is_not_requered():
    "Test util check is not requered"
    check = Check()
    checking = check._is_requered(PAYLOAD_NOT_VALID_REQUERED['address'])
    assert_false(checking)


# check string
PAYLOAD_NOT_VALID_STRING = {
    "tradingName": 2.3,
    "ownerName": 2,
    "document": 20,
}


def test_is_string():
    "Test util check is string"
    check = Check()
    checking = check._is_string(PAYLOAD['tradingName'])
    assert_true(checking)


def test_is_not_string():
    "Test util check is not string"
    check = Check()
    checking = check._is_string(PAYLOAD_NOT_VALID_STRING['tradingName'])
    assert_false(checking)


# check int
PAYLOAD_NOT_VALID_INT = {
    "id": "s3"
}


def test_is_int():
    "Test util check is int"
    check = Check()
    checking = check._is_int(PAYLOAD['id'])
    assert_true(checking)


def test_is_not_int():
    "Test util check is not int"
    check = Check()
    checking = check._is_int(PAYLOAD_NOT_VALID_INT['id'])
    assert_false(checking)


# check dict
PAYLOAD_NOT_VALID_DICT = {
    "coverageArea": 2.3,
    "address": 2
}


def test_is_disc():
    "Test util check is disc"
    check = Check()
    checking = check._is_dict(PAYLOAD['coverageArea'])
    assert_true(checking)


def test_is_not_disc():
    "Test util check is not disc"
    check = Check()
    checking = check._is_dict(PAYLOAD_NOT_VALID_DICT['coverageArea'])
    assert_false(checking)


# check list
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


def test_is_list():
    "Test util check is list"
    check = Check()
    checking = check._is_list(PAYLOAD['coverageArea']['coordinates'])
    assert_true(checking)


def test_is_not_list():
    "Test util check is not list"
    check = Check()
    checking = check._is_list(
        PAYLOAD_NOT_VALID_LIST['coverageArea']['coordinates'])
    assert_false(checking)


# check min length
PAYLOAD_NOT_VALID_MIN_LENGTH = {
    "tradingName": "Zé",
    "ownerName": "Zé"
}


def test_is_min_length():
    "Test util check is min length"
    check = Check()
    checking = check._is_min_length(PAYLOAD['ownerName'], 5)
    assert_true(checking)


def test_is_not_min_length():
    "Test util check is not min length"
    check = Check()
    checking = check._is_min_length(
        PAYLOAD_NOT_VALID_MIN_LENGTH['ownerName'], 5)
    assert_false(checking)


# check length
PAYLOAD_NOT_VALID_LENGTH = {
    "document": '23485957000170'
}


def test_is_length():
    "Test util check is length"
    check = Check()
    checking = check._is_length(PAYLOAD['document'], 18)
    assert_true(checking)


def test_is_not_length():
    "Test util check is not length"
    check = Check()
    checking = check._is_length(PAYLOAD_NOT_VALID_LENGTH['document'], 18)
    assert_false(checking)


# check cnpj
PAYLOAD_NOT_VALID_CNPJ = {
    "document": '1432132123891/0001'
}


def test_is_cnpj():
    "Test util check is cnpj"
    check = Check()
    checking = check._is_cnpj(PAYLOAD['document'])
    assert_true(checking)


def test_is_not_cnpj():
    "Test util check is not cnpj"
    check = Check()
    checking = check._is_cnpj(PAYLOAD_NOT_VALID_CNPJ['document'])
    assert_false(checking)


# is valid id
# - exist
# - requered
# - type number


def test_id_valid():
    "Test valid id"
    valid = ValidPartner(PAYLOAD)
    if valid.errors:
        for item in valid.errors:
            if 'id' in item.keys():
                assert_false(valid.errors)
    else:
        assert_false(valid.errors)


def test_id_not_found():
    "Test not valid id found"
    valid = ValidPartner(PAYLOAD_NOT_FOUND)
    if valid.errors:
        for item in valid.errors:
            if 'id' in item.keys():
                assert_equal(item['id'], os.getenv('ERROR_TEXT_NOT_FOUND'))


def test_id_not_requered():
    "Test not valid id requered"
    valid = ValidPartner(PAYLOAD_NOT_VALID_REQUERED)
    if valid.errors:
        for item in valid.errors:
            if 'id' in item.keys():
                assert_equal(item['id'], os.getenv('ERROR_TEXT_REQUIRED'))


def test_id_not_int():
    "Test not valid id number"
    valid = ValidPartner(PAYLOAD_NOT_VALID_INT)
    if valid.errors:
        for item in valid.errors:
            if 'id' in item.keys():
                assert_equal(item['id'], os.getenv('ERROR_TEXT_NUMBER'))


# is valid tradingName
# - exist
# - requered
# - type string
# - min length


def test_tradingName_valid():
    "Test valid tradingName"
    valid = ValidPartner(PAYLOAD)
    if valid.errors:
        for item in valid.errors:
            if 'tradingName' in item.keys():
                assert_true(valid.errors)
    else:
        assert_false(valid.errors)


def test_tradingName_not_found():
    "Test not valid tradingName found"
    valid = ValidPartner(PAYLOAD_NOT_FOUND)
    if valid.errors:
        for item in valid.errors:
            if 'tradingName' in item.keys():
                assert_equal(item['tradingName'],
                             os.getenv('ERROR_TEXT_NOT_FOUND'))


def test_tradingName_not_requered():
    "Test not valid tradingName requered"
    valid = ValidPartner(PAYLOAD_NOT_VALID_REQUERED)
    if valid.errors:
        for item in valid.errors:
            if 'tradingName' in item.keys():
                assert_equal(item['tradingName'],
                             os.getenv('ERROR_TEXT_REQUIRED'))


def test_tradingName_not_string():
    "Test not valid tradingName string"
    valid = ValidPartner(PAYLOAD_NOT_VALID_STRING)
    if valid.errors:
        for item in valid.errors:
            if 'tradingName' in item.keys():
                assert_equal(item['tradingName'],
                             os.getenv('ERROR_TEXT_STRING'))


def test_tradingName_not_min_length():
    "Test not valid tradingName min_length"
    valid = ValidPartner(PAYLOAD_NOT_VALID_MIN_LENGTH)
    if valid.errors:
        for item in valid.errors:
            if 'tradingName' in item.keys():
                assert_equal(item['tradingName'], os.getenv(
                    'ERROR_TEXT_MIN_LENGTH') + ' 5')


# is valid ownerName
# - exist
# - requered
# - type string
# - min length


def test_ownerName_valid():
    "Test valid ownerName"
    valid = ValidPartner(PAYLOAD)
    if valid.errors:
        for item in valid.errors:
            if 'ownerName' in item.keys():
                assert_true(valid.errors)
    else:
        assert_false(valid.errors)


def test_ownerName_not_found():
    "Test not valid ownerName found"
    valid = ValidPartner(PAYLOAD_NOT_FOUND)
    if valid.errors:
        for item in valid.errors:
            if 'ownerName' in item.keys():
                assert_equal(item['ownerName'], os.getenv(
                    'ERROR_TEXT_NOT_FOUND'))


def test_ownerName_not_requered():
    "Test not valid ownerName requered"
    valid = ValidPartner(PAYLOAD_NOT_VALID_REQUERED)
    if valid.errors:
        for item in valid.errors:
            if 'ownerName' in item.keys():
                assert_equal(item['ownerName'],
                             os.getenv('ERROR_TEXT_REQUIRED'))


def test_ownerName_not_string():
    "Test not valid ownerName string"
    valid = ValidPartner(PAYLOAD_NOT_VALID_STRING)
    if valid.errors:
        for item in valid.errors:
            if 'ownerName' in item.keys():
                assert_equal(item['ownerName'], os.getenv('ERROR_TEXT_STRING'))


def test_ownerName_not_min_length():
    "Test not valid ownerName min_length"
    valid = ValidPartner(PAYLOAD_NOT_VALID_MIN_LENGTH)
    if valid.errors:
        for item in valid.errors:
            if 'ownerName' in item.keys():
                assert_equal(item['ownerName'], os.getenv(
                    'ERROR_TEXT_MIN_LENGTH') + ' 5')


# is valid document
# - exist
# - requered
# - type string
# - length
# - cnpj


def test_document_valid():
    "Test valid document"
    valid = ValidPartner(PAYLOAD)
    if valid.errors:
        for item in valid.errors:
            if 'document' in item.keys():
                assert_true(valid.errors)
    else:
        assert_false(valid.errors)


def test_document_not_found():
    "Test not valid document found"
    valid = ValidPartner(PAYLOAD_NOT_FOUND)
    if valid.errors:
        for item in valid.errors:
            if 'document' in item.keys():
                assert_equal(item['document'], os.getenv(
                    'ERROR_TEXT_NOT_FOUND'))


def test_document_not_requered():
    "Test not valid document requered"
    valid = ValidPartner(PAYLOAD_NOT_VALID_REQUERED)
    if valid.errors:
        for item in valid.errors:
            if 'document' in item.keys():
                assert_equal(item['document'], os.getenv(
                    'ERROR_TEXT_REQUIRED'))


def test_document_not_string():
    "Test not valid document string"
    valid = ValidPartner(PAYLOAD_NOT_VALID_STRING)
    if valid.errors:
        for item in valid.errors:
            if 'document' in item.keys():
                assert_equal(item['document'], os.getenv('ERROR_TEXT_STRING'))


def test_document_not_length():
    "Test not valid document length"
    valid = ValidPartner(PAYLOAD_NOT_VALID_LENGTH)
    if valid.errors:
        for item in valid.errors:
            if 'document' in item.keys():
                assert_equal(item['document'], os.getenv(
                    'ERROR_TEXT_LENGTH') + ' 18')


def test_document_not_cnpj():
    "Test not valid document cnpj"
    valid = ValidPartner(PAYLOAD_NOT_VALID_CNPJ)
    if valid.errors:
        for item in valid.errors:
            if 'document' in item.keys():
                assert_equal(item['document'], os.getenv(
                    'ERROR_TEXT_DOCUMENT'))


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

def test_coverageArea_valid():
    "Test valid coverageArea"
    valid = ValidPartner(PAYLOAD)
    if valid.errors:
        for item in valid.errors:
            if 'coverageArea' in item.keys():
                assert_true(valid.errors)
    else:
        assert_false(valid.errors)


def test_coverageArea_not_found():
    "Test not valid coverageArea found"
    valid = ValidPartner(PAYLOAD_NOT_FOUND)
    if valid.errors:
        for item in valid.errors:
            if 'coverageArea' in item.keys():
                assert_equal(item['coverageArea'],
                             os.getenv('ERROR_TEXT_NOT_FOUND'))


def test_coverageArea_not_dict():
    "Test not valid coverageArea dict"
    valid = ValidPartner(PAYLOAD_NOT_VALID_DICT)
    if valid.errors:
        for item in valid.errors:
            if 'coverageArea' in item.keys():
                assert_equal(item['coverageArea'],
                             os.getenv('ERROR_TEXT_OBJECT'))


def test_coverageArea_not_requered():
    "Test not valid coverageArea requered"
    valid = ValidPartner(PAYLOAD_NOT_VALID_REQUERED)
    if valid.errors:
        for item in valid.errors:
            if 'coverageArea' in item.keys():
                assert_equal(item['coverageArea'],
                             os.getenv('ERROR_TEXT_REQUIRED'))


def test_item_coverageArea_type_not_found():
    "Test not valid item coverageArea type found"
    valid = ValidPartner(PAYLOAD_NOT_FOUND_ITEM_TYPE)
    if valid.errors:
        for item in valid.errors:
            if 'coverageArea' in item.keys():
                assert_equal(item['coverageArea'], 'type ' +
                             os.getenv('ERROR_TEXT_NOT_FOUND'))


def test_item_coverageArea_type_not_requered():
    "Test not valid item coverageArea type requered"
    valid = ValidPartner(PAYLOAD_NOT_VALID_REQUERED_ITEM_TYPE)
    if valid.errors:
        for item in valid.errors:
            if 'coverageArea' in item.keys():
                assert_equal(item['coverageArea'], 'type ' +
                             os.getenv('ERROR_TEXT_REQUIRED'))


def test_item_coverageArea_type_incorrect():
    "Test not valid item coverageArea type incorrect"
    valid = ValidPartner(PAYLOAD_NOT_VALID_TYPE)
    if valid.errors:
        for item in valid.errors:
            if 'coverageArea' in item.keys():
                assert_equal(item['coverageArea'], 'type ' +
                             os.getenv('ERROR_TEXT_INCORRECT'))


def test_item_coverageArea_coordinates_not_found():
    "Test not valid item coverageArea coordinates found"
    valid = ValidPartner(PAYLOAD_NOT_FOUND_ITEM_COORDINATES)
    if valid.errors:
        for item in valid.errors:
            if 'coverageArea' in item.keys():
                assert_equal(item['coverageArea'], 'coordinates ' +
                             os.getenv('ERROR_TEXT_NOT_FOUND'))


def test_item_coverageArea_coordinates_not_requered():
    "Test not valid item coverageArea coordinates requered"
    valid = ValidPartner(PAYLOAD_NOT_VALID_REQUERED_ITEM_COORDINATES)
    if valid.errors:
        for item in valid.errors:
            if 'coverageArea' in item.keys():
                assert_equal(item['coverageArea'], 'coordinates ' +
                             os.getenv('ERROR_TEXT_REQUIRED'))


def test_item_coverageArea_coordinates_not_list():
    "Test not valid item coverageArea coordinates list"
    valid = ValidPartner(PAYLOAD_NOT_VALID_LIST)
    if valid.errors:
        for item in valid.errors:
            if 'coverageArea' in item.keys():
                assert_equal(item['coverageArea'], 'coordinates ' +
                             os.getenv('ERROR_TEXT_LIST'))


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


def test_address_valid():
    "Test valid address"
    valid = ValidPartner(PAYLOAD)
    if valid.errors:
        for item in valid.errors:
            if 'address' in item.keys():
                assert_true(valid.errors)
    else:
        assert_false(valid.errors)


def test_address_not_found():
    "Test not valid address found"
    valid = ValidPartner(PAYLOAD_NOT_FOUND)
    if valid.errors:
        for item in valid.errors:
            if 'address' in item.keys():
                assert_equal(item['address'], os.getenv(
                    'ERROR_TEXT_NOT_FOUND'))


def test_address_not_requered():
    "Test not valid address requered"
    valid = ValidPartner(PAYLOAD_NOT_VALID_REQUERED)
    if valid.errors:
        for item in valid.errors:
            if 'address' in item.keys():
                assert_equal(item['address'], os.getenv('ERROR_TEXT_REQUIRED'))


def test_address_not_dict():
    "Test not valid address dict"
    valid = ValidPartner(PAYLOAD_NOT_VALID_DICT)
    if valid.errors:
        for item in valid.errors:
            if 'address' in item.keys():
                assert_equal(item['address'], os.getenv('ERROR_TEXT_OBJECT'))


def test_item_address_type_not_found():
    "Test not valid item address type found"
    valid = ValidPartner(PAYLOAD_NOT_FOUND_ITEM_TYPE)
    if valid.errors:
        for item in valid.errors:
            if 'address' in item.keys():
                assert_equal(item['address'], 'type ' +
                             os.getenv('ERROR_TEXT_NOT_FOUND'))


def test_item_address_type_not_requered():
    "Test not valid item address type requered"
    valid = ValidPartner(PAYLOAD_NOT_VALID_REQUERED_ITEM_TYPE)
    if valid.errors:
        for item in valid.errors:
            if 'address' in item.keys():
                assert_equal(item['address'], 'type ' +
                             os.getenv('ERROR_TEXT_REQUIRED'))


def test_item_address_type_incorrect():
    "Test not valid item address type incorrect"
    valid = ValidPartner(PAYLOAD_NOT_VALID_TYPE)
    if valid.errors:
        for item in valid.errors:
            if 'address' in item.keys():
                assert_equal(item['address'], 'type ' +
                             os.getenv('ERROR_TEXT_INCORRECT'))


def test_item_address_coordinates_not_found():
    "Test not valid item address coordinates found"
    valid = ValidPartner(PAYLOAD_NOT_FOUND_ITEM_COORDINATES)
    if valid.errors:
        for item in valid.errors:
            if 'address' in item.keys():
                assert_equal(item['address'], 'coordinates ' +
                             os.getenv('ERROR_TEXT_NOT_FOUND'))


def test_item_address_coordinates_not_requered():
    "Test not valid item address coordinates requered"
    valid = ValidPartner(PAYLOAD_NOT_VALID_REQUERED_ITEM_COORDINATES)
    if valid.errors:
        for item in valid.errors:
            if 'address' in item.keys():
                assert_equal(item['address'], 'coordinates ' +
                             os.getenv('ERROR_TEXT_REQUIRED'))


def test_item_address_coordinates_not_list():
    "Test not valid item address coordinates list"
    valid = ValidPartner(PAYLOAD_NOT_VALID_LIST)
    if valid.errors:
        for item in valid.errors:
            if 'address' in item.keys():
                assert_equal(item['address'], 'coordinates ' +
                             os.getenv('ERROR_TEXT_LIST'))
