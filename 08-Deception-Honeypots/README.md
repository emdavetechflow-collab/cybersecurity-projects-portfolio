Deception Technology (Honeypot Network)
The Problem
Hackers often silently penetrate networks without triggering alarms because their activity looks similar to normal users. Defenders need a way to guarantee that if someone is poking around, it is definitely a threat.

The Solution
I developed a custom Deception Technology (Honeypot) using Python. The script emulates a fake server with a login prompt to attract attackers. When an attacker attempts to log in, the Honeypot denies access but secretly captures their source IP address, attempted username, and password, logging the intelligence for threat analysis.

The Proof
Honeypot catching a simulated hacker in real-time:(![Alert
](<proj8 screenshot1 honeypot trap .png>))

Captured intelligence saved for analysis:(![captured intelligence
](<proj8screenshot2 hacker denied.png>))
