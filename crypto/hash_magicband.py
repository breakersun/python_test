
import hashlib
def generate_token(dsn):
    device_secret = "19863D1225BE18094C990BC2592AF9AF2A7D33C5FDCCE00CDCC1E9D78F7F77EB"
    hash_object = hashlib.sha256(bytes(dsn, 'utf-8') + bytes(device_secret, 'utf-8'))
    return hash_object.hexdigest()

if __name__ == "__main__":
    gadgetDeviceToken = generate_token("G0B0XG04903700E0")
    print(gadgetDeviceToken)