Project 5: Kubernetes Cluster Hardening
The Problem
Kubernetes is the engine that runs modern applications, but default configurations are dangerously insecure. Hackers exploit misconfigurations like "Container Escape" to break out of their assigned box and take control of the entire cluster.

The Solution
I used Kubescape to scan Kubernetes deployment YAMLs for security misconfigurations based on the NSA framework. I identified critical failures (privilege escalation, mutable filesystems, running as root) and wrote a hardened deployment manifest using strict securityContext policies and resource limits.

The Proof
Insecure App Scan (Before):(![insecure app output
](<pro5screenshot secured d app.png>))

Hardened App Scan (After):(![secure app-resolved
](<proj5screenshot inseecure app.png>))