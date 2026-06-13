class employee:

    def __init__(self,name,role):
        self.name = name
        self.role=role

    def display(self):
        print(self.name)
        print(self.role)

employee1=employee("Bharath","SRE")
employee1.display()

# #list S3 Buckets
# import boto3

# s3=boto3.client('s3')
# responses=s3.list_buckets()

# for bucket in responses['Buckets']:
#     print(bucket['Name'])

# #List EC2 instances
# ec2 = boto3.client('ec2')
# response = ec2.describe_instances()
# print(response)

#Multi Threading
from threading import Thread

def task():
    print("Task started")

def task2():
    print("Second task started")

t1=Thread(target=task)
t1.start()

t2=Thread(target=task2)
t2.start()


#Useful linux automation scripts
import shutil
total,used,free =shutil.disk_usage("/")
print(f"Total: {total}")

#CPU Monitoring
import psutil
cpu_percent = psutil.cpu_percent(interval=1)
print(cpu_percent)

#interview faviorite one liner

#Reverse String
name = "Bharath"
reverse_name = name[::-1]
print(reverse_name)

#Find duplicates

nums = [1,2,1,3,1,4,2,5]

duplicates = set(
    x for x in nums
    if(nums.count(x) > 1)
)

print(duplicates)

#Common devops use cases
# import yaml

# with open("config.yaml") as file:
#     data = yaml.safe_load(file)

# print(data)

#Parse kubernetes output
# import json

# with open("pods.json") as file:
#     data = json.load(file)

# print(data)

# for item in data["items"]:
#     print(item["metadata"]["name"])

#Github ACtions API
import token
import requests

headers = {
    "Authorization": f"token{GITHUB_TOKEN}"
}

requests.get(url,headers)
