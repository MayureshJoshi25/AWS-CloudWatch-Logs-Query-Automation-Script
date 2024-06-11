# AWS-CloudWatch-Logs-Query-Automation-Script
This script automates querying logs from AWS CloudWatch Logs using boto3. It fetches logs from the past 5 hours and continuously monitors the query status until completion.

## Requirements
Python 3.x
boto3 library
AWS credentials with permissions to access CloudWatch Logs and run queries

## Setup
1. Install the boto3 library:
```
pip install boto3
```

2. Configure your AWS credentials:
Ensure your AWS credentials are set up using environment variables, AWS configuration files, or IAM roles.

3. Clone this repository:
```
git clone https://github.com/your-username/aws-cloudwatch-logs-query-automation.git
cd aws-cloudwatch-logs-query-automation
```

4. Update the script:
Edit the script to include your log group name and AWS credentials.

## Usage
Run the script:
```
python script_name.py
```
The script will start a query to fetch logs from the past 5 hours in the specified log group and will print the results once the query completes.

