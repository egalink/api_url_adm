from App.Database.MongoDb import MongoDb

class MongoSchema:

    mongo=None

    '''
    define the IoC container for MongoDb object instance.
    use: schema.__class__.__name__ to know the
    main class name.
    '''
    def __init__ (self, schema):
        [
            db,
            collection
        ] = schema._db_collection.split('.')

        self.mongo = MongoDb().db(db).on(collection)

    '''
    # Insert a document
    schema.insert_one({'name': 'John', 'age': 30})
    '''
    def insert_one (self, data):
        return self.mongo.insert_one(data)

    '''
    # Find a document
    print(schema.find_one({'name': 'John'}))
    '''
    def find_one (self, filter={}):
        return self.mongo.find_one(filter)

    '''
    # Find multiple documents
    for user in schema.find_many({'age': {'$gt': 25}}):
        print(user)
    '''
    def find_many (self, filter={}, skip=0, limit=0):
        if limit > 0:
            return self.mongo.find(filter).skip(skip).limit(limit)
        else:
            return self.mongo.find(filter).skip(skip)

    '''
    # Update a document
    schema.update_one({'name': 'John'}, {'$set': {'age': 31}})
    '''
    def update_one (self, filter, update):
        return self.mongo.update_one(filter, update)

    '''
    # Delete a document
    schema.delete_one({'name': 'John'})
    '''
    def delete_one (self, filter):
        return self.mongo.delete_one(filter)
