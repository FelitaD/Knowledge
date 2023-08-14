<< [[A. Serialization And Compression Technical Details]]

This appendix discusses some factors data engineers should consider about networking in the cloud. Data engineers frequently encounter networking in their careers and often ignore it despite its importance.

# Cloud Network Topology

A _cloud network topology_ describes how various components in the cloud are arranged and connected, such as cloud services, networks, locations (zones, regions), and more. Data engineers should always know how cloud network topology will affect connectivity across the data systems they build. Microsoft Azure, Google Cloud Platform (GCP), and Amazon Web Services (AWS) all use remarkably similar resource hierarchies of availability zones and regions. At the time of this writing, GCP has added one additional layer, discussed in [“GCP-Specific Networking and Multiregional Redundancy”](https://learning.oreilly.com/library/view/fundamentals-of-data/9781098108298/app02.html#gcp_specific_networking_and_multiregion).

## Data Egress Charges

[Chapter 4](https://learning.oreilly.com/library/view/fundamentals-of-data/9781098108298/ch04.html#choosing_technologies_across_the_data_e) discusses cloud economics and how actual provider costs don’t necessarily drive cloud pricing. Regarding networking, clouds allow inbound traffic for free but charge for outbound traffic to the internet. Outbound traffic is not inherently cheaper, but clouds use this method to create a moat around their services and increase the stickiness of stored data, a practice that has been widely criticized.[1](https://learning.oreilly.com/library/view/fundamentals-of-data/9781098108298/app02.html#ch01fn86) Note that data egress charges can also apply to data passing between availability zones and regions within a cloud.

## Availability Zones

The _availability zone_ is the smallest unit of network topology that public clouds make visible to customers ([Figure B-1](https://learning.oreilly.com/library/view/fundamentals-of-data/9781098108298/app02.html#availability_zones_in_two_separate_regi)). While a zone can potentially consist of multiple data centers, cloud customers cannot control resource placement at this level.

![[Pasted image 20230308214357.png]]

Generally, clouds support their highest network bandwidth and lowest latency between systems and services within a zone. High throughput data workloads should run on clusters located in a single zone for performance and cost reasons. For example, an ephemeral Amazon EMR cluster should generally sit in a single availability zone.

In addition, network traffic sent to VMs within a zone is free, but with a significant caveat: traffic must be sent to private IP addresses. The major clouds utilize virtual networks known as _virtual private clouds_ (VPCs). Virtual machines have private IP addresses within the VPC. They may also be assigned public IP addresses to communicate with the outside world and receive traffic from the internet, but communications using external IP addresses can incur data egress charges.

## Regions

A _region_ is a collection of two or more availability zones. Data centers require many resources to run (electrical power, water, etc.). The resources of separate availability zones are independent so that a local power outage doesn’t take down multiple availability zones. Engineers can build highly resilient, separate infrastructure even within a single region by running servers in multiple zones or creating automated cross-zone failover processes.

Offering multiple regions allows engineers to put resources close to any of their users. _Close_ means that users can realize good network performance in connecting to services, minimizing physical distance along the network path, and a minimal number of hops through routers. Both physical distance and network hops can increase latency and decrease performance. Major cloud providers continue to add new regions.

In general, regions support fast, low-latency networking between zones; networking performance between zones will be worse than within a single zone and incur nominal data egress charges between VMs. Network data movement between regions is even slower and may incur higher egress fees.

In general, object storage is a regional resource. Some data may pass between zones to reach a virtual machine, but this is mainly invisible to cloud customers, and there are no direct networking charges for this. (Of course, customers are still responsible for object access costs.)

Despite regions’ geo-redundant design, many major cloud service failures have affected entire regions, an example of _correlated failure_. Engineers often deploy code and configuration to entire regions; the regional failures we’ve observed have generally resulted from code or configuration problems occurring at the regional level.

## GCP-Specific Networking and Multiregional Redundancy

GCP offers a handful of unique abstractions that engineers should be aware of if they work in this cloud. The first is the _multiregion_, a layer in the resource hierarchy; a multiregion contains multiple regions. Current multiregions are US (data centers in the United States), EU (data centers in European Union member states), and ASIA.

Several GCP resources support multiregions, including Cloud Storage and BigQuery. Data is stored in multiple zones within the multiregion in a geo-redundant manner so that it should remain available in the event of a regional failure. Multiregional storage is also designed to deliver data efficiently to users within the multiregion without setting up complex replication processes between regions. In addition, there are no data egress fees for VMs in a multiregion to access Cloud Storage data in the same multiregion.

Cloud customers can set up multiregional infrastructure on AWS or Azure. In the case of databases or object storage, this involves duplicating data between regions to increase redundancy and put data closer to users.

Google also essentially owns significantly more global-scale networking resources than other cloud providers, something it offers to its customers as _premium-tier networking_. Premium-tier networking allows traffic between zones and regions to pass entirely over Google-owned networks without traversing the public internet.

## Direct Network Connections to the Clouds

Each major public cloud offers enhanced connectivity options, allowing customers to integrate their networks with a cloud region or VPC directly. For example, Amazon offers AWS Direct Connect. In addition to providing higher bandwidth and lower latency, these connection options often offer dramatic discounts on data egress charges. In a typical scenario in the US, AWS egress charges drop from 9 cents per gigabyte over the public internet to 2 cents per gigabyte over direct connect.

# CDNs

_Content delivery networks_ (CDNs) can offer dramatic performance enhancements and discounts for delivering data assets to the public or customers. Cloud providers offer CDN options and many other providers, such as Cloudflare. CDNs work best when delivering the same data repeatedly, but make sure that you read the fine print. Remember that CDNs don’t work everywhere, and certain countries may block internet traffic and CDN delivery.

# The Future of Data Egress Fees

Data egress fees are a significant impediment to interoperability, data sharing, and data movement to the cloud. Right now, data egress fees are a moat designed to prevent public cloud customers from leaving or deploying across multiple clouds.

But interesting signals indicate that change may be on the horizon. In particular, Zoom’s announcement in 2020 near the beginning of the COVID-19 pandemic that it chose Oracle as its cloud infrastructure provider caught the attention of many cloud watchers.[2](https://learning.oreilly.com/library/view/fundamentals-of-data/9781098108298/app02.html#ch01fn87) How did Oracle win this significant cloud contract for critical remote work infrastructure against the cloud heavyweights? AWS expert Corey Quinn offers a reasonably straightforward answer.[3](https://learning.oreilly.com/library/view/fundamentals-of-data/9781098108298/app02.html#ch01fn88) By his back-of-the-envelope calculation, Zoom’s AWS monthly data egress fees would run over $11 million at list price; Oracle’s would cost less than $2 million.

We suspect that GCP, AWS, or Azure will announce significant cuts in egress fees in the next few years, leading to a sea change in the cloud business model. It’s also entirely possible that egress fees go away, similar to how limited and expensive cell-phone minutes disappeared decades ago.

[1](https://learning.oreilly.com/library/view/fundamentals-of-data/9781098108298/app02.html#ch01fn86-marker) Matthew Prince and Nitin Rao, “AWS’s Egregious Egress,” _The Cloudflare Blog_, July 23, 2021, [_https://oreil.ly/NZqKa_](https://oreil.ly/NZqKa).
[2](https://learning.oreilly.com/library/view/fundamentals-of-data/9781098108298/app02.html#ch01fn87-marker) Mark Haranas and Steven Burke, “Oracle Bests Cloud Rivals to Win Blockbuster Cloud Deal,” CRN, April 28, 2020, [_https://oreil.ly/LkqOi_](https://oreil.ly/LkqOi).
[3](https://learning.oreilly.com/library/view/fundamentals-of-data/9781098108298/app02.html#ch01fn88-marker) Corey Quinn, “Why Zoom Chose Oracle Cloud Over AWS and Maybe You Should Too,” Last Week in AWS, April 28, 2020, [_https://oreil.ly/Lx5uu_](https://oreil.ly/Lx5uu).