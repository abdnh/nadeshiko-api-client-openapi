# MediaInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path_image** | **str** |  | [optional] 
**path_audio** | **str** |  | [optional] 
**path_video** | **str** |  | [optional] 

## Example

```python
from nadeshiko_api_client.models.media_info import MediaInfo

# TODO update the JSON string below
json = "{}"
# create an instance of MediaInfo from a JSON string
media_info_instance = MediaInfo.from_json(json)
# print the JSON string representation of the object
print(MediaInfo.to_json())

# convert the object into a dict
media_info_dict = media_info_instance.to_dict()
# create an instance of MediaInfo from a dict
media_info_from_dict = MediaInfo.from_dict(media_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


