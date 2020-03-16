
def subscribe_plan(client_gateway, usage_plan_id, email):
    key_found, _ = key_is_part_of_usage_plan(client_gateway, usage_plan_id, email)
    if key_found:
        raise Exception({
            "type": "OneApiKeyPerEmail",
            "message": "ALREADY HAVE AN API KEY FOR THIS USAGE PLAN. LIMITED TO ONE PER EMAIL."
        })

    create_api_key_res = client_gateway.create_api_key(
        name=email,
        description='KEY CREATION WAS AUTOMATED. REMOVE WITH CAUTION!',
        enabled=True,
        generateDistinctId=True,
    )
    key = create_api_key_res["value"]
    client_gateway.create_usage_plan_key(
        usagePlanId=usage_plan_id,
        keyId=create_api_key_res["id"],
        keyType='API_KEY'
    )
    return key

def key_is_part_of_usage_plan(client_gateway, usage_plan_id, search_key):
    get_usage_plan_keys_res = client_gateway.get_usage_plan_keys(
        usagePlanId=usage_plan_id,
        nameQuery=search_key
    )
    keys = get_usage_plan_keys_res["items"]
    if not keys:
        return False, None
    for key in keys:
        if key["name"] == search_key:
            return True, None
    return False, None