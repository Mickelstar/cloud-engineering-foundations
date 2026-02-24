# --- Environment-Aware Scaling Monitor ---

ENVIRONMENTS = {
    "dev": {
        "DesiredCapacity": 1
    },
    "prod": {
        "DesiredCapacity": 3
    }
}

instances = [
    {"InstanceId": "i-001", "State": "running", "Env": "prod"},
    {"InstanceId": "i-102", "State": "stopped", "Env": "prod"},
    {"InstanceId": "i-103", "State": "running", "Env": "prod"},
    {"InstanceId": "i-201", "State": "running", "Env": "dev"},
]

current_env = "prod"

if current_env not in ENVIRONMENTS:
    raise ValueError("Inavlid environment specified")

desired = ENVIRONMENTS[current_env]["DesiredCapacity"]

running_count = 0

for instance in instances:
    if instance["Env"] == current_env and instance["State"] == "running":
        running_count += 1
    
print(f"Environment: {current_env}")
print(f"Running instances: {running_count}")
print(f"Desired capacity: {desired}")

if running_count < desired:
    print("Action: SCALE UP")
elif running_count > desired:
    print("Action: SCALE DOWN")
else:
    print("Action: NO ACTION NEEDED")