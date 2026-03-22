# SegmentUrls

URLs to media resources for this segment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image_url** | **str** | URL to the subtitle image snapshot | 
**audio_url** | **str** | URL to the audio clip for this segment | 
**video_url** | **str** | URL to the video clip for this segment | 

## Example

```python
from nadeshiko_api_client.models.segment_urls import SegmentUrls

# TODO update the JSON string below
json = "{}"
# create an instance of SegmentUrls from a JSON string
segment_urls_instance = SegmentUrls.from_json(json)
# print the JSON string representation of the object
print(SegmentUrls.to_json())

# convert the object into a dict
segment_urls_dict = segment_urls_instance.to_dict()
# create an instance of SegmentUrls from a dict
segment_urls_from_dict = SegmentUrls.from_dict(segment_urls_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


