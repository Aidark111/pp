import json

with open("lab4/sample-data.json") as f:
    json_data = json.load(f)

interface_data = json_data.get("imdata", [])

header = "Interface Status"
separator = "=" * 80

print(header)
print(separator)
print("{:<50} {:<20} {:<8} {:<6}".format("DN", "Description", "Speed", "MTU"))
print("-" * 80)

for interface in interface_data:
    attributes = interface.get("l1PhysIf", {}).get("attributes", {})
    dn = attributes.get("dn", "")
    speed = attributes.get("speed", "inherit")
    mtu = attributes.get("mtu", "9150")
    print("{:<50} {:<20} {:<8} {:<6}".format(dn, "", speed, mtu))
