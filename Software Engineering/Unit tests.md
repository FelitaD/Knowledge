---
tags: tech
aliases:
publish: true
sr-due: 2022-11-02
sr-interval: 15
sr-ease: 230
---

Typically 3 phases :
1. initialize small piece of application it wants to test
2. applies some stimulus on it
3. observe the results

or 

AAA pattern for writing unit tests :
-   The **Arrange** section of a unit test method initializes objects and sets the value of the data that is passed to the method under test.
-   The **Act** section invokes the method under test with the arranged parameters.
-   The **Assert** section verifies that the action of the method under test behaves as expected. For .NET, methods in the [Assert](https://docs.microsoft.com/en-us/dotnet/api/microsoft.visualstudio.testtools.unittesting.assert) class are often used for verification.
