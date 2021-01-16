import boto3
import botocore
session=boto3.Session(profile_name='default')
print(session)
dev_s3_client = session.resource('s3')
s3=boto3.resource('s3')
for bucket in dev_s3_client.buckets.all():
    print(bucket.name)

##s3.create_bucket(Bucket='botojldjlet',CreateBucketConfiguration={'LocationConstraint':'us-west-1'})
bucket=dev_s3_client.Bucket('py-bucket3')
f=open('test-image.jpeg','rb').read()
bucket.put_object(ACL='public-read',Key='public.jpeg',ContentType='image/jpeg',Body=f)
bucket.put_object(ACL='private',Key='private.jpeg',ContentType='image/jpeg',Body=f)
