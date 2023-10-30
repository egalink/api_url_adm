from healthcheck import HealthCheck as HealthChecker

class HealthCheck:

    def __init__ (self, app):
        HealthChecker(app, "/health").add_check(self.status)

    def status (self):
        # check service health
        return True, { 'healthy': True }
