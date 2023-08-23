## Documentation

- Documentation is essential for an analytics team to work effectively and efficiently. Strong documentation empowers users to self-service questions about data and enables new team members to on-board quickly.
- Documentation often lags behind the code it is meant to describe. This can happen because documentation is a separate process from the coding itself that lives in another tool.
- Therefore, documentation should be as automated as possible and happen as close as possible to the coding.
- In dbt, models are built in SQL files. These models are documented in YML files that live in the same folder as the models.

## Writing documentation and doc blocks

- Documentation of models occurs in the YML files (where generic tests also live) inside the models directory. It is helpful to store the YML file in the same subfolder as the models you are documenting.
- For models, descriptions can happen at the model, source, or column level.
- If a longer form, more styled version of text would provide a strong description, **doc blocks** can be used to render markdown in the generated documentation.

```
{% docs order_status %}                        
  
| status         | definition                                       | |----------------|--------------------------------------------------| | placed         | Order placed, not yet shipped                    | | shipped        | Order has been shipped, not yet been delivered   | | completed      | Order has been received by customers             | | return pending | Customer indicated they want to return this item | | returned       | Item has been returned                           |
{% enddocs %}
```
```
- name: status
  description: "{{ doc('order_status') }}"
```

## Generating and viewing documentation

- In the command line section, an updated version of documentation can be generated through the command `dbt docs generate`. This will refresh the `view docs` link in the top left corner of the Cloud IDE.
- The generated documentation includes the following:
    - Lineage Graph
    - Model, source, and column descriptions
    - Generic tests added to a column
    - The underlying SQL code for each model
    - and more...