---
tags: tech
aliases: [Computer Networks, computer networking]
publish: true
sr-due: 2022-10-07
sr-interval: 1
sr-ease: 230
---

## **Networking Basics**

- **Host** 
Receives and transfers traffic
- **IP Address**
Identifies host
- **Network**
Collection of hosts that share the same IP space (198.62.1.x)
- **Repeater**
Transfer signal further, regenerates it.
- **Hub**
Transfers signal to all connected hosts
Multiport repeater
- **Bridge**
Transfers signal in the opposite direction to which it was sent
- **Switch**
Communication within a network
Combination of hub and bridge. Sends packets to the destination host
- **Router**
Communication between networks
Trafic control point:  security, filtering, redirecting
Learn which networks they are attached to in the **routing table**
Each network has a **gateway** which is the way out of the local network

Many devices that perform routing / switching:
- **Access points**
- **Firewalls**
- Load balancers
- layer 3 switches
- IDS / IPS
- **Proxies**
- Virtual switches / routers

- https://www.youtube.com/watch?v=H7-NR3Q3BeI&list=PLIFyRwBY_4bRLmKfP1KnZA6rZbRHtxmXi&index=2&ab_channel=PracticalNetworking
-   [https://study-ccna.com/what-is-a-network/](https://study-ccna.com/what-is-a-network/)
-   OSI Model [https://www.guru99.com/layers-of-osi-model.html](https://www.guru99.com/layers-of-osi-model.html)

## **IP Addresses and Subnet mask**

**Subnetting** is the practice of dividing a network into two or more smaller networks. It increases routing efficiency, enhances the security of the network, and reduces the size of the broadcast domain.

-   [https://study-ccna.com/subnetting-explained/](https://study-ccna.com/subnetting-explained/)
-   Subnet Calculator: [http://www.subnet-calculator.com](http://www.subnet-calculator.com/)

## **IP Routing**

-   [https://study-ccna.com/what-is-ip-routing/](https://study-ccna.com/what-is-ip-routing/)

## **Vlans**

Le VLAN **permet de définir un nouveau réseau au-dessus du réseau physique** et à ce titre offre les avantages suivants : Plus de souplesse pour l'administration et les modifications du réseau car toute l'architecture peut être modifiée par simple paramètrage des commutateurs.

-   [https://study-ccna.com/what-is-a-vlan/](https://study-ccna.com/what-is-a-vlan/)

## **Access Control Lists**

ACLs are a set of rules used most commonly to filter network traffic. They are used on network devices with packet filtering capatibilites (e.g. routers or firewalls). ACLs are applied on the interface basis to packets leaving or entering an interface.

-   [https://study-ccna.com/what-are-acls/](https://study-ccna.com/what-are-acls/)

## **VPN**

Network with encrypted traffic 
3 types of VPN

-   [https://www.cisco.com/c/en/us/solutions/small-business/resource-center/security/how-does-a-vpn-work.html#~types-of-vpn-topologies](https://www.cisco.com/c/en/us/solutions/small-business/resource-center/security/how-does-a-vpn-work.html#~types-of-vpn-topologies)

## **Ports**

16-bit number associated with a network protocol that identifies a specific application or service.
TCP and UDP specify the source and destination port numbers in their packet headers and that information, along with the source and destination IP addresses and the transport protocol (TCP or UDP), enables applications running on hosts on a TCP/IP network to communicate.
Applications that provide a service (such as FTP and HTTP servers) open a port on the local computer and listen for connection requests. A client can request the service by pointing the request to the application’s IP address and port. A client can use any locally unused port number for communication.

- **Port numbers**
Port numbers are from 0 to 65535. The first 1024 ports are reserved for use by certain privileged services:

![[Pasted image 20230706153442.png|300]]

-   [https://study-ccna.com/ports-explained/](https://study-ccna.com/ports-explained/)
-   [https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers](https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers)

## **TCP / UDP**

UDP is simpler than TCP but has less features. Used for video games where the amount of messages exchanged has to be minimised.
**TCP is a connection-oriented protocol, whereas UDP is a connectionless protocol**. A key difference between TCP and UDP is speed, as TCP is comparatively slower than UDP.

-   How TCP works: [https://www.cisco.com/E-Learning/bulk/public/tac/cim/cib/using_cisco_ios_software/linked/tcpip.htm](https://www.cisco.com/E-Learning/bulk/public/tac/cim/cib/using_cisco_ios_software/linked/tcpip.htm)
-   TCP explained [https://study-ccna.com/tcp-explained/](https://study-ccna.com/tcp-explained/)
-   TCP explained2 [https://en.wikipedia.org/wiki/Transmission_Control_Protocol](https://en.wikipedia.org/wiki/Transmission_Control_Protocol)
-   UDP explained [https://en.wikipedia.org/wiki/User_Datagram_Protocol](https://en.wikipedia.org/wiki/User_Datagram_Protocol)

## **Public / Private Key exchange / security explained**

-   [https://en.wikipedia.org/wiki/Public-key_cryptography](https://en.wikipedia.org/wiki/Public-key_cryptography)

## **Security Certificates & CAs**

**Secure Sockets Layer** (SSL) and **Transport Layer security** (TLS ) are protocols that provide secure communications over a computer network or link.
They are commonly used in web browsing and email.
SSL refers to TLS which a better version.
SSL/TLS provides data encryption, data integrity and authentication.

-   [http://www.steves-internet-guide.com/ssl-certificates-explained/](http://www.steves-internet-guide.com/ssl-certificates-explained/)