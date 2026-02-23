# --- EC2 Instance Inventory ---

instances = [
    {"InstanceId": "i-001", "State": "running", "Env": "prod"},
    {"InstanceId": "i-002", "State": "stopped", "Env": "dev"},
    {"InstanceId": "i-003", "State": "running", "Env": "prod"},
    {"InstanceId": "i-004", "State": "terminated", "Env": "prod"},
    {"InstanceId": "i-005", "State": "running", "Env": "dev"}
]

current_env = "prod"

print(f"Checking instances in {current_env} environment...\n")

for instance in instances:
    if instance["Env"] == current_env:
        if instance["State"] == "running":
            print(f"{instance['InstanceId']} is RUNNING")
        else:
            print(f"{instance['InstanceId']} is {instance['State'].upper()} - ATTENTION")