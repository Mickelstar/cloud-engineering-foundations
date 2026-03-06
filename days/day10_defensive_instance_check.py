instances = [
    {"InstanceId": "i-111", "State": {"Name": "running"}},
    {"InstanceId": "i-222"},  # Missing State
    {"InstanceId": "i-333", "State": {"Name": "stopped"}},
    {"InstanceId": "i-444", "State": {}},  # Missing Name
]

def get_instance_state(instance):
    try:
        return instance["State"]["Name"]
    except KeyError:
        return "unknown"

print("Defensive EC2 State Check:\n")

for instance in instances:
    instance_id = instance.get("InstanceId", "unknown-id")
    state = get_instance_state(instance)

    print(f"Instance {instance_id}: state = {state}")

REQUIRED_KEYS = ["InstanceId", "State"]

def validate_instance(instance):
    for key in REQUIRED_KEYS:
        if key not in instance:
            raise ValueError(f"Missing required key: {key}")

print("\nValidating instances...\n")

for instance in instances:
    try:
        validate_instance(instance)
        print(f"{instance['InstanceId']} is valid")
    except ValueError as e:
        print(f"Invalid instance data: {e}")