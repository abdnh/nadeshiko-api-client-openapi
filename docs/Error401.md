# Error401

Unauthorized error response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Specific error code for programmatic handling | 
**title** | **str** | A short, human-readable summary of the problem | 
**detail** | **str** | A human-readable explanation specific to this occurrence | 
**type** | **str** | A URI reference that identifies the problem type (e.g., GitHub issues link) | [optional] 
**instance** | **str** | A URI reference that identifies the specific occurrence (e.g., trace ID) | [optional] 
**status** | **int** | The HTTP status code | 
**errors** | **Dict[str, str]** | Optional map of field names to their error messages (for validation errors) | [optional] 

## Example

```python
from nadeshiko_api_client.models.error401 import Error401

# TODO update the JSON string below
json = "{}"
# create an instance of Error401 from a JSON string
error401_instance = Error401.from_json(json)
# print the JSON string representation of the object
print(Error401.to_json())

# convert the object into a dict
error401_dict = error401_instance.to_dict()
# create an instance of Error401 from a dict
error401_from_dict = Error401.from_dict(error401_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


