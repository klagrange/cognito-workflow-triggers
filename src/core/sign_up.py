
def sign_up(client_cognito_idp, app_client_id, email, password):
    client_cognito_idp.sign_up(
        ClientId=app_client_id,
        Username=email,
        Password=password,
    )

if __name__ == "__main__":
    import boto3
    CLIENT_COGNITO_IDP = boto3.client('cognito-idp')
    sign_up(CLIENT_COGNITO_IDP, '1qk837pg1jlo2ct4j5olpe3vf1', 'keith@bambu.co', 'Bamb@1234!')