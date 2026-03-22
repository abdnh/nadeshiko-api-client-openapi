# SearchStatsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | [**SearchStatsRequestQuery**](SearchStatsRequestQuery.md) |  | [optional] 
**filters** | [**SearchFilters**](SearchFilters.md) |  | [optional] 
**include** | [**List[IncludeExpansion]**](IncludeExpansion.md) | Resources to expand in the response includes block | [optional] [default to []]

## Example

```python
from nadeshiko_api_client.models.search_stats_request import SearchStatsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SearchStatsRequest from a JSON string
search_stats_request_instance = SearchStatsRequest.from_json(json)
# print the JSON string representation of the object
print(SearchStatsRequest.to_json())

# convert the object into a dict
search_stats_request_dict = search_stats_request_instance.to_dict()
# create an instance of SearchStatsRequest from a dict
search_stats_request_from_dict = SearchStatsRequest.from_dict(search_stats_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


