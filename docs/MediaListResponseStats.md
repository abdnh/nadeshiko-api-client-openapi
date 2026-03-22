# MediaListResponseStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_media** | **int** | Total number of media across all pages | 
**total_segments** | **int** | Total number of non-deleted segments | 
**total_episodes** | **int** | Total number of episodes | 

## Example

```python
from nadeshiko_api_client.models.media_list_response_stats import MediaListResponseStats

# TODO update the JSON string below
json = "{}"
# create an instance of MediaListResponseStats from a JSON string
media_list_response_stats_instance = MediaListResponseStats.from_json(json)
# print the JSON string representation of the object
print(MediaListResponseStats.to_json())

# convert the object into a dict
media_list_response_stats_dict = media_list_response_stats_instance.to_dict()
# create an instance of MediaListResponseStats from a dict
media_list_response_stats_from_dict = MediaListResponseStats.from_dict(media_list_response_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


