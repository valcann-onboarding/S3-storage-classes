# Native
import csv
from os import system, environ

BUCKET_NAME = environ.get('BUCKET_NAME')
OBJECT_KEY = ''

def change_object_storage_class_with_copy(storage_class='STANDARD_IA'):
    global BUCKET_NAME, OBJECT_KEY
    run = f"aws s3 cp " + f"s3://{BUCKET_NAME}/{OBJECT_KEY} " + \
          f"s3://{BUCKET_NAME}/{OBJECT_KEY} " + \
          f"--storage-class {storage_class} " + "> /dev/null"
    system(run)
    print('ccsc> ' + identificador_documento)  # ccsc - copy and change storage class

if __name__ == '__main__':

    path = environ.get('SUBLOT_TAG')
    
    with open(path, 'r') as file:
        reader = csv.reader(file, delimiter = '\t')
        for row in reader:
            
            identificador_documento = row[0]
            OBJECT_KEY = identificador_documento
            change_object_storage_class_with_copy()

    print('success> ' + path)