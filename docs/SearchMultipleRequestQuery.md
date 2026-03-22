# SearchMultipleRequestQuery

What to search for

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**words** | **List[str]** | List of words to search for | 
**exact_match** | **bool** | Whether to use exact matching | [optional] [default to False]

## Example

```python
from nadeshiko_api_client.models.search_multiple_request_query import SearchMultipleRequestQuery

# TODO update the JSON string below
json = "{}"
# create an instance of SearchMultipleRequestQuery from a JSON string
search_multiple_request_query_instance = SearchMultipleRequestQuery.from_json(json)
# print the JSON string representation of the object
print(SearchMultipleRequestQuery.to_json())

# convert the object into a dict
search_multiple_request_query_dict = search_multiple_request_query_instance.to_dict()
# create an instance of SearchMultipleRequestQuery from a dict
search_multiple_request_query_from_dict = SearchMultipleRequestQuery.from_dict(search_multiple_request_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


