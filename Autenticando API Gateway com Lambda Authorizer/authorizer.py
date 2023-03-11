import botocore
import boto3

def lambda_handler(event, context):
    ssm = boto3.client('ssm')
    auth_header = event.get('headers').get('Authorization')
    policy = {}
    
    if auth_header:
    
        try:
            policy = {
                'principalId': 'user',
                'policyDocument': {
                    'Version': '2012-10-17',
                    'Statement': [
                        {
                            'Action': 'execute-api:Invoke',
                            'Effect': 'Deny',
                            'Resource': '*'
                        }
                    ]
                }
            }

            response = ssm.get_parameter(Name=auth_header)
            if 'Parameter' in response:           
                policy['policyDocument']['Statement'][0]['Effect'] = 'Allow'
        except botocore.exceptions.ClientError as error:
            policy['policyDocument']['Statement'][0]['Effect'] = 'Deny'
           
        return policy