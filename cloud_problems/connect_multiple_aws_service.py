import boto3
import redis
import pika
import requests
import csv
import logging
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError
from requests.exceptions import RequestException

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def s3_operations(bucket_name, file_name, data):
    try:
        s3 = boto3.client('s3')
        s3.put_object(Bucket=bucket_name, Key=file_name, Body=data)
        logger.info(f"Successfully wrote data to {bucket_name}/{file_name}")
        
        response = s3.get_object(Bucket=bucket_name, Key=file_name)
        content = response['Body'].read().decode('utf-8')
        logger.info(f"Read data from {bucket_name}/{file_name}: {content}")
    except (NoCredentialsError, PartialCredentialsError) as e:
        logger.error("S3 Credentials not available", exc_info=True)
    except ClientError as e:
        logger.error(f"Failed S3 operation: {e}", exc_info=True)

def redis_operations(host, port, key, value):
    try:
        r = redis.Redis(host=host, port=port)
        r.set(key, value)
        logger.info(f"Set key {key} with value {value} in Redis")
        
        result = r.get(key)
        logger.info(f"Got value {result.decode('utf-8')} for key {key} from Redis")
    except redis.RedisError as e:
        logger.error(f"Failed Redis operation: {e}", exc_info=True)

def rabbitmq_operations(queue_name, message):
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        channel.queue_declare(queue=queue_name)
        logger.info(f"Queue {queue_name} declared in RabbitMQ")
        
        channel.basic_publish(exchange='', routing_key=queue_name, body=message)
        logger.info(f"Sent message: {message} to queue {queue_name}")

        method_frame, header_frame, body = channel.basic_get(queue=queue_name)
        if method_frame:
            logger.info(f"Received message: {body.decode('utf-8')}")
            channel.basic_ack(method_frame.delivery_tag)
        else:
            logger.info(f"No message returned from queue {queue_name}")
        
        connection.close()
    except pika.exceptions.AMQPError as e:
        logger.error(f"Failed RabbitMQ operation: {e}", exc_info=True)

def sqs_operations(queue_url):
    try:
        sqs = boto3.client('sqs')
        response = sqs.receive_message(QueueUrl=queue_url, MaxNumberOfMessages=1)
        messages = response.get('Messages', [])
        if messages:
            message = messages[0]
            logger.info(f"Received message: {message['Body']}")
            sqs.delete_message(QueueUrl=queue_url, ReceiptHandle=message['ReceiptHandle'])
            logger.info(f"Deleted message from queue")
        else:
            logger.info("No messages to receive from SQS")
    except (NoCredentialsError, PartialCredentialsError) as e:
        logger.error("SQS Credentials not available", exc_info=True)
    except ClientError as e:
        logger.error(f"Failed SQS operation: {e}", exc_info=True)

def rds_operations(secret_name, region_name):
    try:
        session = boto3.session.Session()
        client = session.client(service_name='secretsmanager', region_name=region_name)
        secret_response = client.get_secret_value(SecretId=secret_name)
        secret = secret_response['SecretString']
        logger.info(f"Retrieved secret: {secret}")
    except ClientError as e:
        logger.error(f"Failed to retrieve secret or connect to RDS: {e}", exc_info=True)

def aurora_operations(db_cluster_id, db_username, region_name):
    try:
        rds_client = boto3.client('rds', region_name=region_name)
        token = rds_client.generate_db_auth_token(DBHostname=db_cluster_id, Port=3306, DBUsername=db_username)
        logger.info(f"Generated IAM authentication token for Aurora: {token}")
    except ClientError as e:
        logger.error(f"Failed Aurora operation: {e}", exc_info=True)

def check_internet_connectivity(url="http://www.google.com"):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            logger.info("Internet connectivity is available")
        else:
            logger.warning("Internet connectivity is available but returned an unexpected status code")
    except RequestException as e:
        logger.error("No internet connectivity", exc_info=True)

def get_ec2_instance_name(instance_id, region_name):
    try:
        ec2_client = boto3.client('ec2', region_name=region_name)
        response = ec2_client.describe_instances(InstanceIds=[instance_id])
        instance = response['Reservations'][0]['Instances'][0]
        instance_name = next((tag['Value'] for tag in instance['Tags'] if tag['Key'] == 'Name'), None)
        logger.info(f"EC2 Instance Name: {instance_name}")
        return instance_name
    except ClientError as e:
        logger.error(f"Failed to retrieve EC2 instance name: {e}", exc_info=True)

def main():
    try:
        with open('config.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                service_name = row['service_name'].lower()
                logger.info(f"Processing service: {service_name} with parameters: {row}")

                if service_name == 's3':
                    s3_operations(row['param1'], row['param2'], row['param3'])
                elif service_name == 'redis':
                    redis_operations(row['param1'], row['param2'], row['param3'], row['param4'])
                elif service_name == 'rabbitmq':
                    rabbitmq_operations(row['param1'], row['param2'])
                elif service_name == 'sqs':
                    sqs_operations(row['param1'])
                elif service_name == 'rds':
                    rds_operations(row['param1'], row['param2'])
                elif service_name == 'aurora':
                    aurora_operations(row['param1'], row['param2'], row['param3'])
                elif service_name == 'internet':
                    check_internet_connectivity(row['param1'])
                elif service_name == 'ec2':
                    get_ec2_instance_name(row['param1'], row['param2'])
                else:
                    logger.warning(f"Unknown service: {service_name}")

    except FileNotFoundError:
        logger.error("Configuration file not found", exc_info=True)
    except KeyError as e:
        logger.error(f"Missing parameter in the configuration file: {e}", exc_info=True)
    except Exception as e:
        logger.error(f"An error occurred: {e}", exc_info=True)

if __name__ == "__main__":
    main()
