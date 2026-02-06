#Boto3 library/python sdk to create, configure, manage AWS services.
import boto3

def get_s3_buckets():
    """
    This function returns list of S3 buckets from AWS
    """
   
    s3_client = boto3.client("s3")
    return s3_client.list_buckets()["Buckets"]
    

