# ExternalId

Map of external IDs keyed by source. Only sources with values are included.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anilist** | **str** | AniList ID | [optional] 
**imdb** | **str** | IMDB ID | [optional] 
**tvdb** | **str** | TVDB ID | [optional] 
**tmdb** | **str** | TMDB ID | [optional] 

## Example

```python
from nadeshiko_api_client.models.external_id import ExternalId

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalId from a JSON string
external_id_instance = ExternalId.from_json(json)
# print the JSON string representation of the object
print(ExternalId.to_json())

# convert the object into a dict
external_id_dict = external_id_instance.to_dict()
# create an instance of ExternalId from a dict
external_id_from_dict = ExternalId.from_dict(external_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


