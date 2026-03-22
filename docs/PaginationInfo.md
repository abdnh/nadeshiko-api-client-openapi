# PaginationInfo

Pagination metadata for search results

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_more** | **bool** | Whether there are more results after this page | 
**estimated_total_hits** | **int** | Estimated total number of matching segments | 
**estimated_total_hits_relation** | **str** | Whether estimatedTotalHits is exact or a lower bound | 
**cursor** | **str** | Opaque cursor token for fetching the next page (&#x60;null&#x60; when hasMore is false) | 

## Example

```python
from nadeshiko_api_client.models.pagination_info import PaginationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PaginationInfo from a JSON string
pagination_info_instance = PaginationInfo.from_json(json)
# print the JSON string representation of the object
print(PaginationInfo.to_json())

# convert the object into a dict
pagination_info_dict = pagination_info_instance.to_dict()
# create an instance of PaginationInfo from a dict
pagination_info_from_dict = PaginationInfo.from_dict(pagination_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


