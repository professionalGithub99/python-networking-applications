import csv
import requests
import sys
import requests_aws4auth as aws4Auth
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom

#Using File open to create access keys for Security
f=open('new_user_credentials.csv',newline='')
f_reader=csv.DictReader(f,delimiter=',')
f_dict=(list(f_reader))
access_id=f_dict[0]['Access key ID']
access_key=f_dict[0]['Secret access key']
region='us-east-1'
name_space='http://s3.amazonaws.com/doc/2006-03-01/'

#This this is the authorizationmethod used for http requests
#https://pypi.org/project/requests-aws4auth/
auth=aws4Auth.AWS4Auth(access_id,access_key,region,'s3')
def create_bucket(bucket_name):
    #The logic is create bucket name refering to this syntax
    #https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucket.html
    XML = ET.Element('CreateBucketConfiguration')
    endpoint= 'http://{}.s3.{}.amazonaws.com'.format(bucket_name,region)
    XML.attrib['xmlns'] =name_space
    location = ET.SubElement(XML, 'LocationConstraint')
    print(type(XML),'aaaaa')
    location.text ='us-east-2'
    response=requests.put(endpoint,data=location,auth=auth)
    print(response.content)
    print(response.headers)
    print(response.status_code)
    print(location)
    print(endpoint)
    print(auth.region)
def put_object(key_name,bucket_name):
    endpoint='http://{}.s3.{}.amazonaws.com/{}'.format(bucket_name,region,key_name)
    f=open('test-image.jpeg','rb').read()
    print(endpoint)
    requests.put(endpoint,data=f,auth=auth,headers={'Content-Type': 'image/jpeg','x-amz-acl':'private'})
def put_object_pub_read(key_name,bucket_name):
    #acl documentation for header: https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#specifying-grantee
    endpoint='http://{}.s3.{}.amazonaws.com/{}'.format(bucket_name,region,key_name)
    f=open('test-image.jpeg','rb').read()
    print(endpoint)
    res=requests.put(endpoint,data=f,auth=auth,headers={'Content-Type': 'image/jpeg','x-amz-acl':'public-read'})
    print(res.status_code)
    print(res.headers)
    print(res.content)
def get_object(key_name,bucket_name):
    #acl documentation for header: https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#specifying-grantee
    endpoint='http://{}.s3.{}.amazonaws.com/{}'.format(bucket_name,region,key_name)
    ##f=open('priv-test.jpeg','rb').read()
    res=requests.get(endpoint,auth=auth)
    print(auth)
    print(res.status_code)
    print(res.headers)
    print(res.content)
    print(res.text)

def get_object_with_session(key_name,bucket_name):
    endpoint='http://{}.s3.{}.amazonaws.com/{}'.format(bucket_name,region,key_name)
    req=requests.Request(method='Get',url=endpoint,headers={'Content-Type':'image/jpeg'})
    r=req.prepare()
    session=requests.Session()
    s=session.send(r)
    print(s.status_code)
    print(s.headers)
    print(r.path_url)
    print(r.headers)
    print(r.url)
if __name__ == '__main__':
    cmd,*args=sys.argv[1:]
    globals()[cmd](*args)
