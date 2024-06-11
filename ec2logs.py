import boto.ec2
import boto.logs
import boto3
import sys
from datetime import datetime, timedelta
import time

# Auth dictionary containing AWS access keys
auth = {"aws_access_key_id": "your_access_key_id_here", "aws_secret_access_key": "your_secret_access_key_here"}

# Create a CloudWatch Logs client using boto3
client = boto3.client('logs')

# Specify the CloudWatch Logs log group to query
log_group = "your_log_group_here"

# Define the query string to extract @timestamp and @message fields from logs
query = "fields @timestamp, @message"

# Start the CloudWatch Logs Insights query
start_query_response = client.start_query(
    logGroupName=log_group,  # Specify the log group name
    startTime=int((datetime.today() - timedelta(hours=5)).timestamp()),  # Query logs from the past 5 hours
    endTime=int(datetime.now().timestamp()),  # Up to the current time
    queryString=query,  # The query to run
)

# Retrieve the unique query ID from the response
query_id = start_query_response['queryId']

response = None  # Initialize the response variable

# Loop until the query completes
while response == None or response['status'] == 'Running':
    print('Waiting for query to complete ...')  # Print status message
    time.sleep(1)  # Wait for 1 second before checking the status again
    response = client.get_query_results(queryId=query_id)  # Fetch the query results

# At this point, the query has completed and the results are stored in the response variable
