import boto3
from botocore.exceptions import ClientError

def scan_and_fix_s3():
    # Connect to AWS S3
    s3 = boto3.client('s3')
    
    print("🤖 Scanning AWS S3 Buckets for security mistakes...\n")
    
    # Get a list of all buckets in your AWS account
    buckets = s3.list_buckets()['Buckets']
    
    for bucket in buckets:
        bucket_name = bucket['Name']
        
        try:
            # Ask AWS for the public access settings of this bucket
            pab = s3.get_public_access_block(Bucket=bucket_name)
            config = pab['PublicAccessBlockConfiguration']
            
            # If ANY of the 4 public blocks are turned OFF, it's vulnerable!
            if (config['BlockPublicAcls'] == False or 
                config['IgnorePublicAcls'] == False or 
                config['BlockPublicPolicy'] == False or 
                config['RestrictPublicBuckets'] == False):
                
                print(f"🚨 ALERT: Bucket '{bucket_name}' is VULNERABLE! Public access is allowed.")
                print(f"🛠️ FIXING: Automatically turning on Block Public Access...\n")
                
                # Send the command to fix the bucket automatically!
                s3.put_public_access_block(
                    Bucket=bucket_name,
                    PublicAccessBlockConfiguration={
                        'BlockPublicAcls': True,
                        'IgnorePublicAcls': True,
                        'BlockPublicPolicy': True,
                        'RestrictPublicBuckets': True
                    }
                )
                print(f"✅ SUCCESS: Bucket '{bucket_name}' is now SECURE!\n")
                
            else:
                print(f"✅ SAFE: Bucket '{bucket_name}' is properly secured.\n")
                
        except ClientError as e:
            # If a bucket has no settings at all, AWS treats it as public
            if e.response['Error']['Code'] == 'NoSuchPublicAccessBlockConfiguration':
                print(f"🚨 ALERT: Bucket '{bucket_name}' has NO Public Access Block (Vulnerable)!")
                print(f"🛠️ FIXING: Automatically turning on Block Public Access...\n")
                
                s3.put_public_access_block(
                    Bucket=bucket_name,
                    PublicAccessBlockConfiguration={
                        'BlockPublicAcls': True,
                        'IgnorePublicAcls': True,
                        'BlockPublicPolicy': True,
                        'RestrictPublicBuckets': True
                    }
                )
                print(f"✅ SUCCESS: Bucket '{bucket_name}' is now SECURE!\n")

# Run the robot!
scan_and_fix_s3()