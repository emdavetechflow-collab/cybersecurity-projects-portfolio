Project 6: Purple Team Attack & Defend Simulation
The Problem
Defenders often assume their security tools will catch hackers, but they never test them. When a real attack happens, they find out the alarms were silent the whole time.

The Solution
I conducted a Purple Team simulation to validate defensive capabilities. I simulated a real-world Brute Force attack (MITRE ATT&CK T1110), verified the attack left a footprint in Windows Security logs (Event ID 4625), and authored a SIGMA detection rule to automate future alerting.

The Proof
Red Team: Simulated Attack (Failed Logon):(![attack proof
](<proj6screenshot1 attack proof .png>))

Blue Team: Attack Footprint in Windows Event Viewer (Event ID 4625):(![attack footprint
](<proj6 screenshot2 defense proof.png>))

Detection Rule (SIGMA):See `detect-brute-force.yml
