# Day 3 – Cloud Resource Summary & Prioritization

print("=== Cloud Environment Summary ===")

resources = [
    {"id": "i-201", "state": "running", "env": "prod", "owner": "payments"},
    {"id": "i-202", "state": "stopped", "env": "prod", "owner": "auth"},
    {"id": "i-203", "state": "running", "env": "dev", "owner": "payments"},
    {"id": "i-204", "state": "stopped", "env": "dev", "owner": "analytics"},
    {"id": "i-205", "state": "running", "env": "prod", "owner": "orders"},
    {"id": "i-206", "state": "stopped", "env": "prod", "owner": "inventory"},
]

total_resources = len(resources)
prod_issues = 0
dev_stopped = 0

print(f"Total resources: {total_resources}")

for r in resources:
    if r["env"] == "prod" and r["state"] != "running":
        prod_issues += 1
        print(f"[CRITICAL] {r['id']} in PROD owned by {r['owner']} is NOT running")

    if r["env"] == "dev" and r["state"] == "stopped":
        dev_stopped += 1

print("\n=== Summary Report ===")
print(f"Production issues: {prod_issues}")
print(f"Development resources stopped: {dev_stopped}")

if prod_issues > 0:
    print("ACTION REQUIRED: Investigate production outages immediately!")
else:
    print("All production resources are healthy.")