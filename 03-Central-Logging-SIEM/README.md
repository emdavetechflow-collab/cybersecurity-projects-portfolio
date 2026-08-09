Project 3: Central Logging Threat Hunter (SIEM)
The Problem
Without a Security Information and Event Management (SIEM) system, security teams are blind. Logs are scattered across hundreds of computers, making it impossible to catch hackers who are silently guessing passwords or moving through the network.

The Solution
I deployed a local ELK Stack (Elasticsearch, Logstash, Kibana) SIEM using Docker. I ingested simulated Windows Security logs and built a custom Python threat-hunting script. The script queries the Elasticsearch API to automatically detect brute-force attacks (more than 10 failed logins) and trigger a Critical Alert with the attacker's IP address.

The Proof
Kibana Dashboard showing the 50 Failed Login attempts:(![kibana 50 failed logins
](<proj3 screenshot3 kibana 50 passwords quess.png>))

Python Threat Hunter catching the attack automatically:(![threat hunter
](<proj3 screenshot2 threat alert .png>))
