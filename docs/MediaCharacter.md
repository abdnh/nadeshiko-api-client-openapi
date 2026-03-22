# MediaCharacter

Character appearing in a media with their voice actor and role

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | AniList character ID | 
**name_ja** | **str** | Japanese name of the character | 
**name_en** | **str** | English name of the character | 
**image_url** | **str** | Character image URL | 
**seiyuu** | [**Seiyuu**](Seiyuu.md) |  | 
**role** | **str** | Character&#39;s role in the media | 

## Example

```python
from nadeshiko_api_client.models.media_character import MediaCharacter

# TODO update the JSON string below
json = "{}"
# create an instance of MediaCharacter from a JSON string
media_character_instance = MediaCharacter.from_json(json)
# print the JSON string representation of the object
print(MediaCharacter.to_json())

# convert the object into a dict
media_character_dict = media_character_instance.to_dict()
# create an instance of MediaCharacter from a dict
media_character_from_dict = MediaCharacter.from_dict(media_character_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


