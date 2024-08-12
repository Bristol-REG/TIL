# Exceptions aren't always errors

Exceptions aren't always errors, in general they're just unusual paths through code. e.g.

```python
for item in my_list:
    try:
        fast_algorithm(item)
    except ZeroDivisionError as e:
        # The fast version hasn't worked, but this is expected to happen occasionally
        # Let's fall back on our safe algorithm
        slow_but_safe_algorithm(item)

        logger.warning(f"{item} caused {e}")
```

You could imagine another usecase where you want to just ignore the error, or do something like ignore a keyboard interrupt.

Python also has `warnings`, it's a builtin library with special exceptions in it for warnings.

In general people tend to ask forgiveness rather than permission with respect to exceptions. It's not like C++ where raising and catching exceptions is slow and annoying.

Via: [Richard](https://github.com/richard-lane)
