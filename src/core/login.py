
def login(client_cognito_idp, app_client_id, email, password):
    initiate_auth_res = client_cognito_idp.initiate_auth(
        AuthFlow="USER_PASSWORD_AUTH",
        AuthParameters={
            'USERNAME': email,
            'PASSWORD': password
        },
        ClientId=app_client_id,
    )
    return initiate_auth_res["AuthenticationResult"]["AccessToken"]