from flask import request, jsonify, current_app as app
from flask_restful import Resource, reqparse, inputs
from flask_jwt_extended import jwt_required, get_jwt_identity
from App.Services.StringHelpers import validate_url
from App.Schemas.Url import Url
from App.Schemas.User import User
from App.Services.StringHelpers import str2objectid
from datetime import datetime, timedelta

class UrlResponseGenerator:

    def __init__ (self, domain, obj) -> None:

        expires_in = None
        expires_at = None

        if obj['expires_at'] is not None:
            expiration = (obj['expires_at'] - datetime.utcnow()).total_seconds()
            expires_at = (datetime.now() + timedelta(seconds=expiration)).strftime("%Y-%m-%d %H:%M:%S")
            expires_in = int(expiration)

        self._document = {
            'uid': obj['uid'],
            'url': obj['url'],
            'clicks': obj['clicks'],
            'active': bool(obj['active']),
            'shortened_url': f"{domain}/u/{obj['uid']}",
            'expires_at': expires_at,
            'expires_in': expires_in,
            'created_at': obj['created_at'].strftime("%Y-%m-%d %H:%M:%S"),
        }

    def parse (self):
        return self._document


class UrlGeneratorLS (Resource):

    def __init__ (self) -> None:
        super().__init__()
        self._domain_name = request.url_root.strip("/")
    
    @jwt_required()
    def get (self):

        user_id = get_jwt_identity()
        profile = User().find_one({ '_id': str2objectid(user_id) })

        if (profile is None):
            return {
                "error": "No se encontró el usuario solicitado.",
            }, 404

        urllist = []

        for url in Url().find_many({ 'user_id': profile['_id'] }):
            urllist.append(UrlResponseGenerator(self._domain_name, url).parse())

        #app.logger.info('Requesting all registered urls.')
        return jsonify(urllist)

    @jwt_required()
    def post (self):

        user_id = get_jwt_identity()
        profile = User().find_one({ '_id': str2objectid(user_id) })

        if (profile is None):
            return {
                "error": "No se encontró el usuario solicitado.",
            }, 404

        parser = reqparse.RequestParser()
        parser.add_argument('url', required=True, type=inputs.url, help="Por favor, proporciona una URL válida.")
        parser.add_argument('expiration', required=False, type=inputs.datetime_from_iso8601, help="Por favor, proporciona una fecha de expiración válida.")
        payload = parser.parse_args()

        # validate if the provided url is a correct one:
        if validate_url(payload.url) is False:
            return {
                "error": "La URL no es válida.",
            }, 400

        uid = Url().save_url(profile['_id'], payload.url, payload.expiration)

        return {
            "uid": f"{uid}"
        }, 201


class UrlGeneratorWP (Resource):

    def __init__ (self) -> None:
        super().__init__()
        self._domain_name = request.url_root.strip("/")

    @jwt_required()
    def get (self, uid):

        user_id = get_jwt_identity()
        profile = User().find_one({ '_id': str2objectid(user_id) })

        if (profile is None):
            return {
                "error": "No se encontró el usuario solicitado.",
            }, 404

        url = Url().find_one({ 'uid': uid, 'user_id': profile['_id'] })
        
        if (url is None):
            return {
                "error": "No se encontró el usuario solicitado.",
            }, 404

        return UrlResponseGenerator(self._domain_name, url).parse(), 200

    @jwt_required()
    def delete (self, uid):

        user_id = get_jwt_identity()
        profile = User().find_one({ '_id': str2objectid(user_id) })

        if (profile is None):
            return {
                "error": "No se encontró el usuario solicitado.",
            }, 404

        try:
            
            Url().delete_one({
                'uid'       : uid,
                'user_id'   : profile['_id']
            })

        except Exception as e:
            return {
                'error': str(e)
            }, 500

        return { 'uid': uid }, 200