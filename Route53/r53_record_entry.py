import sys
import boto3

session = boto3.Session(profile_name='route53role')
r53client = session.client('route53')

HostedZid = 'ZXXXXXXXXX'
HOSTFQDN = str(sys.argv[1])
PRIVATEIP = str(sys.argv[2])

response = r53client.change_resource_record_sets(
    HostedZoneId = HostedZid,
    ChangeBatch={
        'Comment': 'ASG-SERVERS',
        'Changes': [{
                'Action': 'UPSERT',
                'ResourceRecordSet': {
                    'Name': HOSTFQDN,
                    'Type': 'A',
                    'TTL': 60,
                    'ResourceRecords': [{'Value': PRIVATEIP}]
                    }
            },]
    }
)
