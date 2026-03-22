# SearchRequestQuery

What to search for (omit for queryless browse)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search** | **str** | Search expression (supports boolean operators, wildcards, phrase matching) | [optional] 
**exact_match** | **bool** | Whether to use exact phrase matching | [optional] [default to False]

## Example

```python
from nadeshiko_api_client.models.search_request_query import SearchRequestQuery

# TODO update the JSON string below
json = "{}"
# create an instance of SearchRequestQuery from a JSON string
search_request_query_instance = SearchRequestQuery.from_json(json)
# print the JSON string representation of the object
print(SearchRequestQuery.to_json())

# convert the object into a dict
search_request_query_dict = search_request_query_instance.to_dict()
# create an instance of SearchRequestQuery from a dict
search_request_query_from_dict = SearchRequestQuery.from_dict(search_request_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


