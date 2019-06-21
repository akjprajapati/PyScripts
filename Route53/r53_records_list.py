import boto3
session = boto3.Session(profile_name='route53role')
r53client = session.client('route53')
r53list= r53client.list_resource_record_sets(HostedZoneId='ZXXXXXX')

for i in r53list['ResourceRecordSets']:
        print(i['Name'])


###List 'A' records only.
#for i in r53list['ResourceRecordSets']:
#  if i['Type'] == 'A':
#    print(i['Name'])


###List 'CNAME' records only.
#for i in r53list['ResourceRecordSets']:
#  if i['Type'] == 'CNAME':
#    print(i['Name'])
