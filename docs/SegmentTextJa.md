# SegmentTextJa


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** | Original Japanese content | 
**highlight** | **str** | Japanese content with search terms highlighted | [optional] 
**tokens** | [**List[Token]**](Token.md) | Morphological tokens for interactive display (Labs feature) | [optional] 

## Example

```python
from nadeshiko_api_client.models.segment_text_ja import SegmentTextJa

# TODO update the JSON string below
json = "{}"
# create an instance of SegmentTextJa from a JSON string
segment_text_ja_instance = SegmentTextJa.from_json(json)
# print the JSON string representation of the object
print(SegmentTextJa.to_json())

# convert the object into a dict
segment_text_ja_dict = segment_text_ja_instance.to_dict()
# create an instance of SegmentTextJa from a dict
segment_text_ja_from_dict = SegmentTextJa.from_dict(segment_text_ja_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


