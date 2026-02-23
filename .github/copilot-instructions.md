---
applyTo: "geotab-downloader/**/*.py, backend/**/*.py"
---

# Code Style

## Let it crash

### Exceptions
Don't write code to catch exceptions that you can't handle. If you don't know how to handle an exception, let it crash and let the developer fix the underlying issue rather than hiding it.

### Accessing dict fields
If some field is expected to always be present, just access it directly instead of `dict.get`.

If the field is missing, it will raise a KeyError, which is good because it indicates a bug in the code that needs to be fixed, rather than silently returning None and potentially causing more subtle bugs down the line.

If you are not sure if the field will always be present, then use `dict.get`.

## Avoid redundant comments

We are all experienced developers here.

Redundant comments that just restate what the code is doing are not helpful. They just add noise.

This is bad:
```python
# Get device from geotab API
def get_device_from_geotab_api(api_client, device_id):
    api.client(...)
```

Also bad:
```python
def get_device_from_geotab_api(api_client, device_id):
    """Get device from geotab API.
    """
    api.client(...)
```
## Keep try blocks minimal

Only include the code that might raise an exception in a try block. This makes it easier to identify the source of errors and prevents catching exceptions from unrelated code.

This is bad:
```python
try:
    this_may_raise_FooException()
    something_unrelated_to_the_exception()
except FooException:
    # handle the exception
```

This is better:
```python
try:
    this_may_raise_FooException()
except FooException:
    # handle the exception
something_unrelated_to_the_exception()
```

This is also OK:
```python
try:
    this_may_raise_FooException()
except FooException:
    # handle the exception
else:
    something_unrelated_to_the_exception()
```

## Follow PEP 8

Do it.

## Software development principles

- YAGNI (I tend to over-engineer, account for this)
- KISS (don't be clever, be clear)
- other best practices that you know and follow
