# SeriesWithMediaMediaInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position** | **int** | Position in the series (1-indexed) | 
**media** | [**Media**](Media.md) |  | 

## Example

```python
from nadeshiko_api_client.models.series_with_media_media_inner import SeriesWithMediaMediaInner

# TODO update the JSON string below
json = "{}"
# create an instance of SeriesWithMediaMediaInner from a JSON string
series_with_media_media_inner_instance = SeriesWithMediaMediaInner.from_json(json)
# print the JSON string representation of the object
print(SeriesWithMediaMediaInner.to_json())

# convert the object into a dict
series_with_media_media_inner_dict = series_with_media_media_inner_instance.to_dict()
# create an instance of SeriesWithMediaMediaInner from a dict
series_with_media_media_inner_from_dict = SeriesWithMediaMediaInner.from_dict(series_with_media_media_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


