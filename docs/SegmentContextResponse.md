# SegmentContextResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**segments** | [**List[Segment]**](Segment.md) |  | 
**includes** | [**SegmentContextResponseIncludes**](SegmentContextResponseIncludes.md) |  | 

## Example

```python
from nadeshiko_api_client.models.segment_context_response import SegmentContextResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SegmentContextResponse from a JSON string
segment_context_response_instance = SegmentContextResponse.from_json(json)
# print the JSON string representation of the object
print(SegmentContextResponse.to_json())

# convert the object into a dict
segment_context_response_dict = segment_context_response_instance.to_dict()
# create an instance of SegmentContextResponse from a dict
segment_context_response_from_dict = SegmentContextResponse.from_dict(segment_context_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


