# SearchFiltersSegmentDurationMs

Segment audio duration range filter (in milliseconds)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min** | **int** | Minimum duration in ms | [optional] 
**max** | **int** | Maximum duration in ms | [optional] 

## Example

```python
from nadeshiko_api_client.models.search_filters_segment_duration_ms import SearchFiltersSegmentDurationMs

# TODO update the JSON string below
json = "{}"
# create an instance of SearchFiltersSegmentDurationMs from a JSON string
search_filters_segment_duration_ms_instance = SearchFiltersSegmentDurationMs.from_json(json)
# print the JSON string representation of the object
print(SearchFiltersSegmentDurationMs.to_json())

# convert the object into a dict
search_filters_segment_duration_ms_dict = search_filters_segment_duration_ms_instance.to_dict()
# create an instance of SearchFiltersSegmentDurationMs from a dict
search_filters_segment_duration_ms_from_dict = SearchFiltersSegmentDurationMs.from_dict(search_filters_segment_duration_ms_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


