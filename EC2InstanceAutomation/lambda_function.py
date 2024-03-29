import boto3

def lambda_handler(event, context):
    
    # create EC2 client
    ec2 = boto3.resource('ec2')
    
    for instance in ec2.instances.all():
        state = instance.state['Name']
        if state == 'stopped':
            try:
                instance.start()
            except:
                print("Some Error")
