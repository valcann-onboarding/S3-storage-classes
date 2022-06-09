import boto3

ecs = boto3.client('ecs')

cluster_name = 'malves-s3-storage-classes'
subnet_id = 'subnet-025cb151539c1106c'
sg_id = 'sg-058b0c7719434b946' 
bucket_name = 'malves-s3-storage-classes'
task_definition = 'storage-classes-2step:1' 

for index in range(5):
    if index < 10:
        sublot_tag = f'x0{index}'
    else:
        sublot_tag = f'x{index}'

    run_task = ecs.run_task(
        cluster=cluster_name,
        count=1,
        launchType='FARGATE',
        networkConfiguration={
            'awsvpcConfiguration': {
                'subnets': [
                    subnet_id,
                ],
                'securityGroups': [
                    sg_id,
                ],
                'assignPublicIp': 'ENABLED'
            }
        },
        overrides={
            'containerOverrides': [
                {
                    'name': 's3-storage-classes-2step',
                    'environment': [
                        {
                            'name': 'BUCKET_NAME',
                            'value': bucket_name
                        },
                        {
                            'name': 'SUBLOT_TAG',
                            'value': sublot_tag
                        }
                    ]
                },
            ]
        },
        startedBy='VALCANN',
        taskDefinition=task_definition
    )
    
