# SegmentTextEn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** | English translation | 
**is_machine_translated** | **bool** | Whether the translation was machine-translated | 
**highlight** | **str** | English content with search terms highlighted | [optional] 

## Example

```python
from nadeshiko_api_client.models.segment_text_en import SegmentTextEn

# TODO update the JSON string below
json = "{}"
# create an instance of SegmentTextEn from a JSON string
segment_text_en_instance = SegmentTextEn.from_json(json)
# print the JSON string representation of the object
print(SegmentTextEn.to_json())

# convert the object into a dict
segment_text_en_dict = segment_text_en_instance.to_dict()
# create an instance of SegmentTextEn from a dict
segment_text_en_from_dict = SegmentTextEn.from_dict(segment_text_en_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


