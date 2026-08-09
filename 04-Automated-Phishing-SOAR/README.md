Project 4: Automated Phishing Responder (SOAR)
The Problem
SOC analysts are overwhelmed by the volume of phishing emails. Manually extracting links, checking them against threat intelligence databases, and responding takes too long, allowing hackers to successfully steal credentials.

The Solution
I built a custom SOAR (Security Orchestration, Automation, and Response) automation script using Python. The script automatically reads suspicious emails, uses Regex to extract URLs, queries the VirusTotal API for threat intelligence, and automatically triggers a quarantine action if the link is deemed malicious.

The Proof
Here is the SOAR robot catching a malicious Eicar test link and automatically triggering the quarantine action:(![maliciuos eicar test link
](<proj4 screenshot1.png>))
