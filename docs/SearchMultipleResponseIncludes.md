# SearchMultipleResponseIncludes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**media** | [**Dict[str, Media]**](Media.md) | Media objects keyed by mediaId | 

## Example

```python
from nadeshiko_api_client.models.search_multiple_response_includes import SearchMultipleResponseIncludes

# TODO update the JSON string below
json = "{}"
# create an instance of SearchMultipleResponseIncludes from a JSON string
search_multiple_response_includes_instance = SearchMultipleResponseIncludes.from_json(json)
# print the JSON string representation of the object
print(SearchMultipleResponseIncludes.to_json())

# convert the object into a dict
search_multiple_response_includes_dict = search_multiple_response_includes_instance.to_dict()
# create an instance of SearchMultipleResponseIncludes from a dict
search_multiple_response_includes_from_dict = SearchMultipleResponseIncludes.from_dict(search_multiple_response_includes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


