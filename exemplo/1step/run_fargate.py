import boto3

ecs = boto3.client('ecs')

cluster_name = ''
subnet_id = ''
sg_id = ''  
bucket_name = ''
task_definition = '' 

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
                    'name': 'p',
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
        startedBy='',
        taskDefinition=task_definition
    )
