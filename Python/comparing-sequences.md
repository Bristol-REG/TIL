# Comparing sequences is automatically element-by-element

You can compare two sequences of the same type in Python, which checks them element-by-element and makes a decision based on the first value that is different in the two sequences.

The following example uses `tuple`s:

```python
>>> (1, 2, 3) < (1, 2, 4)
True

>>> (1, 2, 3) == (1.0, 2.0, 3.0)
True

>>> (1, 2, 3) == (1.0, 2.0, 4.0)
False
```

This is very useful for sorting things where you want to sort by one thing, then another thing if there is a tie:

```python
# adapted from the Python sorting docs

student_tuples = [
    ('john', 'A', 15),  # name, class, age
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]

# sort by class, age (descending), then name
sorted(student_tuples, key=lambda student: (student[1], -student[2], student[0]))

# ^ you would normally use something nicer than tuples for data like this, but hopefully useful as an example
```

Via: [Richard](https://github.com/richard-lane) and [James](https://github.com/jatonline)
