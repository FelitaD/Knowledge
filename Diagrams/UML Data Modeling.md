
Data modeling says how to represent data for application. 

Data models example :
- Relational model - with design principles
- XML
- Database design model
	- A higher level-model is translated into the model implemented by the DBMS

# Higher-Level Database Design Model

Higher-level database design models examples :
- E/R Entity-Relationship Model
- UML Unified Modeling Language
	- Subset of data modeling

- Both are graphical
- Both can be translated to relations automatically

# 5 Concepts of UML Data Modeling

## Classes

Commonly, classes consist of a class name, class attributes and methods.
But in data modeling, classes will add a PK and drop methods :

Class in data modeling :
- class name
- class primary key
- class attributes
-> Relation

## Associations

Capture relationships between objects of 2 classes.

**Multiplicity of Associations** 
How many objects can be related to objects of another class.
- m .. * : related to any number (except 0)
- 0 .. n : related to possibly none and up to n
- 0 .. * : no restrictions to multiplicity
- 1 .. 1 : default - each object related to 1

**Types of relationships**
- one-to-one
- many-to-one
- many-to-many
- complete
	- every object must participate in the relationship
	- **`DEFAULT`** complete one-to-one : each object on the left has an association on the right and reversly 
	- complete one-to-many : each object on the left has an association with many on the right and each object on the right has multiple associations with objects on the left

## Associations Classes

**Example** 
Association : Student -*applied*-> College
We want to also add the date and decision to the association *applied*.
The way to do it is to add a construct : association classes.

Not possible in UML to add multiple associations between 2 objects.

**Eliminating Association Classes**
Unnecessary when 0..1 or 1..1 multiplicity

**Self-Association**
Student -*sibling*-> Student 
College -*branch*-> College

## Subclasses

Student subclasses with their additional attributes :
- Foreign student
	- country
- Domestic student
	- state
	- SSN
- AP student

**Terminology and properties of subclasses**

superclass / subclass - generalization / specialization

> Specialization constraints
> Rather than the usual cardinality/multiplicity symbols, the subclass association line is labeled with **specialization constraints**. Constraints are described along two dimensions: incomplete versus complete, and disjoint versus overlapping.

-   In an **incomplete** specialization, also called a **partial** specialization, only _some_ individuals of the parent class are specialized (that is, have unique attributes). Other individuals of the parent class have only the common attributes.
-   In a **complete** specialization, _all_ individuals of the parent class have one or more unique attributes that are not common to the generalized (parent) class.
-   In a **disjoint** specialization, also called an **exclusive** specialization, an individual of the parent class may be a member of _only one_ specialized subclass.
-   In an **overlapping** specialization, an individual of of the parent class may be a member of _more than one_ of the specialized subclasses.

## Composition & Aggregation

≠ Aggregation in SQL

### Composition

When objects of one class belong to objects of another class.

**Example**
College and Departments
Composition is a special type of association
Implicitly 1 to 1

### Aggregation
Open diamond : apartment belongs to one college or not at all.

![[asset-v1_StanfordOnline+SOE.YDB-MDL_THEORY0001+2T2020+type@asset+block@UMLModeling 1.pdf]]