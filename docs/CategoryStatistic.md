# CategoryStatistic


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **int** |  | [optional] 
**count** | **int** |  | [optional] 

## Example

```python
from nadeshiko_api_client.models.category_statistic import CategoryStatistic

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryStatistic from a JSON string
category_statistic_instance = CategoryStatistic.from_json(json)
# print the JSON string representation of the object
print(CategoryStatistic.to_json())

# convert the object into a dict
category_statistic_dict = category_statistic_instance.to_dict()
# create an instance of CategoryStatistic from a dict
category_statistic_from_dict = CategoryStatistic.from_dict(category_statistic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


