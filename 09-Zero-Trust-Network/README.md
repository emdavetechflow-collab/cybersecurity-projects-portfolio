Project 9: Zero Trust Network Architecture
The Problem
Traditional security relies on a "Castle and Moat" approach. Once a user or hacker is inside the network firewall, they are implicitly trusted and can access resources. This leads to massive breaches when attackers steal internal credentials.

The Solution
I implemented a Zero Trust Architecture using token-based identity verification. Instead of trusting requests based on their network location, the application demands an API Key (Identity Badge) in the HTTP headers. If the key is missing or invalid, the request is strictly denied with a 401 Unauthorized error.

The Proof
Access denied without identity verification (Zero Trust working):(![access denied
](<proj9 screenshot2 unauthorised .png>))

Access granted when correct identity (API Key) is provided:(![with aapikey
](<pro9screenshot3 with apikey.png>))
