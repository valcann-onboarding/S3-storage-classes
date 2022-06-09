# Native
import csv
from os import system, environ

BUCKET_NAME = environ.get('BUCKET_NAME')
OBJECT_KEY = ''

def restore_object(tier='Bulk'):
    global BUCKET_NAME, OBJECT_KEY
    run = f"aws s3api restore-object --bucket {BUCKET_NAME} " + \
          f"--key {OBJECT_KEY} " + \
          '--restore-request Days=7,GlacierJobParameters={"Tier"=' + f'"{tier}"' + '}'
    system(run)
    print('restore> ' + identificador_documento)

if __name__ == '__main__':

    path = environ.get('SUBLOT_TAG')
    
    with open(path, 'r') as file:
        reader = csv.reader(file, delimiter = '\t')
        for row in reader:
            
            identificador_documento = row[0]
            OBJECT_KEY = identificador_documento
            restore_object()

    print('success> ' + path)

