# Day 2 – Cloud-Oriented Python Logic

print("=== Cloud Resource Environment Check ===")

resources = [
    {"id": "i-101", "state": "running", "env": "prod"},
    {"id": "i-102", "state": "stopped", "env": "dev"},
    {"id": "i-103", "state": "running", "env": "dev"},
    {"id": "i-104", "state": "stopped", "env": "prod"},
    {"id": "i-105", "state": "bad state", "env": "prod"}
]

def evaluate_resource(resource):
    resource_id = resource["id"]
    state = resource["state"]
    env = resource["env"]

    if env == "prod" and state != "running":
        return f"[ALERT] {resource_id} in PROD is not running!"
    elif env == "dev" and state != "running":
        return f"[INFO] {resource_id} in DEV is stopped (acceptable)."
    else:
        return f"[OK] {resource_id} is healthy."

for r in resources:
    result = evaluate_resource(r)
    print(result)