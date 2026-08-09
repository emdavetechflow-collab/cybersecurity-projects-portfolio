Project 2: Cloud Security Posture Manager (CSPM)
The Problem
Cloud environments like AWS are massive. Humans frequently make misconfigurations, such as leaving S3 storage buckets open to the public internet. Hackers use automated scanners to find these open buckets and steal data. Manually checking thousands of resources is impossible.

The Solution
I developed a custom Cloud Security Posture Management (CSPM) tool using Python and the Boto3 library. The script connects to AWS, audits all S3 buckets for public access settings, and if a vulnerability is found, it automatically remediates the issue by applying the "Block Public Access" setting.

The Proof
Here is the script catching an insecure public bucket and automatically securing it:(![image of security alert and fix
](<Proj2 scren 1.png>))
