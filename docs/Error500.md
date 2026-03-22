# Error500

Internal Server Error response

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
from nadeshiko_api_client.models.error500 import Error500

# TODO update the JSON string below
json = "{}"
# create an instance of Error500 from a JSON string
error500_instance = Error500.from_json(json)
# print the JSON string representation of the object
print(Error500.to_json())

# convert the object into a dict
error500_dict = error500_instance.to_dict()
# create an instance of Error500 from a dict
error500_from_dict = Error500.from_dict(error500_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


