[[Fundamentals of DE - OReilly]] << | >> [[Chapter 1. Data Engineering Described]]

# Preface

How did this book come about? The origin is deeply rooted in our journey from data science into data engineering. We often jokingly refer to ourselves as _recovering data scientists_. We both had the experience of being assigned to data science projects, then struggling to execute these projects due to a lack of proper foundations. Our journey into data engineering began when we undertook data engineering tasks to build foundations and infrastructure.

With the rise of data science, companies splashed out lavishly on data science talent, hoping to reap rich rewards. Very often, data scientists struggled with basic problems that their background and training did not address—data collection, data cleansing, data access, data transformation, and data infrastructure. These are problems that data engineering aims to solve.

# What This Book Isn’t

Before we cover what this book is about and what you’ll get out of it, let’s quickly cover what this book _isn’t_. This book isn’t about data engineering using a particular tool, technology, or platform. While many excellent books approach data engineering technologies from this perspective, these books have a short shelf life. Instead, we focus on the fundamental concepts behind data engineering.

# What This Book Is About

This book aims to fill a gap in current data engineering content and materials. While there’s no shortage of technical resources that address specific data engineering tools and technologies, people struggle to understand how to assemble these components into a coherent whole that applies in the real world. This book connects the dots of the end-to-end data lifecycle. It shows you how to stitch together various technologies to serve the needs of downstream data consumers such as analysts, data scientists, and machine learning engineers. This book works as a complement to O’Reilly books that cover the details of particular technologies, platforms, and programming languages.

The big idea of this book is the _data engineering lifecycle_: data generation, storage, ingestion, transformation, and serving. Since the dawn of data, we’ve seen the rise and fall of innumerable specific technologies and vendor products, but the data engineering lifecycle stages have remained essentially unchanged. With this framework, the reader will come away with a sound understanding for applying technologies to real-world business problems.

Our goal here is to map out principles that reach across two axes. First, we wish to distill data engineering into principles that can encompass _any relevant technology_. Second, we wish to present principles that will stand the test of _time_. We hope that these ideas reflect lessons learned across the data technology upheaval of the last twenty years and that our mental framework will remain useful for a decade or more into the future.

One thing to note: we unapologetically take a cloud-first approach. We view the cloud as a fundamentally transformative development that will endure for decades; most on-premises data systems and workloads will eventually move to cloud hosting. We assume that infrastructure and systems are _ephemeral_ and _scalable_, and that data engineers will lean toward deploying managed services in the cloud. That said, most concepts in this book will translate to non-cloud environments.

# Who Should Read This Book

Our primary intended audience for this book consists of technical practitioners, mid- to senior-level software engineers, data scientists, or analysts interested in moving into data engineering; or data engineers working in the guts of specific technologies, but wanting to develop a more comprehensive perspective. Our secondary target audience consists of data stakeholders who work adjacent to technical practitioners—e.g., a data team lead with a technical background overseeing a team of data engineers, or a director of data warehousing wanting to migrate from on-premises technology to a cloud-based solution.

Ideally, you’re curious and want to learn—why else would you be reading this book? You stay current with data technologies and trends by reading books and articles on data warehousing/data lakes, batch and streaming systems, orchestration, modeling, management, analysis, developments in cloud technologies, etc. This book will help you weave what you’ve read into a complete picture of data engineering across technologies and paradigms.

# Prerequisites

We assume a good deal of familiarity with the types of data systems found in a corporate setting. In addition, we assume that readers have some familiarity with SQL and Python (or some other programming language), and experience with cloud services.

Numerous resources are available for aspiring data engineers to practice Python and SQL. Free online resources abound (blog posts, tutorial sites, YouTube videos), and many new Python books are published every year.

The cloud provides unprecedented opportunities to get hands-on experience with data tools. We suggest that aspiring data engineers set up accounts with cloud services such as AWS, Azure, Google Cloud Platform, Snowflake, Databricks, etc. Note that many of these platforms have _free tier_ options, but readers should keep a close eye on costs and work with small quantities of data and single node clusters as they study.

Developing familiarity with corporate data systems outside of a corporate environment remains difficult, and this creates certain barriers for aspiring data engineers who have yet to land their first data job. This book can help. We suggest that data novices read for high-level ideas and then look at materials in the Additional Resources section at the end of each chapter. On a second read through, note any unfamiliar terms and technologies. You can utilize Google, Wikipedia, blog posts, YouTube videos, and vendor sites to become familiar with new terms and fill gaps in your understanding.

# What You’ll Learn and How It Will Improve Your Abilities

This book aims to help you build a solid foundation for solving real-world data engineering problems.

By the end of this book you will understand:

