"""The Endpoints to manage the BOOK_REQUESTS"""
from business import ValidPartner, Hydrator, Partner
from flask import jsonify, request, Blueprint
from flask_cors import CORS, cross_origin
import os
import logging


REQUEST_API = Blueprint('partner', __name__)


def get_blueprint():
    """Return the blueprint for the main app module"""
    return REQUEST_API


@REQUEST_API.route('/search/{ltn}/{lat}', methods=['GET'])
@cross_origin()
def partner_geo_search(ltn, lat):
    """Search partner
    @param id: string : id partner
    with application/json mimetype.
    @return: 200: flask/response object
    @raise 400: Failed. Bad post data.
    @raise 404: Failed. Not found.
    @raise 500: Failed. Server Error.
    """

    try:
        partner = Partner()
        registers = partner.geo_search(ltn, lat)
        if registers:
            partners = []
            for item in registers:
                partners.append(Hydrator(item).encode_partner())
            logging.debug(f'Success search - 202 - {id}')
            return jsonify(partners), 202
        else:
            logging.error(f'Error search - 404 - Not found')
            return jsonify({'exist': 'Partner Not found'}), 404

    except expression as identifier:
        logging.error(f'Error search geo partner - 500 - System', identifier)
        return jsonify({'error': identifier}), 500


@REQUEST_API.route('/partner/{id}', methods=['GET'])
@cross_origin()
def partner_find(id):
    """Find partner
    @param id: string : id partner
    with application/json mimetype.
    @return: 200: flask/response object.
    @raise 400: Failed. Bad post data.
    @raise 404: Failed. Not found.
    @raise 500: Failed. Server Error.
    """
    try:
        partner = Partner(id)
        if partner.search():
            register = Hydrator(partner.register).encode_partner()
            logging.debug(f'Success search - 202 - {id}')
            return jsonify(register), 202
        else:
            logging.error(f'Error search - 404 - Not found')
            return jsonify({'exist': 'Partner Not found'}), 404
    except expression as identifier:
        logging.error(f'Error search - 500 - System', identifier)
        return jsonify({'error': identifier}), 500


@REQUEST_API.route('/partner/{id}', methods=['PUT'])
@cross_origin()
def partner_update(id):
    """Update partner
    @param id: string : id partner
    with application/json mimetype.
    @return: 202: flask/response object.
    @raise 400: Failed. Bad post data.
    @raise 404: Failed. Not found.
    @raise 500: Failed. Server Error.
    """
    try:
        data = request.get_json(force=True)
        valid = ValidPartner(data)

        if valid.error:
            logging.error(f'Error update - 400 - Validate')
            return jsonify(valid.error), 400

        register = Hydrator(data).decode_partner()

        partner = Partner(id)
        if partner.update(register):
            logging.debug(f'Success update - 202 - {id}')
            return jsonify({'update': True}), 202
        else:
            logging.error(f'Error update - 404 - Not found')
            return jsonify({'exist': 'Partner Not found'}), 404

    except expression as identifier:
        logging.error(f'Error update - 500 - System', identifier)
        return jsonify({'error': identifier}), 500


@REQUEST_API.route('/partner/{id}', methods=['DELETE'])
@cross_origin()
def partner_delete(id):
    """Create partner
    @param id: string : id partner
    with application/json mimetype.
    @return: 202: flask/response object.
    @raise 400: Failed. Bad post data.
    @raise 404: Failed. Not found.
    @raise 500: Failed. Server Error.
    """
    try:
        partner = Partner(id)
        if partner.delete():
            logging.debug(f'Success delete - 202 - {id}')
            return jsonify({'delete': True}), 202
        else:
            logging.error(f'Error delete - 404 - Not found')
            return jsonify({'exist': 'Partner Not found'}), 404

    except expression as identifier:
        logging.error(f'Error delete - 500 - System', identifier)
        return jsonify({'error': identifier}), 500


@REQUEST_API.route('/partner/', methods=['POST'])
@cross_origin()
def partner_create():
    """Create partner
    with application/json mimetype.
    @return: 201: flask/response object.
    @raise 400: Failed. Bad post data.
    @raise 409: Failed. Data duplicated.
    @raise 500: Failed. Server Error.
    """
    try:
        data = request.get_json(force=True)
        valid = ValidPartner(data)

        if valid.error:
            logging.error(f'Error create - 400 - Validate')
            return jsonify(valid.error), 400

        register = Hydrator(data).decode_partner()

        partner = Partner()
        if partner.create(register):
            logging.debug(f'Success create - 201 - {data["tradingName"]}')
            return jsonify({'create': True}), 201
        else:
            logging.error(f'Error create - 409 - Exist')
            return jsonify({'exist': 'Partner already exists'}), 409

    except expression as identifier:
        logging.error(f'Error create - 500 - System', identifier)
        return jsonify({'error': identifier}), 500
