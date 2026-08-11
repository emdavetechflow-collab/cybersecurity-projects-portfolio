import time

# --- THE DATABASE ---
# This holds our user and their valid login token
database = {
    "user_token": {
        "username": "county_admin",
        "original_ip": "192.168.1.10", # Normal county IP (Pittsburgh)
        "risk_level": "low",
        "valid": True
    }
}

print("🏦 Welcome to the Cloud Identity Provider (Simulator)\n")

# --- STEP 1: Normal User Logs In ---
print("--- Step 1: Normal Employee Login ---")
print("✅ User 'county_admin' logs in from Pittsburgh (192.168.1.10).")
print("Token generated and risk level set to LOW.\n")

# --- STEP 2: The Hacker Attack ---
print("--- Step 2: Hacker Steals Token! ---")
print("🚨 ALERT: A hacker stole the county_admin's token from their browser!")
print("The hacker tries to use the token from Russia (185.220.101.15).\n")

# Simulate the hacker changing the token's IP address
stolen_token = database["user_token"]
stolen_token["current_ip"] = "185.220.101.15" # Hacker's IP
stolen_token["risk_level"] = "high" # Identity provider detects Impossible Travel!

# --- STEP 3: Conditional Access Policy ---
print("--- Step 3: Evaluating Conditional Access Policy ---")
print("Policy Rule: If risk_level == 'high', BLOCK access immediately.\n")

if stolen_token["risk_level"] == "high":
    print("🚨 ACCESS BLOCKED!")
    print("Reason: Impossible Travel detected. Token was used in Pittsburgh and Russia within 5 minutes.")
    print("Action: Token has been revoked. Account is locked until admin review.")
    stolen_token["valid"] = False
else:
    print("✅ ACCESS GRANTED.")