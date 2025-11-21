Copy page

About doc function
==================

The `doc` function is used to reference docs blocks in the description field of schema.yml files. It is analogous to the `ref` function. For more information, consult the [Documentation guide](/docs/explore/build-and-view-your-docs).

Usage:

orders.md

```
{% docs orders %}  
  
# docs  
- go  
- here  
   
{% enddocs %}
```

schema.yml

```
models:  
  - name: orders  
    description: "{{ doc('orders') }}"
```