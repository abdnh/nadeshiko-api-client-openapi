# SearchMultipleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | [**SearchMultipleRequestQuery**](SearchMultipleRequestQuery.md) |  | 
**filters** | [**SearchFilters**](SearchFilters.md) |  | [optional] 
**include** | [**List[IncludeExpansion]**](IncludeExpansion.md) | Resources to expand in the response includes block | [optional] [default to []]

## Example

```python
from nadeshiko_api_client.models.search_multiple_request import SearchMultipleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SearchMultipleRequest from a JSON string
search_multiple_request_instance = SearchMultipleRequest.from_json(json)
# print the JSON string representation of the object
print(SearchMultipleRequest.to_json())

# convert the object into a dict
search_multiple_request_dict = search_multiple_request_instance.to_dict()
# create an instance of SearchMultipleRequest from a dict
search_multiple_request_from_dict = SearchMultipleRequest.from_dict(search_multiple_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


