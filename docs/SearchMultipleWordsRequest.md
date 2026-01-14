# SearchMultipleWordsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**words** | **List[str]** |  | [optional] 

## Example

```python
from nadeshiko_api_client.models.search_multiple_words_request import SearchMultipleWordsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SearchMultipleWordsRequest from a JSON string
search_multiple_words_request_instance = SearchMultipleWordsRequest.from_json(json)
# print the JSON string representation of the object
print(SearchMultipleWordsRequest.to_json())

# convert the object into a dict
search_multiple_words_request_dict = search_multiple_words_request_instance.to_dict()
# create an instance of SearchMultipleWordsRequest from a dict
search_multiple_words_request_from_dict = SearchMultipleWordsRequest.from_dict(search_multiple_words_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


