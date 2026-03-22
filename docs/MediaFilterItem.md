# MediaFilterItem

A media filter entry with optional episode restriction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**media_id** | **str** | Media identifier (publicId or AniList external ID) | 
**episodes** | **List[int]** | Specific episodes (omit for all episodes) | [optional] 

## Example

```python
from nadeshiko_api_client.models.media_filter_item import MediaFilterItem

# TODO update the JSON string below
json = "{}"
# create an instance of MediaFilterItem from a JSON string
media_filter_item_instance = MediaFilterItem.from_json(json)
# print the JSON string representation of the object
print(MediaFilterItem.to_json())

# convert the object into a dict
media_filter_item_dict = media_filter_item_instance.to_dict()
# create an instance of MediaFilterItem from a dict
media_filter_item_from_dict = MediaFilterItem.from_dict(media_filter_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


