# SearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | [**SearchRequestQuery**](SearchRequestQuery.md) |  | [optional] 
**take** | **int** | Max amount of entries by response | [optional] [default to 10]
**cursor** | **str** | Opaque cursor token returned from the previous search page | [optional] 
**sort** | [**SearchRequestSort**](SearchRequestSort.md) |  | [optional] 
**filters** | [**SearchFilters**](SearchFilters.md) |  | [optional] 
**include** | [**List[IncludeExpansion]**](IncludeExpansion.md) | Resources to expand in the response includes block | [optional] [default to [media]]

## Example

```python
from nadeshiko_api_client.models.search_request import SearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SearchRequest from a JSON string
search_request_instance = SearchRequest.from_json(json)
# print the JSON string representation of the object
print(SearchRequest.to_json())

# convert the object into a dict
search_request_dict = search_request_instance.to_dict()
# create an instance of SearchRequest from a dict
search_request_from_dict = SearchRequest.from_dict(search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


