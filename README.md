# AWS-CloudWatch-Logs-Query-Automation-Script
This script automates querying logs from AWS CloudWatch Logs using boto3. It fetches logs from the past 5 hours and continuously monitors the query status until completion.

## Requirements
Python 3.x
boto3 library
AWS credentials with permissions to access CloudWatch Logs and run queries
Setup
Install the boto3 library:

sh
Copy code
pip install boto3
Configure your AWS credentials:
Ensure your AWS credentials are set up using environment variables, AWS configuration files, or IAM roles.

Clone this repository:

sh
Copy code
git clone https://github.com/your-username/aws-cloudwatch-logs-query-automation.git
cd aws-cloudwatch-logs-query-automation
Update the script:
Edit the script to include your log group name and AWS credentials.

Usage
Run the script:

sh
Copy code
python script_name.py
The script will start a query to fetch logs from the past 5 hours in the specified log group and will print the results once the query completes.

License
This project is licensed under the MIT License. See the LICENSE file for details.
