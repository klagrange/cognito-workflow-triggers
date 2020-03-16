
def confirm_sign_up(client_cognito_idp, app_client_id, email, code):
    client_cognito_idp.confirm_sign_up(
        ClientId=app_client_id,
        Username=email,
        ConfirmationCode=code,
    )
