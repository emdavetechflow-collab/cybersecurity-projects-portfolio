Project 12: Identity Security Lab
The Problem
Modern attackers bypass firewalls and Multi-Factor Authentication by stealing session tokens via phishing or malware. Once they have the token, they are inside the network. Traditional security trusts the token, failing to verify the context of how the identity is being used.

The Solution
I architected an Identity Security simulation demonstrating Conditional Access Policies against token theft. I simulated an Impossible Travel attack where a stolen token was used across geographies, and engineered an automated policy that instantly evaluated the risk and revoked access.

The Proof
Conditional Access Policy blocking stolen token (Impossible Travel):(![Access blocked image
](<proj12 screenshot access blocked.png>))
