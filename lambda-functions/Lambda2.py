### CLASSIFICATION LAMBDA FUNCTION

import json
import sagemaker
import base64
import boto3
from sagemaker.serializers import IdentitySerializer

# Fill this in with the name of your deployed model
## TODO: fill in
ENDPOINT = "image-classification-2023-09-18-00-20-01-991" 
runtime = boto3.client('runtime.sagemaker')

def lambda_handler(event, context):
    
    key = event['body']['s3_key']
    bucket = event['body']['s3_bucket'] 
    # Decode the image data
    ## TODO: fill in
    image = base64.b64decode(event['body']['image_data'])

    # Instantiate a Predictor

    # inferences = ## TODO: fill in
    response = runtime.invoke_endpoint(EndpointName=ENDPOINT, ContentType="image/png", Body=image)
                                        
    
    # We return the data back to the Step Function    
    event['body']["inferences"] = json.loads(response["Body"].read().decode('utf-8'))
    
    return {
        'statusCode': 200,
        'body': {
            "image_data": event['body']['image_data'],
            "s3_bucket": bucket,
            "s3_key": key,
            "inferences": event['body']["inferences"]
        }
    }