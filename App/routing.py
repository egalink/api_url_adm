from flask import jsonify
from App.Controllers.UrlGenerator import UrlGeneratorLS, UrlGeneratorWP

def resources (api):
    api.add_resource(UrlGeneratorLS, '/api/url')
    api.add_resource(UrlGeneratorWP, '/api/url/<string:uid>')

def routing (app, api):

    @app.route('/')
    def say_hello():
        return { 'description': 'Una simple api para recortar tus URL\'s de la WEB.' }

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({ 'error': 'Not found.' }), 404

    resources(api)
