from healthcheck import HealthCheck as HealthChecker
from App.Database.MongoDb import MongoDb

class HealthCheck:

    def __init__ (self, app):
        HealthChecker(app, "/health").add_check(self.status)
 
    def check_db_connection (self):
        database_connection = True
        try:
            MongoDb().get_client().list_database_names()
        except Exception as e:
            database_connection = False

        return database_connection

    def status (self):
        # check service health
        healthy = True

        database_connection = self.check_db_connection()
        if database_connection is False: healthy = False

        return healthy, {
            "healthy": healthy,
            "database_connection": database_connection
        }
