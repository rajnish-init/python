import requests

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")
complete_detail = response.json()

for i in range(len(complete_detail)):
    # print(i["title"]) # This will print the pull request number
    # print(i["user"]["login"]) # This will print the login name of the user who created the pull request

    print(complete_detail[i]["user"]["login"]) # This will print the login name of the user who created the first pull request















# ec2_instance_info = [
#     {
#         "id": "instance-001",
#         "type": "t2.micro"
#     },
#     {
#         "id": "instance-002",
#         "type": "t2.micro"
#     },
#     {
#         "id": "instance-003",
#         "type": "t2.micro"
#     }
# ]

# print(ec2_instance_info[1]["id"])