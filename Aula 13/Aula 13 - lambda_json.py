import json

def lambda_handler(event, context):
    # TODO implement
    
    response = {
        "store" : "PetStore",
        "location" : "Rua dos Pets",
        "zipCode" : "11111111",
        "city" : "Miami",
        "state" : "Florida",
        "phone" : "123456789"
    }
    
    return {
      "statusCode": 200,
      "body": json.dumps(response)
    }