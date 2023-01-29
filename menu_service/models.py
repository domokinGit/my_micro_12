import mongoengine


class Product(mongoengine.Document):
    meta = {
        'db_alias': 'mydb',
        'collection': 'menu',
    }

    product_id = mongoengine.UUIDField(primary_key=True)
    product = mongoengine.StringField(max_length=40, required=True)
    price = mongoengine.IntField(max_length=30, required=True)
