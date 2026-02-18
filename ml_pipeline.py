def score_root_usage(finding):
    if "Tele2 Sweden" in finding["Actor"]["IpAddressV4"]:
        return 8.7  # High risk ISP
    return 2.0
