# Seiyuu

Japanese voice actor (seiyuu)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Internal seiyuu ID | 
**public_id** | **str** | Public identifier for the seiyuu (use this in public URLs) | 
**external_ids** | [**ExternalId**](ExternalId.md) |  | 
**name_ja** | **str** | Japanese name of the voice actor | 
**name_en** | **str** | English name of the voice actor | 
**image_url** | **str** | Profile image URL | 

## Example

```python
from nadeshiko_api_client.models.seiyuu import Seiyuu

# TODO update the JSON string below
json = "{}"
# create an instance of Seiyuu from a JSON string
seiyuu_instance = Seiyuu.from_json(json)
# print the JSON string representation of the object
print(Seiyuu.to_json())

# convert the object into a dict
seiyuu_dict = seiyuu_instance.to_dict()
# create an instance of Seiyuu from a dict
seiyuu_from_dict = Seiyuu.from_dict(seiyuu_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


