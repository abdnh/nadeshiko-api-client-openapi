# WordMatchMedia

Media match count entry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**media_id** | **int** | Media identifier (look up full details in includes.media) | 
**match_count** | **int** | Number of times the word appears in this media | 

## Example

```python
from nadeshiko_api_client.models.word_match_media import WordMatchMedia

# TODO update the JSON string below
json = "{}"
# create an instance of WordMatchMedia from a JSON string
word_match_media_instance = WordMatchMedia.from_json(json)
# print the JSON string representation of the object
print(WordMatchMedia.to_json())

# convert the object into a dict
word_match_media_dict = word_match_media_instance.to_dict()
# create an instance of WordMatchMedia from a dict
word_match_media_from_dict = WordMatchMedia.from_dict(word_match_media_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


