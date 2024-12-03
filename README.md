# cloudwatch-alerts-lambda
AWS SDK for Python to interact with AWS services like SNS and CloudWatch Logs.
# AWS Lambda Log Monitoring and Alert System

This AWS Lambda function monitors CloudWatch Logs for specific events, such as errors, and sends an alert via SNS (Simple Notification Service) when a matching event is found.

## Overview

The Lambda function performs the following tasks:
1. Monitors CloudWatch Logs for error messages or specific events.
2. Sends an alert to an SNS topic when a matching log message (e.g., "ERROR") is found.
3. Alerts can be configured to notify via email, SMS, or Slack.

## How It Works

- The Lambda function reads log events from a specified CloudWatch Logs group.
- It checks the logs for the word **"ERROR"** (this can be modified to any string).
- If an error is found, an SNS notification is sent, which can be configured to notify users via email, SMS, or other services like Slack.
- The Lambda function is triggered either by a scheduled CloudWatch Event or by specific CloudWatch Logs events.

## Setup

### 1. Create the Lambda Function

1. Go to the AWS Lambda console and create a new Lambda function.
2. Choose Python as the runtime and add the necessary IAM Role with the following permissions:
   - `logs:FilterLogEvents` (to read CloudWatch Logs).
   - `sns:Publish` (to send alerts via SNS).

### 2. Configure SNS

1. Create a new SNS topic in the **SNS Console** (e.g., `AlertTopic`).
2. Add subscriptions to the SNS topic:
   - Email (to receive alerts).
   - Slack (using an incoming Webhook URL via Lambda if desired).
3. Copy the SNS Topic ARN and update the `ALERT_TOPIC_ARN` in the Lambda function code.

### 3. Configure CloudWatch Logs

1. Define the CloudWatch Logs group (`LOG_GROUP_NAME`) that the Lambda function should monitor.
2. Set up a CloudWatch Event or EventBridge rule to trigger the Lambda function at specific intervals or in response to new log events.
