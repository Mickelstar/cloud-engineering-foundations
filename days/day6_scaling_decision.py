# --- Auto Scaling Decision Simulation ---

instances = [
    {"InstanceId": "i-001", "State": "running"},
    {"InstanceId": "i-002", "State": "stopped"},
    {"InstanceId": "i-003", "State": "running"},
    {"InstanceId": "i-004", "State": "running"},
]

DESIRED_CAPACITY = 3

running_count = 0

for instance in instances:
    if instance["State"] == "running":
        running_count += 1

print(f"Running instances: {running_count}")
print(f"Desired capacity: {DESIRED_CAPACITY}")

if running_count < DESIRED_CAPACITY:
    print("Action: SCALE UP")
elif running_count > DESIRED_CAPACITY:
    print("Action: SCALE DOWN")
else:
    print("Action: NO ACTION NEEDED")