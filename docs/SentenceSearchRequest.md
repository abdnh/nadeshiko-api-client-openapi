# SentenceSearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** | Text or sentence to search | [optional] 
**limit** | **int** | Max amount of entries by response | [optional] 
**uuid** | **str** | Unique ID from sentence (Useful to get a specific sentence) | [optional] 
**category** | **int** | Anime, Liveaction | [optional] 
**anime_id** | **int** | Unique ID from media | [optional] 
**season** | **List[int]** | Array of seasons to get | [optional] 
**episode** | **List[int]** | Array of episodes to get | [optional] 
**random_seed** | **float** | A value from 0 to 1 | [optional] 
**content_sort** | **str** | Order by amount of characters | [optional] 
**cursor** | **List[int]** | Current page of search | [optional] 

## Example

```python
from nadeshiko_api_client.models.sentence_search_request import SentenceSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SentenceSearchRequest from a JSON string
sentence_search_request_instance = SentenceSearchRequest.from_json(json)
# print the JSON string representation of the object
print(SentenceSearchRequest.to_json())

# convert the object into a dict
sentence_search_request_dict = sentence_search_request_instance.to_dict()
# create an instance of SentenceSearchRequest from a dict
sentence_search_request_from_dict = SentenceSearchRequest.from_dict(sentence_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


