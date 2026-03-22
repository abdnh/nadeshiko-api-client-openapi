# SegmentContextResponseIncludes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**media** | [**Dict[str, Media]**](Media.md) | Media objects keyed by mediaId | [optional] 

## Example

```python
from nadeshiko_api_client.models.segment_context_response_includes import SegmentContextResponseIncludes

# TODO update the JSON string below
json = "{}"
# create an instance of SegmentContextResponseIncludes from a JSON string
segment_context_response_includes_instance = SegmentContextResponseIncludes.from_json(json)
# print the JSON string representation of the object
print(SegmentContextResponseIncludes.to_json())

# convert the object into a dict
segment_context_response_includes_dict = segment_context_response_includes_instance.to_dict()
# create an instance of SegmentContextResponseIncludes from a dict
segment_context_response_includes_from_dict = SegmentContextResponseIncludes.from_dict(segment_context_response_includes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


