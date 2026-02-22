# --- Variables ---
cloud_provider = "AWS"
region = "us-east-1"
is_production = True

print("Cloud Provider:", cloud_provider)
print("Region:", region)
print("Production:", is_production)

# --- List (think: EC2 instances) ---
instances = [
    {"InstanceId": "i-11111", "State": "running"},
    {"InstanceId": "i-22222", "State": "stopped"},
    {"InstanceId": "i-33333", "State": "running"},
    {"InstanceId": "i-44444", "State": "terminated"}
]

# --- State the Function first ---
def check_instance_health(instance):
    try:
        instance_id = instance["InstanceId"]
        state = instance["State"]

        if state == "running":
            return f"Instance {instance_id} is Healthy."
        elif state == "stopped":
            return f"Instance {instance_id} is Stopped. Needs attention."
        else:
            return f"Instance {instance_id} is in unknown state '{state}'. Check status."
    except KeyError as e:
        return f"Error: Missing key {e} in instance data."

# --- Using the function to check health of instances ---
print("\n--- EC2 Instance Health Check ---")

for instance in instances:
    result = check_instance_health(instance)
    print(result)

# --- Dictionary (Singele AWS resources) ---
print("\n--- Single Instance Metadata ---")

instance_info = {
    "InstanceId": "i-67890",
    "State": "stopped",
    "InstanceType": "t2.micro",
    "AvailabilityZone": "us-east-1a"
}

state = instance_info["State"]

if state == "running": 
    print("Instance is healthy.")
else:
    print("Instance needs attention.")

print("Instance ID:", instance_info["InstanceId"])
print("State:", instance_info["State"])
print("Type:", instance_info["InstanceType"])
print("AZ:", instance_info["AvailabilityZone"])