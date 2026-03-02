ENVIRONMENTS = {
    "dev": {
        "instance_type": "t3.micro",
        "max_instances": 1
    },
    "prod": {
        "instance_type": "m5.large",
        "max_instances": 5
    }
}

current_env = "prod"  # change to "prod" carefully

if current_env not in ENVIRONMENTS:
    raise ValueError("Invalid environment")

config = ENVIRONMENTS[current_env]

print(f"Running in {current_env.upper()} environment")
print("Instance type:", config["instance_type"])
print("Max instances:", config["max_instances"])

if current_env == "prod":
    confirm = input("You are in PROD. Type YES to continue: ")
    if confirm != "YES":
        print("Aborted.")
        exit()