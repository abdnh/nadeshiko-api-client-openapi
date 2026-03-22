# Series

Ordered media series grouping

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Series ID | 
**public_id** | **str** | Public identifier for the series | 
**name_ja** | **str** | Japanese name of the series | 
**name_romaji** | **str** | Romaji name of the series | 
**name_en** | **str** | English name of the series | 

## Example

```python
from nadeshiko_api_client.models.series import Series

# TODO update the JSON string below
json = "{}"
# create an instance of Series from a JSON string
series_instance = Series.from_json(json)
# print the JSON string representation of the object
print(Series.to_json())

# convert the object into a dict
series_dict = series_instance.to_dict()
# create an instance of Series from a dict
series_from_dict = Series.from_dict(series_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


