from datetime import datetime
from nanoid import generate
from App.Database.MongoSchema import MongoSchema

class Url (MongoSchema):

    _db_collection='urlshortener.urls'

    def __init__ (self):
        super().__init__(self)

    def save_url (self, url, uid=generate(size=12)):
        _id = self.insert_one({
            'url': url,
            'uid': uid,
            'created_at': datetime.utcnow()
        }).inserted_id

        return uid
