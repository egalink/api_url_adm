import nanoid
from datetime import datetime, timezone
from App.Database.MongoSchema import MongoSchema

class Url (MongoSchema):

    _db_collection='urlshortener.urls'

    def __init__ (self):
        super().__init__(self)

    def save_url (self, user_id, url, expires_at=None, active=True):

        # expiration date must be on UTC to calculate
        # expiration from any local time:
        if (expires_at is not None):
            expires_at = datetime.fromtimestamp(expires_at.timestamp(), tz=timezone.utc)

        uid = nanoid.generate(size=9)
        _id = self.insert_one({
            'url': url,
            'uid': uid,
            'clicks': 0,
            'active': active,
            'user_id': user_id,
            'expires_at': expires_at,
            'created_at': datetime.now(), # this is only a representative date.
        }).inserted_id

        return uid
