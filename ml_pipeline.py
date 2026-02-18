import json

def score_root_usage(finding):
    if "Tele2 Sweden" in str(finding):
        return 8.7  # High risk ISP
    return 2.0

# Testa med din finding
with open('findings.json') as f:
    data = json.load(f)
    print("Tele2 Sweden risk score:", score_root_usage(data))
