# MediaSearchStats

Search hit statistics for a single media

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**media_id** | **int** | Media identifier (look up full details in includes.media) | 
**public_id** | **str** | Public identifier for use in URLs and filters | 
**match_count** | **int** | Number of matching segments found in this media | 
**episode_hits** | **Dict[str, int]** | Mapping of episode numbers to segment hit counts | 

## Example

```python
from nadeshiko_api_client.models.media_search_stats import MediaSearchStats

# TODO update the JSON string below
json = "{}"
# create an instance of MediaSearchStats from a JSON string
media_search_stats_instance = MediaSearchStats.from_json(json)
# print the JSON string representation of the object
print(MediaSearchStats.to_json())

# convert the object into a dict
media_search_stats_dict = media_search_stats_instance.to_dict()
# create an instance of MediaSearchStats from a dict
media_search_stats_from_dict = MediaSearchStats.from_dict(media_search_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


