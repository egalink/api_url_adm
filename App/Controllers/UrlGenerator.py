from flask import request, jsonify
from flask_restful import Resource, reqparse, inputs
from App.Services.StringHelpers import validate_url
from App.Schemas.Url import Url

class UrlGeneratorLS (Resource):

    def __init__ (self) -> None:
        super().__init__()
        self._domain_name = request.url_root.strip("/")

    def get (self):

        documents = []

        for doc in Url().find_many({}):
            documents.append({
                'uid': doc['uid'],
                'url': doc['url'],
                'clicks': doc['clicks'],
                'active': bool(doc['active']),
                'shortened_url': f"{self._domain_name}/u/{doc['uid']}",
                'expires_in': int(doc['expires_at'].total_seconds()) if doc['expires_at'] else 0,
                'created_at': doc['created_at'].strftime("%Y-%m-%d %H:%M:%S"),
            })

        return jsonify(documents)

    def post (self):
        parser = reqparse.RequestParser()
        parser.add_argument('url', required=True, type=inputs.url, help="Por favor, proporciona una URL válida.")
        payload = parser.parse_args()

        # validate if the provided url is a correct one:
        if validate_url(payload.url) is False:
            return { 'failure': 'La URL no es válida.' }, 400

        uid = Url().save_url(payload.url)

        return { 'success': f'{uid}' }, 201
    
class UrlGeneratorWP (Resource):

    def __init__ (self) -> None:
        super().__init__()
        self._domain_name = request.url_root.strip("/")

    def delete (self, uid):
        try:
            Url().delete_one({ 'uid': uid })
        except Exception as e:
            return { 'failure': str(e) }, 500

        return { 'success': uid }, 200