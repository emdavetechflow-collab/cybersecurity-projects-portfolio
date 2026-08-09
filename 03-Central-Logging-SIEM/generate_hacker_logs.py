from elasticsearch import Elasticsearch
import datetime

# Connect to our local SIEM brain
es = Elasticsearch("http://localhost:9200")

print("🤖 Sending simulated hacker Brute-Force logs to SIEM...\n")

index_name = "windows-security-logs"

# Simulate 50 failed logins (The Hacker!)
for i in range(50):
    log = {
        "timestamp": datetime.datetime.now().isoformat(),
        "computer": "WIN-SERVER-01",
        "event_id": 4625, # Windows Event ID for Failed Logon
        "status": "FAILURE",
        "username": "Administrator",
        "source_ip": "192.168.1.55",
        "message": "An account failed to log on."
    }
    es.index(index=index_name, document=log)

print("🚨 50 Failed logins sent!")

# Simulate 1 successful login (The Hacker got in!)
log_success = {
    "timestamp": datetime.datetime.now().isoformat(),
    "computer": "WIN-SERVER-01",
    "event_id": 4624, # Windows Event ID for Successful Logon
    "status": "SUCCESS",
    "username": "Administrator",
    "source_ip": "192.168.1.55",
    "message": "An account was successfully logged on."
}
es.index(index=index_name, document=log_success)

print("💀 1 Successful login sent! The hacker guessed the password!")
print("\n✅ Done! Go check your Kibana dashboard.")