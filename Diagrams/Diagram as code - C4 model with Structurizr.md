---
tags: 
- tech
- software-development
---
Software architecture diagrams from a text based definition.

# C4 model

[Make models not diagrams](https://dev.to/simonbrown/modelling-software-architecture-with-plantuml-56fc)
[Structurizr](https://github.com/structurizr/dsl) : uses the DSL language to create models that is software agnostic (Mermaid, PlantUML...) and also uses the [C4 model](https://c4model.com/)
4 levels of abstraction : Overview first, zoom and filter, provide details

## 1. System Context
- Users
- System dependencies
## 2. Containers
≠ docker containers
- Architecture's shape
- Technologies
## 3. Components
- Logical components
- Interactions
## 4. Code
- Implementation (classes...)

![[Pasted image 20221018180259.png]]

# Structurizr DSL 

Tool to define the 4 levels of abstraction in one place (avoid repetition).

Workspace : wrapper for software architecture model
Workspace extension : reuse elements accross workspaces

Views :
- System context view : big picture
- Container view : applications and data stores that reside in software system
- Component view : 
- Filtered view : to include exclude tags and show present vs future version for example
- Dynamic view : 

# Structurizr CLI

`structurizr-cli push -id 79499 -key cf87dcc0-e88c-44d1-9da2-3863ebf341fb -secret 8ad49168-e0d6-40e7-b1df-2b9a1cf77e8e -workspace workspace.dsl`

# Resources

eBook : https://leanpub.com/visualising-software-architecture/read_sample
Cookbook : https://github.com/structurizr/dsl/tree/master/docs/cookbook
Language reference : https://github.com/structurizr/dsl/blob/master/docs/language-reference.md#workspace
Conference : https://www.youtube.com/watch?v=x2-rSnhpw0g&ab_channel=AgileontheBeach