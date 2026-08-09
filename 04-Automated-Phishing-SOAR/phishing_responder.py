import os
import re
import requests
import time
from dotenv import load_dotenv

# Load our secret API key
load_dotenv()
API_KEY = os.getenv("VT_API_KEY")

def analyze_email(email_text):
    print("🤖 SOAR Robot is reading the suspicious email...\n")
    
    # 1. Find the website link
    url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    urls = re.findall(url_pattern, email_text)
    
    if not urls:
        print("✅ No website links found. Safe!")
        return

    for url in urls:
        print(f"🔍 Found a link: {url}")
        print(" Submitting to VirusTotal for scanning...\n")
        
        headers = {"x-apikey": API_KEY}
        
        # Submit the link
        post_resp = requests.post("https://www.virustotal.com/api/v3/urls", headers=headers, data={"url": url})
        post_data = post_resp.json()
        
        # Check if we hit the speed limit
        if 'error' in post_data and 'QuotaExceededError' in post_data['error']['code']:
            print("⚠️ VirusTotal Free API limit reached. Triggering Quarantine based on suspicious context!\n")
            print(f"🚨 QUARANTINE EMAIL! Link: {url}")
            print(" Action: Block the sender and warn the user.\n")
            return

        # If we didn't hit the limit, let's try to get the report
        try:
            analysis_id = post_data['data']['id']
            print("⏳ Waiting 30 seconds for scan to finish...")
            time.sleep(30)
            
            response = requests.get(f"https://www.virustotal.com/api/v3/analyses/{analysis_id}", headers=headers)
            data = response.json()
            
            malicious_votes = data['data']['attributes']['stats']['malicious']
            
            if malicious_votes >= 2:
                print(f"🚨 QUARANTINE EMAIL! VirusTotal found {malicious_votes} security engines flagging this link!")
                print(" Action: Block the sender and warn the user.\n")
            else:
                print(f"✅ SAFE LINK. Only {malicious_votes} engines found issues.\n")
                
        except Exception:
            print("⚠️ Could not read the report due to API limits.")
            print(" However, the link is suspicious. Triggering Quarantine!\n")
            print(f"🚨 QUARANTINE EMAIL! Link: {url}")
            print(" Action: Block the sender and warn the user.\n")

# --- OUR FAKE PHISHING EMAIL ---
suspicious_email = """
From: boss@company.com
Subject: URGENT: Open this invoice immediately!

Hey, I need you to review this document right now, it is very important.
Do not tell anyone about this.

Click here: https://secure.eicar.org/eicar.com.txt
"""

# Run the robot!
analyze_email(suspicious_email)