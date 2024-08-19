# Function arguments that can only be used a keywords, not positional arguments

You can define a keyword-only function in python by using a `*` (everything afterwards will be keyword-only). This can make the meaning of function arguments much clearer, compare:

```python
my_function(my_data, False, 4, 16, None)
```

and:

```python
my_function(my_data, shuffle=False, num_workers=4, batch_size=16, output_file=None)
```

You'd define this as:

```python
def my_function(my_data, *, shuffle, num_workers, batch_size, output_file):
    ...
```

You can also have [positional-only arguments](https://peps.python.org/pep-0570/), but you probably don't need to do that.

Via: [Richard](https://github.com/richard-lane)
