"""The Endpoints to manage the BOOK_REQUESTS"""
from business.partner import Partner
from flask import jsonify, request, Blueprint, Response
from flask_cors import CORS, cross_origin
import os
import logger_config
import ujson


REQUEST_API = Blueprint('partner', __name__)


def get_blueprint():
    """Return the blueprint for the main app module"""
    return REQUEST_API


@REQUEST_API.route('/geo-partner/<lnt>/<lat>', methods=['GET'])
def partner_geo_search(lnt, lat):
    """search geo partner
    @return: 200: flask/response object.
    @raise 400: Failed. Bad post data.
    @raise 404: Failed. Data duplicated.
    @raise 500: Failed. Server Error.
    """
    logger = logger_config.get_logger()
    logger.info(f'search geo partner - {lnt}, {lat}')
    return jsonify({'lnt': lnt, 'lat': lat}), 200


@REQUEST_API.route('/partner/<id>', methods=['GET'])
def partner_search(id):
    """Create partner
    @return: 200: flask/response object.
    @raise 404: Failed. Data duplicated.
    @raise 500: Failed. Server Error.
    """
    logger = logger_config.get_logger()
    logger.info(f'--- search partner - {id} ---')

    business = Partner(id)
    business.search()
    # return register create
    if business.register:
        logger.info(f'search success')
        return jsonify(business.register), 200
    # return error duplicated
    if business.conflited:
        logger.error(
            f'search error - 404 - not found {id}')
        return jsonify({'error': 'not found'}), 404
    # return error server
    logger.error(f'search error - 500 {id}')
    return jsonify({'error': 'server error'}), 500


@REQUEST_API.route('/partner', methods=['POST'])
def partner_create():
    """Create partner
    with application/json mimetype.
    @return: 201: flask/response object.
    @raise 400: Failed. Bad post data.
    @raise 409: Failed. Data duplicated.
    @raise 500: Failed. Server Error.
    """
    logger = logger_config.get_logger()
    data = request.get_json(force=True)
    logger.info(f'--- submit create partner ---')

    business = Partner(data)
    business.create()
    # return register create
    if business.register:
        logger.info(f'create success - {str(data["tradingName"])}')
        return jsonify(business.register), 201
    # return error payload
    if business.error:
        logger.error(f'create error - 400 - ', business.error)
        return jsonify({'error': business.error}), 400
    # return error duplicated
    if business.conflited:
        logger.error(
            f'create error - 409 - duplicate register {str(data["tradingName"])}')
        return jsonify({'error': f'duplicate register {str(data["tradingName"])}'}), 409
    # return error server
    logger.error(f'create error - 500')
    return jsonify({'error': 'server error'}), 500
