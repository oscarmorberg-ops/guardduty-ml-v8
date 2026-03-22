## GuardDuty ML v8.0 – Live Findings Pipeline

Current findings (simulated GuardDuty stream):

- 3 CRITICAL – e.g. UnauthorizedAccess:EC2/SSHBruteForce, CryptoCurrency:EC2/BitcoinTool [web:987][web:979]  
- 5 HIGH – e.g. Trojan:EC2/DriveBySourceTraffic [web:987][web:979]  
- 12 MEDIUM – behavior anomalies on IAM/API usage [web:978][web:981]  
- 20+ LOW – port scans and blocked probes

All findings are enriched, scored and pushed into the CSIO dashboard in near real time.
