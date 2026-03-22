# SearchFiltersSegmentLengthChars

Content character count range filter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min** | **int** | Minimum content length | [optional] 
**max** | **int** | Maximum content length | [optional] 

## Example

```python
from nadeshiko_api_client.models.search_filters_segment_length_chars import SearchFiltersSegmentLengthChars

# TODO update the JSON string below
json = "{}"
# create an instance of SearchFiltersSegmentLengthChars from a JSON string
search_filters_segment_length_chars_instance = SearchFiltersSegmentLengthChars.from_json(json)
# print the JSON string representation of the object
print(SearchFiltersSegmentLengthChars.to_json())

# convert the object into a dict
search_filters_segment_length_chars_dict = search_filters_segment_length_chars_instance.to_dict()
# create an instance of SearchFiltersSegmentLengthChars from a dict
search_filters_segment_length_chars_from_dict = SearchFiltersSegmentLengthChars.from_dict(search_filters_segment_length_chars_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


