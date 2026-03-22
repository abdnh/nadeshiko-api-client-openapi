# Media

Media entry with full metadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Internal unique identifier for the media | 
**public_id** | **str** | Public identifier for the media (use this in public URLs) | 
**external_ids** | [**ExternalId**](ExternalId.md) |  | 
**name_ja** | **str** | Original Japanese name of the media | 
**name_romaji** | **str** | Romaji transliteration of the media name | 
**name_en** | **str** | English name of the media | 
**airing_format** | **str** | Format of the media release (e.g., TV, OVA, Movie) | 
**airing_status** | **str** | Current airing status (FINISHED, RELEASING, NOT_YET_RELEASED, CANCELLED) | 
**genres** | **List[str]** | List of genres associated with the media | 
**cover_url** | **str** | Full URL to the cover image | 
**banner_url** | **str** | Full URL to the banner image | 
**start_date** | **date** | Start date of the media (first airing/release) | 
**end_date** | **date** | End date of the media (last airing/release) | [optional] 
**category** | [**Category**](Category.md) |  | 
**segment_count** | **int** | Total number of subtitle segments available | 
**episode_count** | **int** | Total number of episodes available | 
**studio** | **str** | Animation studio that produced the media | [optional] 
**season_name** | **str** | Airing season label for the media | 
**season_year** | **int** | Airing year for the media | 
**characters** | [**List[MediaCharacter]**](MediaCharacter.md) | Characters appearing in the media with their voice actors | [optional] 

## Example

```python
from nadeshiko_api_client.models.media import Media

# TODO update the JSON string below
json = "{}"
# create an instance of Media from a JSON string
media_instance = Media.from_json(json)
# print the JSON string representation of the object
print(Media.to_json())

# convert the object into a dict
media_dict = media_instance.to_dict()
# create an instance of Media from a dict
media_from_dict = Media.from_dict(media_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


