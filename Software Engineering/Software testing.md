
Cf : [[Data pipeline tests]]
Fixtures : ensure specified environnement for a single test, supported by Pytest

### Types of tests

#### [[Unit tests]] 

- close to the source code
- individual functions
- cheap and run by continuous integration server

#### Integration tests

- interaction of modules and services
- more expensive since more components running
- eg. can connect to a database

#### Functional tests

- verify the output of an action and not intermediate states of the system
- eg. database returns certain value

#### End-to-end tests

- replicates user behaviour
- eg. logging, email notifications...

#### Performance tests

- evaluates how system performs under particular a workload
- measure reliability, speed, scalability, responsiveness

#### Smoke tests

- basic tests to check basic functionality
- usually right after a build or deployment

