# EpisodeListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**episodes** | [**List[Episode]**](Episode.md) | Array of episode objects | 
**pagination** | [**OpaqueCursorPagination**](OpaqueCursorPagination.md) |  | 

## Example

```python
from nadeshiko_api_client.models.episode_list_response import EpisodeListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EpisodeListResponse from a JSON string
episode_list_response_instance = EpisodeListResponse.from_json(json)
# print the JSON string representation of the object
print(EpisodeListResponse.to_json())

# convert the object into a dict
episode_list_response_dict = episode_list_response_instance.to_dict()
# create an instance of EpisodeListResponse from a dict
episode_list_response_from_dict = EpisodeListResponse.from_dict(episode_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


