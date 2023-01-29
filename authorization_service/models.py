import mongoengine


class User(mongoengine.Document):
    meta = {
        'db_alias': 'mydb',
        'collection': 'users',
    }

    user_id = mongoengine.UUIDField(primary_key=True)
    name = mongoengine.StringField(max_length=40, required=True)
    email = mongoengine.StringField(max_length=30, required=True)
    password = mongoengine.StringField(max_length=30, required=True)
