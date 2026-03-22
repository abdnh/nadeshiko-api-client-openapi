# SearchMultipleResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[WordMatch]**](WordMatch.md) |  | 
**includes** | [**SearchMultipleResponseIncludes**](SearchMultipleResponseIncludes.md) |  | 

## Example

```python
from nadeshiko_api_client.models.search_multiple_response import SearchMultipleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SearchMultipleResponse from a JSON string
search_multiple_response_instance = SearchMultipleResponse.from_json(json)
# print the JSON string representation of the object
print(SearchMultipleResponse.to_json())

# convert the object into a dict
search_multiple_response_dict = search_multiple_response_instance.to_dict()
# create an instance of SearchMultipleResponse from a dict
search_multiple_response_from_dict = SearchMultipleResponse.from_dict(search_multiple_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


