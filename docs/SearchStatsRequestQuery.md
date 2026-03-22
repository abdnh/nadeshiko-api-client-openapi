# SearchStatsRequestQuery

What to search for (omit for queryless stats)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search** | **str** | Search expression (supports boolean operators, wildcards, phrase matching) | [optional] 
**exact_match** | **bool** | Whether to use exact phrase matching | [optional] [default to False]

## Example

```python
from nadeshiko_api_client.models.search_stats_request_query import SearchStatsRequestQuery

# TODO update the JSON string below
json = "{}"
# create an instance of SearchStatsRequestQuery from a JSON string
search_stats_request_query_instance = SearchStatsRequestQuery.from_json(json)
# print the JSON string representation of the object
print(SearchStatsRequestQuery.to_json())

# convert the object into a dict
search_stats_request_query_dict = search_stats_request_query_instance.to_dict()
# create an instance of SearchStatsRequestQuery from a dict
search_stats_request_query_from_dict = SearchStatsRequestQuery.from_dict(search_stats_request_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


