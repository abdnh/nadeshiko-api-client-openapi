# SegmentInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**uuid** | **str** |  | [optional] 
**position** | **int** |  | [optional] 
**start_time** | **str** |  | [optional] 
**end_time** | **str** |  | [optional] 
**content_jp** | **str** |  | [optional] 
**content_jp_highlight** | **str** |  | [optional] 
**content_en** | **str** |  | [optional] 
**content_en_highlight** | **str** |  | [optional] 
**content_en_mt** | **bool** |  | [optional] 
**content_es** | **str** |  | [optional] 

## Example

```python
from nadeshiko_api_client.models.segment_info import SegmentInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SegmentInfo from a JSON string
segment_info_instance = SegmentInfo.from_json(json)
# print the JSON string representation of the object
print(SegmentInfo.to_json())

# convert the object into a dict
segment_info_dict = segment_info_instance.to_dict()
# create an instance of SegmentInfo from a dict
segment_info_from_dict = SegmentInfo.from_dict(segment_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


