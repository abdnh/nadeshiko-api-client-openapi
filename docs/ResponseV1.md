# ResponseV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**statistics** | [**List[Statistic]**](Statistic.md) |  | [optional] 
**category_statistics** | [**List[CategoryStatistic]**](CategoryStatistic.md) |  | [optional] 
**sentences** | [**List[Sentence]**](Sentence.md) |  | [optional] 
**cursor** | **List[float]** |  | [optional] 

## Example

```python
from nadeshiko_api_client.models.response_v1 import ResponseV1

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseV1 from a JSON string
response_v1_instance = ResponseV1.from_json(json)
# print the JSON string representation of the object
print(ResponseV1.to_json())

# convert the object into a dict
response_v1_dict = response_v1_instance.to_dict()
# create an instance of ResponseV1 from a dict
response_v1_from_dict = ResponseV1.from_dict(response_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


