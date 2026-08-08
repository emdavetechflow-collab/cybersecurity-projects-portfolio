Project 1: DevSecOps Automated Security Pipeline
The Problem
Developers sometimes accidentally leave passwords and API keys in their code, or use outdated software libraries with known security holes. If this code gets published, hackers can easily find these secrets and break into the company's cloud infrastructure. Manual security checks are too slow and miss things.

The Solution
I built a GitHub Actions CI/CD pipeline that automatically scans code every time a developer pushes a commit. It uses:

Gitleaks: To scan for hardcoded secrets, passwords, and API keys.
Trivy: To scan software dependencies (like Python libraries) for Critical and High severity vulnerabilities.
If a secret or vulnerability is found, the pipeline automatically FAILS, blocking the bad code from being merged.

The Proof
Pipeline catching a vulnerability (OLD Flask version) and failing the build:(![problem image](<proj 1 sscren 1.png>))

Pipeline passing after the vulnerability was fixed and code was secured:(![solution image](<proj1 secrenshot 3 prob fix.png>))

How to use
Create a .github/workflows/ directory in your repository.
Copy the security-scan.yml file into that directory.
Push code. The pipeline will run automatically.
