import jwt
import re

def verify_token(client_cognito_idp, app_client_id, access_token):
    is_valid, email = token_is_valid(client_cognito_idp, app_client_id, access_token)
    if not is_valid:
        raise Exception({
            "statusCode": 403,
            "type": "InvalidToken",
            "message": "Invalid Token {0}".format(access_token)
        })
    return email

def token_is_valid(client_cognito_idp, app_client_id, access_token):
    matched = re.match("^[A-Za-z0-9-_=]+\.[A-Za-z0-9-_=]+\.?[A-Za-z0-9-_.+/=]*$", access_token)
    if not matched:
        return False, None
    decoded_body = jwt.decode(access_token, verify=False)
    if decoded_body["client_id"] != app_client_id:
        return False, None
    email = _get_email(client_cognito_idp, access_token)
    return True, email

def _get_email(client_cognito_idp, access_token):
    get_user_res = client_cognito_idp.get_user(
        AccessToken=access_token,
    )
    return get_user_res["UserAttributes"][2]["Value"]
