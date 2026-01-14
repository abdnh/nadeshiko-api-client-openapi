# Statistic


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anime_id** | **int** |  | [optional] 
**category** | **int** |  | [optional] 
**name_anime_romaji** | **str** |  | [optional] 
**name_anime_en** | **str** |  | [optional] 
**name_anime_jp** | **str** |  | [optional] 
**amount_sentences_found** | **int** |  | [optional] 
**season_with_episode_hits** | **Dict[str, Dict[str, int]]** |  | [optional] 

## Example

```python
from nadeshiko_api_client.models.statistic import Statistic

# TODO update the JSON string below
json = "{}"
# create an instance of Statistic from a JSON string
statistic_instance = Statistic.from_json(json)
# print the JSON string representation of the object
print(Statistic.to_json())

# convert the object into a dict
statistic_dict = statistic_instance.to_dict()
# create an instance of Statistic from a dict
statistic_from_dict = Statistic.from_dict(statistic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


