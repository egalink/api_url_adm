import re
import validators
from bson.objectid import ObjectId
from urllib.parse import urlparse

def validate_url (value):
    regexp = re.compile("^((http|https)://)[-a-zA-Z0-9@:%._\\+~#?&//=]{2,256}\\.[a-z]{2,6}\\b([-a-zA-Z0-9@:%._\\+~#?&//=]*)$")
    return regexp.match(value) is not None and validators.url(value) is True

def objectid2str (object_id):
    if isinstance(object_id, ObjectId):
        return str(object_id)
    else:
        raise ValueError('Input is not a valid ObjectId')

def str2objectid (object_id_string):
    if isinstance(object_id_string, str) and ObjectId.is_valid(object_id_string):
        return ObjectId(object_id_string)
    else:
        raise ValueError('Input is not a valid string representation of an ObjectId')
        
def get_domain_name_from_url (url_string):
    if validate_url(url_string) is False:
        raise ValueError("The provided string is not a valid URL.")

    return urlparse(url_string).netloc