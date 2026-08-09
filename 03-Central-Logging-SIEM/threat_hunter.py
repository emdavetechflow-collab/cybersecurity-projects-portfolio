from elasticsearch import Elasticsearch

# Connect to our SIEM brain
es = Elasticsearch("http://localhost:9200")

print("🤖 Threat Hunter is checking SIEM for Brute Force attacks...\n")

# Ask Elasticsearch to count the failed logins
query = {
    "size": 0,
    "query": {
        "match": {
            "status": "FAILURE"
        }
    }
}

response = es.search(index="windows-security-logs", body=query)
fail_count = response['hits']['total']['value']

# If the failures are more than 10, we have a hacker!
if fail_count > 10:
    print(f"🚨 CRITICAL ALERT: {fail_count} Failed logins detected!")
    print("A Brute Force attack is happening right now!")
    print("Attacker IP: 192.168.1.55")
    print("Action: Block IP address immediately at the firewall!\n")
else:
    print(f"✅ All clear. Only {fail_count} failed logins. No attack detected.")