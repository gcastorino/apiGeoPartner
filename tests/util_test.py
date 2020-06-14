"""The tests to run in this project.
To run the tests type,
$ nosetests --verbose
"""

from nose.tools import assert_true, assert_false
from business.util import Check
import os

# check found


def test_is_found():
    "Test check is found"
    check = Check()
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
    checking = check._is_found('id', PAYLOAD)
    assert_true(checking)


def test_is_not_found():
    "Test check is not found"
    check = Check()
    PAYLOAD_NOT_FOUND = {}
    checking = check._is_found('id', PAYLOAD_NOT_FOUND)
    assert_false(checking)


# check requered

def test_is_requered():
    "Test check is requered"
    check = Check()
    checking = check._is_requered('address')
    assert_true(checking)


def test_is_not_requered():
    "Test check is not requered"
    check = Check()
    checking = check._is_requered("")
    assert_false(checking)


# check longitude

def test_is_lnt():
    "Test check is longitude"
    check = Check()
    checking = check._is_lnt(-94.40)
    assert_true(checking)


def test_is_not_lnt():
    "Test check is not longitude"
    check = Check()
    checking = check._is_lnt(181)
    assert_false(checking)


# check latitude

def test_is_lat():
    "Test check is latitude"
    check = Check()
    checking = check._is_lat(-84.40)
    assert_true(checking)


def test_is_not_lat():
    "Test check is not latitude"
    check = Check()
    checking = check._is_lat(-94.40)
    assert_false(checking)


# check string

def test_is_string():
    "Test check is string"
    check = Check()
    checking = check._is_string('Zé da Silva')
    assert_true(checking)


def test_is_not_string():
    "Test check is not string"
    check = Check()
    checking = check._is_string(3)
    assert_false(checking)


# check int

def test_is_int():
    "Test check is int"
    check = Check()
    checking = check._is_int(3)
    assert_true(checking)


def test_is_not_int():
    "Test check is not int"
    check = Check()
    checking = check._is_int('Zé da Silva')
    assert_false(checking)


# check dict


def test_is_disc():
    "Test check is disc"
    check = Check()
    checking = check._is_dict({'Zé da Silva': [10, 10]})
    assert_true(checking)


def test_is_not_disc():
    "Test check is not disc"
    check = Check()
    checking = check._is_dict([10, 10])
    assert_false(checking)


# check list


def test_is_list():
    "Test check is list"
    check = Check()
    checking = check._is_list([10, 10])
    assert_true(checking)


def test_is_not_list():
    "Test check is not list"
    check = Check()
    checking = check._is_list("[10,10]")
    assert_false(checking)


# check min length

def test_is_min_length():
    "Test check is min length"
    check = Check()
    checking = check._is_min_length('Zé da Silva', 5)
    assert_true(checking)


def test_is_not_min_length():
    "Test check is not min length"
    check = Check()
    checking = check._is_min_length('Zé', 5)
    assert_false(checking)


# check length

def test_is_length():
    "Test check is length"
    check = Check()
    checking = check._is_length("23.485.957/0001-70", 18)
    assert_true(checking)


def test_is_not_length():
    "Test check is not length"
    check = Check()
    checking = check._is_length('23485957000170', 18)
    assert_false(checking)


# check cnpj

def test_is_cnpj():
    "Test check is cnpj"
    check = Check()
    checking = check._is_cnpj("23.485.957/0001-70")
    assert_true(checking)


def test_is_not_cnpj():
    "Test check is not cnpj"
    check = Check()
    checking = check._is_cnpj('1432132123891/0001')
    assert_false(checking)
