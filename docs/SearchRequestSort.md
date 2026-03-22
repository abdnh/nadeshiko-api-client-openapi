# SearchRequestSort

Sort configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** | Sort mode | [optional] [default to 'NONE']
**seed** | **int** | Non-negative integer seed for deterministic random sorting (only used when mode is RANDOM) | [optional] 

## Example

```python
from nadeshiko_api_client.models.search_request_sort import SearchRequestSort

# TODO update the JSON string below
json = "{}"
# create an instance of SearchRequestSort from a JSON string
search_request_sort_instance = SearchRequestSort.from_json(json)
# print the JSON string representation of the object
print(SearchRequestSort.to_json())

# convert the object into a dict
search_request_sort_dict = search_request_sort_instance.to_dict()
# create an instance of SearchRequestSort from a dict
search_request_sort_from_dict = SearchRequestSort.from_dict(search_request_sort_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


