from flask import jsonify
from flask_jwt_extended import create_access_token
from App.Controllers.UrlGenerator import UrlGeneratorLS, UrlGeneratorWP

def resources (api):
    api.add_resource(UrlGeneratorLS, '/api/url')
    api.add_resource(UrlGeneratorWP, '/api/url/<string:uid>')

def routing (app, api):

    @app.route('/')
    def say_hello():
        access_token = create_access_token(identity="cfeaeeabcf746207d81aaaa2a2832ead06f340686a4c005fdf17e22c8ca1b020")
        return jsonify(access_token=access_token)
        return { 'success': 'Una simple api para recortar tus URL\'s de la WEB.' }, 200

    @app.errorhandler(404)
    def not_found_error(error):
        return jsonify({ 'failure': 'not found', 'message': error.description }), 404

    #@app.errorhandler(500)
    #def internal_server_error(error):
    #    return jsonify({'error': 'internal server error', 'message': error.description}), 500

    @app.errorhandler(Exception)
    def handle_exception(e):
        response = jsonify({'failure': e.__class__.__name__, 'message': str(e)})
        response.status_code = 500
        return response
    
    resources(api)
