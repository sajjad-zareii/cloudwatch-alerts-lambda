import boto3
import json

# Initialize AWS clients
sns_client = boto3.client('sns')
cloudwatch_logs_client = boto3.client('logs')

# Define log group name and SNS Topic ARN
LOG_GROUP_NAME = "/aws/lambda/my-lambda-log-group"  # Your CloudWatch log group
ALERT_TOPIC_ARN = "arn:aws:sns:us-west-2:123456789012:AlertTopic"  # Your SNS Topic ARN

def lambda_handler(event, context):
    # Get logs from CloudWatch
    logs = get_logs_from_cloudwatch()

    # Check logs for error messages
    for log in logs:
        if "ERROR" in log:  # Modify this condition to match specific log criteria
            send_alert(log)

def get_logs_from_cloudwatch():
    # Retrieve logs from CloudWatch
    response = cloudwatch_logs_client.filter_log_events(
        logGroupName=LOG_GROUP_NAME,
        limit=5  # Limit the number of log events to process
    )

    logs = []
    for event in response['events']:
        logs.append(event['message'])  # Add log messages to list
    return logs

def send_alert(log_message):
    # Send an alert via SNS
    message = {
        "subject": "New error in logs!",
        "body": f"An error was found in the logs: {log_message}"
    }
    
    sns_client.publish(
        TopicArn=ALERT_TOPIC_ARN,
        Message=json.dumps(message),
        Subject="System Error Alert"
    )
    print(f"Alert sent: {message}")