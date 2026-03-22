# GuardDuty ML v8.0 – Live Findings Pipeline

This project simulates a live Amazon GuardDuty findings stream and processes it with a custom ML‑driven pipeline. It ingests raw findings, enriches them with context, assigns risk scores, and pushes prioritized alerts into my CCISO security dashboard in near real time.

## Current simulated findings

- 3 CRITICAL – e.g. UnauthorizedAccess:EC2/SSHBruteForce, CryptoCurrency:EC2/BitcoinTool  
- 5 HIGH – e.g. Trojan:EC2/DriveBySourceTraffic  
- 12 MEDIUM – behavior anomalies on IAM/API usage  
- 20+ LOW – port scans and blocked probes  

All findings are normalized, enriched and scored before being sent to the dashboard, so I can focus on high‑impact alerts instead of raw noise.
