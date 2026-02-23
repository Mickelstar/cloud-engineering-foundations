# --- Cloud Environment Configuration ---

ENVIRONMENTS = {
    "dev": {
        "region": "us-east-1",
        "instance_type": "t2.micro",
        "max_instances": 2
    },
    "prod": {
        "region": "us-east-1",
        "instance_type": "t3.medium",
        "max_instances": 10
    }
}

# --- Select Environment ---
current_env = "prod" # change to "prod" later

# --- safety check ---
if current_env not in ENVIRONMENTS:
    raise ValueError("Invalid environment specified!")

# --- Load Configuration ---
config = ENVIRONMENTS[current_env]

print("Environment:", current_env)
print("Region:", config["region"])
print("Instance Type:", config["instance_type"])
print("Max Instances:", config["max_instances"])