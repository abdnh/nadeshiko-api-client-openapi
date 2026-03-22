# MediaListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**media** | [**List[Media]**](Media.md) |  | 
**pagination** | [**OpaqueCursorPagination**](OpaqueCursorPagination.md) |  | 
**stats** | [**MediaListResponseStats**](MediaListResponseStats.md) |  | 

## Example

```python
from nadeshiko_api_client.models.media_list_response import MediaListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MediaListResponse from a JSON string
media_list_response_instance = MediaListResponse.from_json(json)
# print the JSON string representation of the object
print(MediaListResponse.to_json())

# convert the object into a dict
media_list_response_dict = media_list_response_instance.to_dict()
# create an instance of MediaListResponse from a dict
media_list_response_from_dict = MediaListResponse.from_dict(media_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


