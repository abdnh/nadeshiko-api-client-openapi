# SegmentTextEs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** | Spanish translation | 
**is_machine_translated** | **bool** | Whether the translation was machine-translated | 
**highlight** | **str** | Spanish content with search terms highlighted | [optional] 

## Example

```python
from nadeshiko_api_client.models.segment_text_es import SegmentTextEs

# TODO update the JSON string below
json = "{}"
# create an instance of SegmentTextEs from a JSON string
segment_text_es_instance = SegmentTextEs.from_json(json)
# print the JSON string representation of the object
print(SegmentTextEs.to_json())

# convert the object into a dict
segment_text_es_dict = segment_text_es_instance.to_dict()
# create an instance of SegmentTextEs from a dict
segment_text_es_from_dict = SegmentTextEs.from_dict(segment_text_es_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


