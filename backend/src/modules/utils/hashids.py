from hashids import Hashids

# Init Hashids with custom cryptographic configuration
hashids = Hashids(
    salt="change for production",
    min_length=10,
    alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_'
)


SEPARATION_CHAR = '-'


def to_public_id(model, db_id):
    model_name = model.__name__
    hashid = hashids.encode(db_id)
    return model_name + SEPARATION_CHAR + hashid


def to_db_id(public_id):
    encoded_id = public_id.split(SEPARATION_CHAR)[1]
    try:
        db_id = hashids.decode(encoded_id)[0]
    except:
        db_id = None
    return db_id