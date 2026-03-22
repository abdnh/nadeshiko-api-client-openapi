# SearchFiltersLanguages

Language inclusion/exclusion for search matching

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude** | **List[str]** | Language codes to exclude from search matching (e.g., [\&quot;en\&quot;], [\&quot;es\&quot;], [\&quot;en\&quot;,\&quot;es\&quot;]) | [optional] 

## Example

```python
from nadeshiko_api_client.models.search_filters_languages import SearchFiltersLanguages

# TODO update the JSON string below
json = "{}"
# create an instance of SearchFiltersLanguages from a JSON string
search_filters_languages_instance = SearchFiltersLanguages.from_json(json)
# print the JSON string representation of the object
print(SearchFiltersLanguages.to_json())

# convert the object into a dict
search_filters_languages_dict = search_filters_languages_instance.to_dict()
# create an instance of SearchFiltersLanguages from a dict
search_filters_languages_from_dict = SearchFiltersLanguages.from_dict(search_filters_languages_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


