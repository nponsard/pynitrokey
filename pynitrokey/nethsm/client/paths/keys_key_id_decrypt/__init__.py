# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from pynitrokey.nethsm.client.apis.paths.keys_key_id_decrypt import KeysKeyIDDecrypt

path = "/keys/{KeyID}/decrypt"