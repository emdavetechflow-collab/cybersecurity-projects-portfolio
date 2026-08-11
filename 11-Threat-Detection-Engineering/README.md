Project 11: Threat Detection Engineering
The Problem
Default SIEM alerts miss advanced hacker techniques. Writing custom detection rules for specific SIEMs (like Splunk or Elastic) creates vendor lock-in and makes it hard to share detections with the community.

The Solution
I authored a custom Threat Detection rule using the SIGMA standard to target MITRE ATT&CK T1059.001 (Encoded PowerShell). I then used the SIGMA CLI to automatically translate the rule into native query languages for both Elastic (KQL) and Splunk (SPL), demonstrating vendor-neutral detection engineering.

The Proof
SIGMA Rule (Universal Standard):See suspicious_powershell.yml

Translated for Elastic/Kibana:(![Elastic translation
](<proj11 screenshot suspiciuos powershel comand.png>))

Translated for Splunk:(![splunk translation
](<proj11 splunk output.png>))
