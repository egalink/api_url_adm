from flask import jsonify
from App.Controllers.UrlGenerator import UrlGeneratorLS, UrlGeneratorWP

def resources (api):
    api.add_resource(UrlGeneratorLS, '/api/url')
    api.add_resource(UrlGeneratorWP, '/api/url/<string:uid>')

def routing (app, api):

    @app.route('/')
    def say_hello():
        return jsonify({
            "info": "Una simple api para recortar tus URL\'s de la WEB."
        }), 200

    @app.errorhandler(404)
    def not_found_error(error):
        return jsonify({
            'error': error.description
        }), 404

    #@app.errorhandler(500)
    #def internal_server_error(error):
    #    return jsonify({'error': 'internal server error', 'message': error.description}), 500

    @app.errorhandler(Exception)
    def handle_exception(e):
        response = jsonify({
            "type": e.__class__.__name__,
            "error": str(e)
        })
        response.status_code = 500
        return response
    
    resources(api)
