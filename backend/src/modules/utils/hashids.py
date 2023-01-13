from hashids import Hashids

# Init Hashids with custom cryptographic configuration
hashids = Hashids(
    salt="change for production",
    min_length=10,
    alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_'
)


SEPARATION_CHAR = '-'


def to_public_id(model, db_id):
    model_name = model
    full_id = model_name + SEPARATION_CHAR + str(db_id)
    hashid = hashids.encode(full_id)
    return model_name + SEPARATION_CHAR + hashid


def to_db_id(model, public_id):
    encoded_id = public_id.split(SEPARATION_CHAR)[1]
    decoded_id = hashids.decode(encoded_id)
    db_id = decoded_id.split(SEPARATION_CHAR)[1]
    return db_id