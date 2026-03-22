# SearchFilters

Search filters for narrowing segment results

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**media** | [**SearchFiltersMedia**](SearchFiltersMedia.md) |  | [optional] 
**category** | [**List[Category]**](Category.md) | Media category filter | [optional] [default to [ANIME, JDRAMA]]
**content_rating** | [**List[ContentRating]**](ContentRating.md) | Content ratings to include (omit for all ratings) | [optional] 
**status** | **List[str]** | Segment status filter | [optional] [default to [ACTIVE]]
**segment_length_chars** | [**SearchFiltersSegmentLengthChars**](SearchFiltersSegmentLengthChars.md) |  | [optional] 
**segment_duration_ms** | [**SearchFiltersSegmentDurationMs**](SearchFiltersSegmentDurationMs.md) |  | [optional] 
**languages** | [**SearchFiltersLanguages**](SearchFiltersLanguages.md) |  | [optional] 

## Example

```python
from nadeshiko_api_client.models.search_filters import SearchFilters

# TODO update the JSON string below
json = "{}"
# create an instance of SearchFilters from a JSON string
search_filters_instance = SearchFilters.from_json(json)
# print the JSON string representation of the object
print(SearchFilters.to_json())

# convert the object into a dict
search_filters_dict = search_filters_instance.to_dict()
# create an instance of SearchFilters from a dict
search_filters_from_dict = SearchFilters.from_dict(search_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


