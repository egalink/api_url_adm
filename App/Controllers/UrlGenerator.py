from flask import request, jsonify
from flask_restful import Resource, reqparse
from App.Services.StringHelpers import validate_url
from App.Schemas.Url import Url

class UrlGeneratorLS (Resource):

    def __init__ (self) -> None:
        super().__init__()
        self._domain_name = request.url_root.strip("/")

    def get (self):
        data_list = []
        for item in Url().find_many():
            data_list.append({
                'uid': item['uid'],
                'url': item['url'],
                #'created_at': item['created_at'].strftime("%Y-%m-%d %H:%M:%S")
            })

        return jsonify(data_list)

    def post (self):
        parser = reqparse.RequestParser()
        parser.add_argument('url', required=True, type=str, help="Por favor, proporciona una URL válida.")
        payload = parser.parse_args()

        # validate if the url param is present in payload:
        if 'url' in payload and len(payload.url) < 8:
            return { 'failure': 'Proporciona una URL.' }, 400

        # validate if the provided url is a correct one:
        if validate_url(payload.url) is False:
            return { 'failure': 'La URL no es válida.' }, 400

        _id = Url().save_url(payload.url)

        return { 'success': f'{_id}' }, 201
    
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