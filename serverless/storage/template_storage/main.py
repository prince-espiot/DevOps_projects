import os
import io # To read from saved file
from google.cloud import storage, vision
import functions_framework
# Add any imports that you may need, but make sure to update requirements.txt

@functions_framework.cloud_event
def image_to_text_storage(cloud_event):
    # TODO: Add logic here
    storage_client = storage.Client()

    data = cloud_event.data

    name = data["name"]
    print('Name without txt: ',name)
    if name.endswith('.jpg'):
        bucket_name = data["bucket"]
        print('bucket_name:',bucket_name)
        print('name:',name)
        print('name_out_if:',name)
        bucket = storage_client.get_bucket(bucket_name)
        print('bucket:',bucket)
        blob = bucket.blob(name)
        blob.download_to_filename('/tmp/'+ name)
    
        client = vision.ImageAnnotatorClient()
        with io.open('/tmp/'+name, 'rb') as image_file:
            content = image_file.read()
            print('content:',content)
        image = vision.Image(content=content)
        response = client.text_detection(image=image)
        texts = response.text_annotations
        print('Texts:',texts)

        fileName = os.path.splitext(name)[0]

        print('filename:',fileName)
        
        write_file(bucket_name,fileName,texts)
    
    return

def write_file(bucket_name,blob_txt,texts):
    client = storage.Client()
    bucket = client.get_bucket(bucket_name)
    blob = bucket.blob(blob_txt+'.txt')
    with blob.open(mode='w') as f:
        for line in texts: 
            f.write(line.description)