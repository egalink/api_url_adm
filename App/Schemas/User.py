from App.Database.MongoSchema import MongoSchema

class User (MongoSchema):

    _db_collection='urlshortener.users'

    def __init__ (self):
        super().__init__(self)
