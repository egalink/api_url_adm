from flask import jsonify
from App.Controllers.UrlGenerator import UrlGeneratorLS, UrlGeneratorWP

def resources (api):
    api.add_resource(UrlGeneratorLS, '/api/url')
    api.add_resource(UrlGeneratorWP, '/api/url/<string:uid>')

def routing (app, api):

    @app.route('/')
    def say_hello():
        return { 'success': 'Una simple api para recortar tus URL\'s de la WEB.' }, 200

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({ 'failure': 'Not found.' }), 404

    resources(api)
