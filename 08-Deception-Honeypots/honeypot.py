import socket
import time
from datetime import datetime

LOG_FILE = "honeypot_logs.txt"
PORT = 2222 # We will hide our trap on port 2222

def log_attacker(ip, username, password):
    with open(LOG_FILE, "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{timestamp}] IP: {ip} | User: {username} | Pass: {password}\n")

def start_honeypot():
    print(f"🪤 Honeypot trap set! Listening for hackers on port {PORT}...\n")
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", PORT))
    server.listen(5)
    
    while True:
        # A hacker connects!
        attacker_socket, attacker_ip = server.accept()
        print(f"🚨 ALERT! Hacker detected from IP: {attacker_ip[0]}")
        
        try:
            # Send a fake login screen
            attacker_socket.send(b"Welcome to Secure Server.\r\nLogin: ")
            username = attacker_socket.recv(1024).decode().strip()
            
            attacker_socket.send(b"Password: ")
            password = attacker_socket.recv(1024).decode().strip()
            
            # Tell the hacker they failed, but we saved their data!
            attacker_socket.send(b"Access Denied.\r\n")
            
            # Save their secrets
            log_attacker(attacker_ip[0], username, password)
            print(f"   Captured -> User: {username} | Pass: {password}\n")
            
        except Exception:
            pass
        finally:
            attacker_socket.close()

# Run the trap!
start_honeypot()