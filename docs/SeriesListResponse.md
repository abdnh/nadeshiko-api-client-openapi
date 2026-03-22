# SeriesListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**series** | [**List[Series]**](Series.md) |  | 
**pagination** | [**OpaqueCursorPagination**](OpaqueCursorPagination.md) |  | 

## Example

```python
from nadeshiko_api_client.models.series_list_response import SeriesListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SeriesListResponse from a JSON string
series_list_response_instance = SeriesListResponse.from_json(json)
# print the JSON string representation of the object
print(SeriesListResponse.to_json())

# convert the object into a dict
series_list_response_dict = series_list_response_instance.to_dict()
# create an instance of SeriesListResponse from a dict
series_list_response_from_dict = SeriesListResponse.from_dict(series_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


