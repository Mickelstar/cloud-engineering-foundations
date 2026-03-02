FEATURE_FLAGS = {
    "enable_autoscaling": True,
    "enable_detailed_logs": True,
    "allow_instance_termination": False
}

print("Feature Flags Status:")

for feature, enabled in FEATURE_FLAGS.items():
    status = "ENABLED" if enabled else "DISABLED"
    print(f"- {feature}: {status}")

print("\nEvaluating behavior...")

if FEATURE_FLAGS["enable_autoscaling"]:
    print("Auto Scaling is ACTIVE")
else:
    print("Auto Scaling is OFF")

if FEATURE_FLAGS["allow_instance_termination"]:
    print("Instances can be terminated")
else:
    print("Instance termination is BLOCKED")