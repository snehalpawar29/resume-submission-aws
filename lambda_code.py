import json
import boto3
import uuid
import base64
from datetime import datetime

# AWS clients
s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
ses = boto3.client('ses', region_name='ap-south-1')

# CONFIG
BUCKET = "YOUR_RESUME_BUCKET"
TABLE = "ResumeSubmissions"
EMAIL_TO = "YOUR_VERIFIED_EMAIL"
EMAIL_FROM = "YOUR_VERIFIED_EMAIL"


def lambda_handler(event, context):
    try:
        body = json.loads(event["body"])

        name = body.get("name")
        email = body.get("email")
        filename = body.get("filename")
        file_base64 = body.get("file")

        # generate unique id
        submission_id = str(uuid.uuid4())
        key = submission_id + "-" + filename

        # decode file
        file_bytes = base64.b64decode(file_base64)

        # upload to S3
        s3.put_object(
            Bucket=BUCKET,
            Key=key,
            Body=file_bytes
        )

        # save metadata to DynamoDB
        table = dynamodb.Table(TABLE)

        table.put_item(
            Item={
                "submissionId": submission_id,
                "name": name,
                "email": email,
                "file": key,
                "timestamp": datetime.utcnow().isoformat()
            }
        )

        # send email notification
        ses.send_email(
            Source=EMAIL_FROM,
            Destination={"ToAddresses": [EMAIL_TO]},
            Message={
                "Subject": {
                    "Data": "New Resume Submitted"
                },
                "Body": {
                    "Text": {
                        "Data": f"""
New resume submitted

Name: {name}
Email: {email}
File: {key}
"""
                    }
                }
            }
        )

        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "*",
                "Access-Control-Allow-Methods": "*"
            },
            "body": json.dumps({
                "message": "resume uploaded",
                "file": key
            })
        }

    except Exception as e:
        print("ERROR:", str(e))
        return {
            "statusCode": 500,
            "headers": {
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({
                "error": str(e)
            })
        }