-   How data engineering impacts your current role (data scientist, software engineer, or data team lead)
-   How to cut through the marketing hype and choose the right technologies, data architecture, and processes
-   How to use the data engineering lifecycle to design and build a robust architecture
-   Best practices for each stage of the data lifecycle

And you will be able to:

-   Incorporate data engineering principles in your current role (data scientist, analyst, software engineer, data team lead, etc.)
-   Stitch together a variety of cloud technologies to serve the needs of downstream data consumers
-   Assess data engineering problems with an end-to-end framework of best practices
-   Incorporate data governance and security across the data engineering lifecycle

# Navigating This Book

This book is composed of four parts:

-   [Part I, “Foundation and Building Blocks”](https://learning.oreilly.com/library/view/fundamentals-of-data/9781098108298/part01.html#part1)
-   [Part II, “The Data Engineering Lifecycle in Depth”](https://learning.oreilly.com/library/view/fundamentals-of-data/9781098108298/part02.html#part2)
-   [Part III, “Security, Privacy, and the Future of Data Engineering”](https://learning.oreilly.com/library/view/fundamentals-of-data/9781098108298/part03.html#part3)
-   Appendices [A](https://learning.oreilly.com/library/view/fundamentals-of-data/9781098108298/app01.html#a_serialization_and_compression_technic) and [B](https://learning.oreilly.com/library/view/fundamentals-of-data/9781098108298/app02.html#b_cloud_networking): covering serialization and compression, and cloud networking, respectively

In [Part I](https://learning.oreilly.com/library/view/fundamentals-of-data/9781098108298/part01.html#part1), we begin by defining data engineering in [Chapter 1](https://learning.oreilly.com/library/view/fundamentals-of-data/9781098108298/ch01.html#data_engineering_described), then map out the data engineering lifecycle in [Chapter 2](https://learning.oreilly.com/library/view/fundamentals-of-data/9781098108298/ch02.html#the_data_engineering_lifecycle-id000095). In [Chapter 3](https://learning.oreilly.com/library/view/fundamentals-of-data/9781098108298/ch03.html#designing_good_data_architecture), we discuss _good architecture_. In [Chapter 4](https://learning.oreilly.com/library/view/fundamentals-of-data/9781098108298/ch04.html#choosing_technologies_across_the_data_e), we introduce a framework for choosing the right technology—while we frequently see technology and architecture conflated, these are in fact very different topics.

[Part II](https://learning.oreilly.com/library/view/fundamentals-of-data/9781098108298/part02.html#part2) builds on [Chapter 2](https://learning.oreilly.com/library/view/fundamentals-of-data/9781098108298/ch02.html#the_data_engineering_lifecycle-id000095) to cover the data engineering lifecycle in depth; each lifecycle stage—data generation, storage, ingestion, transformation and serving—is covered in its own chapter. [Part II](https://learning.oreilly.com/library/view/fundamentals-of-data/9781098108298/part02.html#part2) is arguably the heart of the book, and the other chapters exist to support the core ideas covered here.

[Part III](https://learning.oreilly.com/library/view/fundamentals-of-data/9781098108298/part03.html#part3) covers additional topics. In [Chapter 10](https://learning.oreilly.com/library/view/fundamentals-of-data/9781098108298/ch10.html#security_and_privacy), we discuss _security and privacy_. While security has always been an important part of the data engineering profession, it has only become more critical with the rise of for profit hacking and state sponsored cyber attacks. And what can we say of privacy? The era of corporate privacy nihilism is over—no company wants to see its name appear in the headline of an article on sloppy privacy practices. Reckless handling of personal data can also have significant legal ramifications with the advent of GDPR, CCPA, and other regulations. In short, security and privacy must be top priorities in any data engineering work.

In the course of working in data engineering, doing research for this book and interviewing numerous experts, we thought a good deal about where the field is going in the near and long term. [Chapter 11](https://learning.oreilly.com/library/view/fundamentals-of-data/9781098108298/ch11.html#the_future_of_data_engineering) outlines our highly speculative ideas on the future of data engineering. By its nature, the future is a slippery thing. Time will tell if some of our ideas are correct. We would love to hear from our readers on how their visions of the future agree with or differ from our own.

In the appendices, we cover a handful of technical topics that are extremely relevant to the day-to-day practice of data engineering but didn’t fit into the main body of the text. Specifically, engineers need to understand serialization and compression (see [Appendix A](https://learning.oreilly.com/library/view/fundamentals-of-data/9781098108298/app01.html#a_serialization_and_compression_technic)) both to work directly with data files and to assess performance considerations in data systems, and cloud networking (see [Appendix B](https://learning.oreilly.com/library/view/fundamentals-of-data/9781098108298/app02.html#b_cloud_networking)) is a critical topic as data engineering shifts into the cloud.