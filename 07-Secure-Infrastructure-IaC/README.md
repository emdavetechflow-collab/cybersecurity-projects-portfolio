Project 7: Secure Infrastructure as Code (IaC)
The Problem
Building cloud networks manually through the web console is slow and dangerous. Humans make typos that leave networks exposed to the internet (like public subnets), and rebuilding the network in a disaster takes hours.

The Solution
I developed Infrastructure as Code using Terraform to build an AWS VPC and Subnet. I implemented a Shift Left security approach by using Checkov to scan the Terraform manifests for critical misconfigurations (like public IP mapping) before the infrastructure was ever built.

The Proof
Insecure Infrastructure Scan (Before):(![insecure neetwork
](<proj7screenshot1 failed scan.png>))

Hardened Infrastructure Scan (After):(![secure network
](<proj7screenshot2 passed scan.png>))
