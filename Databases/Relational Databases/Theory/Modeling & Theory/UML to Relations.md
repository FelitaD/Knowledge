Learn about  translating designs in the UML language into relational schemas.

The interest is the translator between the higher-level design language and DBMS model.

**Translations UML -> Relations**
- Classes 
	- the translation is very direct, turn sideways
- Associations
	- Association becomes 1 relation with an attribute of each relations (d'où association table)
	- Depending on the multiplicity of relationship
		- Eg. with K2 being a key for A
		- No association table needed when 0..1 or 0..0 we can add the key from this relation to the other table
- Association Classes
	- Extend the association relation to include association attributes
	- Self-Associations
		- Create different names like id_1 and id_2
- Subclasses
	- 3 cases of translation :
		1. Subclass relations contain superclass key + specialized attributes S(K, A), S1(K, B), S2(K, C)
		2. Subclass relations contain all attributes S(K, A), S1(K, A, B), S2(K, A, C)
		3. One relation containing all superclass + subclass attributes S(K, A, B, C)
	- Best depends on the properties of the subclass relationship (overlapping / disjoint, complete / incomplete)
		- heavily {overlapping} -> design 3 because capture all attributes together and we could see directly rather than assembling all the different pieces
		- {disjoint, complete} -> design 2 puts each object in its own class
- Composition & Aggregation
	- The component will just contain the key of the object it's composed from. Eg. College(cName, state), Department(dName, building, cName)
	- 























![[StanfordOnlineSOE.YDB-UML0001-V000200_DTH.mp4]]![[09-02-uml-to-relations-part2.mp4]]
![[09-02-uml-to-relations-part3.mp4]]

![[asset-v1_StanfordOnline+SOE.YDB-MDL_THEORY0001+2T2020+type@asset+block@UMLRelations.pdf]]