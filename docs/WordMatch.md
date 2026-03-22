# WordMatch

Word matching result with occurrences across media

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**word** | **str** | The word that was searched for | 
**is_match** | **bool** | Indicates whether the word was found in any segment | 
**match_count** | **int** | Total number of times this word appears across all media | 
**media** | [**List[WordMatchMedia]**](WordMatchMedia.md) | List of media containing this word | 

## Example

```python
from nadeshiko_api_client.models.word_match import WordMatch

# TODO update the JSON string below
json = "{}"
# create an instance of WordMatch from a JSON string
word_match_instance = WordMatch.from_json(json)
# print the JSON string representation of the object
print(WordMatch.to_json())

# convert the object into a dict
word_match_dict = word_match_instance.to_dict()
# create an instance of WordMatch from a dict
word_match_from_dict = WordMatch.from_dict(word_match_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


