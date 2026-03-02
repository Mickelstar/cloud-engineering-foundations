# --- Simulated AWS CLI: describe-instances ---

aws_cli_response = {
    "Reservations": [
        {
            "Instances": [
                {
                    "InstanceId": "i-aaa111",
                    "State": {"Name": "running"},
                    "InstanceType": "t3.micro",
                },
                {
                    "InstanceId": "i-bbb222",
                    "State": {"Name": "stopped"},
                    "InstanceType": "t3.micro",
                },
            ]
        },
        {
            "Instances": [
                {
                    "InstanceId": "i-ccc333",
                    "State": {"Name": "running"},
                    "InstanceType": "t3.micro",
                },
                {
                    "InstanceId": "i-ddd444",
                    "State": {"Name": "terminated"},
                    "InstanceType": "t3.micro",
                },
            ]
        }
    ]
}

running_instances = []

for reservation in aws_cli_response["Reservations"]:
    for instance in reservation["Instances"]:
        state = instance["State"]["Name"]
        if state == "running":
            running_instances.append(instance["InstanceId"])

print("Running instances:")
for instance_id in running_instances:
    print("-", instance_id)

print(f"Total running instances: {len(running_instances)}")