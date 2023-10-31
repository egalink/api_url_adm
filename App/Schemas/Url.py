import nanoid
from datetime import datetime
from App.Database.MongoSchema import MongoSchema

class Url (MongoSchema):

    _db_collection='urlshortener.urls'

    def __init__ (self):
        super().__init__(self)

    def save_url (self, url, expires_at=None, active=True):

        uid = nanoid.generate(size=9)
        _id = self.insert_one({
            'url': url,
            'uid': uid,
            'clicks': 0,
            'active': active,
            'expires_at': expires_at,
            'created_at': datetime.utcnow(),
        }).inserted_id

        return uid
