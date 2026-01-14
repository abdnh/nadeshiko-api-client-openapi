# BasicInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id_anime** | **int** |  | [optional] 
**name_anime_romaji** | **str** |  | [optional] 
**name_anime_en** | **str** |  | [optional] 
**name_anime_jp** | **str** |  | [optional] 
**cover** | **str** |  | [optional] 
**banner** | **str** |  | [optional] 
**episode** | **int** |  | [optional] 
**season** | **int** |  | [optional] 
**category** | **int** |  | [optional] 

## Example

```python
from nadeshiko_api_client.models.basic_info import BasicInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BasicInfo from a JSON string
basic_info_instance = BasicInfo.from_json(json)
# print the JSON string representation of the object
print(BasicInfo.to_json())

# convert the object into a dict
basic_info_dict = basic_info_instance.to_dict()
# create an instance of BasicInfo from a dict
basic_info_from_dict = BasicInfo.from_dict(basic_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


