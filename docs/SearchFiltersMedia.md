# SearchFiltersMedia

Media inclusion/exclusion filters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include** | [**List[MediaFilterItem]**](MediaFilterItem.md) | Include only segments from these media (with optional episode filter) | [optional] 
**exclude** | [**List[MediaFilterItem]**](MediaFilterItem.md) | Exclude segments from these media (with optional episode filter) | [optional] 

## Example

```python
from nadeshiko_api_client.models.search_filters_media import SearchFiltersMedia

# TODO update the JSON string below
json = "{}"
# create an instance of SearchFiltersMedia from a JSON string
search_filters_media_instance = SearchFiltersMedia.from_json(json)
# print the JSON string representation of the object
print(SearchFiltersMedia.to_json())

# convert the object into a dict
search_filters_media_dict = search_filters_media_instance.to_dict()
# create an instance of SearchFiltersMedia from a dict
search_filters_media_from_dict = SearchFiltersMedia.from_dict(search_filters_media_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


