# SearchResponseIncludes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**media** | [**Dict[str, Media]**](Media.md) | Media objects keyed by media publicId | 

## Example

```python
from nadeshiko_api_client.models.search_response_includes import SearchResponseIncludes

# TODO update the JSON string below
json = "{}"
# create an instance of SearchResponseIncludes from a JSON string
search_response_includes_instance = SearchResponseIncludes.from_json(json)
# print the JSON string representation of the object
print(SearchResponseIncludes.to_json())

# convert the object into a dict
search_response_includes_dict = search_response_includes_instance.to_dict()
# create an instance of SearchResponseIncludes from a dict
search_response_includes_from_dict = SearchResponseIncludes.from_dict(search_response_includes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


