"""The Endpoints to manage the Partner"""
from business.partner import Partner
from controller.partner import PartnerCreate
from flask import jsonify, request, Blueprint, Response
from flask_cors import CORS, cross_origin
import os
import logger_config
import ujson


REQUEST_API = Blueprint('partner', __name__)


def get_blueprint():
    """Return the blueprint for the main app module"""
    return REQUEST_API


@REQUEST_API.route('/search-partner/<lnt>/<lat>', methods=['GET'])
def partner_geo_search(lnt, lat):
    """search geo partner
    @param lnt : string
    @param lat : string
    @return: 200: flask/response object.
    @raise 404: Failed. Data not found.
    @raise 400: Failed. Bad post data.
    @raise 500: Failed. Server Error.
    """
    try:
        logger = logger_config.get_logger()
        logger.info(f'search partner ({lnt}, {lat})')
        business = Partner()
        business.geo_search(lnt, lat)

        # return error not found
        if business.conflited:
            logger.error(
                f'search partner - error - 404 - not found')
            return jsonify({'error': 'not found'}), 404

        # return error not found
        if business.error:
            logger.error(
                f'get partner - error - 400 - {id}')
            return jsonify(business.error), 400

        # return register create
        logger.info(
            f'search partner - success - 200')
        logger.info(
            f'search partner - totalizers - {len(business.register)}')
        return jsonify(business.register), 200

    except Exception as e:
        # return error server
        logger.error(f'search partner - error - 500 - {str(e)}')
        return jsonify({'error': {str(e)}}), 500


@REQUEST_API.route('/partner/<id>', methods=['GET'])
def partner_search(id):
    """search partner
    @param id : string
    @return: 200: flask/response object.
    @raise 404: Failed. Data not found.
    @raise 400: Failed. Bad post data.
    @raise 500: Failed. Server Error.
    """
    try:
        logger = logger_config.get_logger()
        logger.info(f'--- get partner - {id} ---')
        # TODO validar id
        business = Partner(id)
        business.search()

        # return error not found
        if business.conflited:
            logger.error(
                f'get partner - error - 404 - not found {id}')
            return jsonify({'error': 'not found'}), 404

        # return error not found
        if business.error:
            logger.error(
                f'get partner - error - 400 - {id}')
            return jsonify(business.error), 400

        # return register create
        logger.info(f'get partner - success - 200')
        return jsonify(business.register), 200

    except Exception as e:
        # return error server
        logger.error(f'get partner - error - 500 {id}, {str(e)}')
        return jsonify({'error': 'server error'}), 500


@REQUEST_API.route('/partner/', methods=['POST'])
def partner_create():
    """Create partner
    @param data : json
    with application/json mimetype.
    @return: 202: flask/response object.
    @raise 400: Failed. Bad post data.
    @raise 500: Failed. Server Error.
    """
    try:
        logger = logger_config.get_logger()
        data = request.get_json(force=True)

        # return error not found
        if 'pdvs' not in data:
            logger.error(f'create partner - error - 404 - pdvs not found')
            return jsonify({'error': 'pvds - not found'}), 404

        logger.info(f'--- create partner ---')
        response = PartnerCreate(data['pdvs'])
        response.process()

        # return error process
        if response.error:
            logger.error(
                f'create partner - error - 400 - {str(response.error)}')
            return jsonify({'error': response.error}), 400

        # start process create
        logger.info(
            f'create partner - Accepted - 202')
        logger.info(
            f'create partner - totalizers - {str(response.totalizers)}')
        return jsonify({'totalizers': response.totalizers, 'pdvs': response.register}), 202

    except Exception as e:
        # return error server
        logger.error(f'create partner - error - 500, {str(e)}')
        return jsonify({'error': 'server error'}), 500
