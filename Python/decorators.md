# Python decorators (the @things before functions)

Python decorators are things like `@decorator_name` that you sometimes see before function definitions.

They can be really useful for things like:

- [timing your function](https://stackoverflow.com/a/27737385) to see how long it takes to run
- [caching the output from a function](https://docs.python.org/3/library/functools.html#functools.cache) so it runs more quickly the second time
- [retrying web/API calls](https://tenacity.readthedocs.io) if they go wrong or timeout
- [logging](https://calmcode.io/course/pandas-pipe/logs) stages of a pipeline
- modifying the input/output from the function

They are quite a thing to get your head around at first, but if you remember that a decorator is "a function that you pass a function to, that then returns another function" along with the following example, then you have most of the mental model already:

```python
# This code...
@my_decorator
def my_function():
   print("hello")

# is EXACTLY the same as this code...
def my_function():
   print("hello")
my_function = my_decorator(my_function)

# (my_decorator replaces the my_function variable with a modified function)
```

For some more examples, see:
- https://calmcode.io/course/decorators
- https://realpython.com/primer-on-python-decorators/
