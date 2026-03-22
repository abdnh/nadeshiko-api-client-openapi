# Episode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**media_id** | **int** | ID of the media this episode belongs to | 
**episode_number** | **int** | Episode number within the media | 
**title_en** | **str** | English title of the episode | [optional] 
**title_romaji** | **str** | Romanized title of the episode | [optional] 
**title_ja** | **str** | Japanese title of the episode | [optional] 
**description** | **str** | Episode description or synopsis | [optional] 
**aired_at** | **datetime** | When the episode originally aired | [optional] 
**length_seconds** | **int** | Episode duration in seconds | [optional] 
**thumbnail_url** | **str** | URL to episode thumbnail image | [optional] 
**segment_count** | **int** | Number of segments in this episode | 

## Example

```python
from nadeshiko_api_client.models.episode import Episode

# TODO update the JSON string below
json = "{}"
# create an instance of Episode from a JSON string
episode_instance = Episode.from_json(json)
# print the JSON string representation of the object
print(Episode.to_json())

# convert the object into a dict
episode_dict = episode_instance.to_dict()
# create an instance of Episode from a dict
episode_from_dict = Episode.from_dict(episode_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


