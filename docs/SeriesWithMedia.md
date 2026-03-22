# SeriesWithMedia

Series with ordered media entries

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Series ID | 
**name_ja** | **str** | Japanese name of the series | 
**name_romaji** | **str** | Romaji name of the series | 
**name_en** | **str** | English name of the series | 
**media** | [**List[SeriesWithMediaMediaInner]**](SeriesWithMediaMediaInner.md) | All media in the series, sorted by position | 

## Example

```python
from nadeshiko_api_client.models.series_with_media import SeriesWithMedia

# TODO update the JSON string below
json = "{}"
# create an instance of SeriesWithMedia from a JSON string
series_with_media_instance = SeriesWithMedia.from_json(json)
# print the JSON string representation of the object
print(SeriesWithMedia.to_json())

# convert the object into a dict
series_with_media_dict = series_with_media_instance.to_dict()
# create an instance of SeriesWithMedia from a dict
series_with_media_from_dict = SeriesWithMedia.from_dict(series_with_media_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


