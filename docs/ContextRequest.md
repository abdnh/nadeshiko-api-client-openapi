# ContextRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**media_id** | **int** |  | [optional] 
**season** | **int** |  | [optional] 
**episode** | **int** |  | [optional] 
**segment_position** | **int** |  | [optional] 
**limit** | **int** |  | [optional] 

## Example

```python
from nadeshiko_api_client.models.context_request import ContextRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ContextRequest from a JSON string
context_request_instance = ContextRequest.from_json(json)
# print the JSON string representation of the object
print(ContextRequest.to_json())

# convert the object into a dict
context_request_dict = context_request_instance.to_dict()
# create an instance of ContextRequest from a dict
context_request_from_dict = ContextRequest.from_dict(context_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


