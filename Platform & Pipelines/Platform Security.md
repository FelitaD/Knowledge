---
tags: tech
aliases:
publish: true
sr-due: 2022-10-13
sr-interval: 5
sr-ease: 228
---

Goal : not everyone has access to all the data

## Network security
### Networks, Firewalls and ACL (Access Control Lists)
- Platform divided into networks
- Firewall contains an Access Control List to control who can commmunicate
	- Identifies which IP Address, which network and port
	- Which direction can communicate (in and out)

![[Pasted image 20220830134220.png]]

### Proxy servers
Very common in local setup
Works like an Access Control List 
Gives access to external clients to servers through a particular protocol
Service like Squid Proxy 
Once installed, doesn't need management and can go transparently through it.
Not enough secure for some. If proxy server hacked, you're in.

![[Pasted image 20220830135501.png]]

### Bastion Hosts
Dedicated Linux machines who have access to other networks
Clients log remotely to the machine.

![[Pasted image 20220830145026.png]]




## Access Management
### IAM (Identity and Access Management)
Distinction identity / access :
- Identity : the user
- Access : what can the user do

![[Pasted image 20220830145910.png]]

### LDAP (Lightweight Director Access Protocol)

Guarantees that user authentication is valid.
LDAP allows a user to search for an individual without knowing where they're located
The common use of LDAP is to provide a central place for authentication -- meaning it stores usernames and passwords

![[Pasted image 20220830150201.png]]




## Data Transmission Security
### HTTPS and SSH, SCP
- Encrypted connections
- Exchange encryption keys private / public

### Tokens

JWT

![[Pasted image 20220830151645.png]]