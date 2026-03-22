# OpaqueCursorPagination

Opaque cursor pagination metadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_more** | **bool** | Whether more results are available | 
**cursor** | **str** | Opaque token for the next page (&#x60;null&#x60; when &#x60;hasMore&#x60; is &#x60;false&#x60;) | 

## Example

```python
from nadeshiko_api_client.models.opaque_cursor_pagination import OpaqueCursorPagination

# TODO update the JSON string below
json = "{}"
# create an instance of OpaqueCursorPagination from a JSON string
opaque_cursor_pagination_instance = OpaqueCursorPagination.from_json(json)
# print the JSON string representation of the object
print(OpaqueCursorPagination.to_json())

# convert the object into a dict
opaque_cursor_pagination_dict = opaque_cursor_pagination_instance.to_dict()
# create an instance of OpaqueCursorPagination from a dict
opaque_cursor_pagination_from_dict = OpaqueCursorPagination.from_dict(opaque_cursor_pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


