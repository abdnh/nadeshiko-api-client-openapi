# SearchStatsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**media** | [**List[MediaSearchStats]**](MediaSearchStats.md) |  | 
**categories** | [**List[CategoryCount]**](CategoryCount.md) |  | 
**includes** | [**SearchResponseIncludes**](SearchResponseIncludes.md) |  | 

## Example

```python
from nadeshiko_api_client.models.search_stats_response import SearchStatsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SearchStatsResponse from a JSON string
search_stats_response_instance = SearchStatsResponse.from_json(json)
# print the JSON string representation of the object
print(SearchStatsResponse.to_json())

# convert the object into a dict
search_stats_response_dict = search_stats_response_instance.to_dict()
# create an instance of SearchStatsResponse from a dict
search_stats_response_from_dict = SearchStatsResponse.from_dict(search_stats_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


