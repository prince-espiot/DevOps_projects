import os
from google.cloud import storage
import functions_framework
import json
from flask import jsonify

# Add any imports that you may need, but make sure to update requirements.txt

@functions_framework.http
def create_text_file_http(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        Return the fileName in the body of the response.
        Return a HTTP status code of 200.
    Note:
        For more information on how Flask integrates with Cloud
        Functions, see the `Writing HTTP functions` page.
        <https://cloud.google.com/functions/docs/writing/http#http_frameworks>
    """
    
    # TODO: Add logic here

    request_json = request.get_json()
    print('json_data:',request_json)

    #request_args = request.args
    
    print("bucket_enivor:",os.environ['BUCKET_ENV_VAR'])

    bucket_name = os.environ['BUCKET_ENV_VAR']

    client = storage.Client()

    bucket = client.get_bucket(bucket_name)
    print('bucket_afc:', bucket) #checkpoint

   
    name = request_json['fileName']
    print("name:",name)
    blob = bucket.blob(name)
    print("blob:",blob)
    
    
    content = request_json['fileContent']
    #contents = blob.download_as_string()
    output = jsonify({'fileName':content})
    print('output_data:',output)
    contents_data = json.dumps(content)

    with blob.open("w") as f:
        f.write(content)

    print("content:",contents_data)

    status_code = 200
    return output, status_code
    
#gcloud functions deploy echo --gen2 --source=. --runtime=python310 --trigger-http --entry-point=echo --region=europe-west1    