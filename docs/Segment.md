# Segment

Segment with content, optional highlights, and media URLs

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Numeric identifier for the segment | 
**uuid** | **str** | Unique identifier for the segment | 
**public_id** | **str** | Public identifier for the segment (use this instead of uuid in public URLs) | 
**position** | **int** | Position of the segment within the episode | 
**status** | **str** | Segment status | 
**start_time_ms** | **int** | Start time of the segment in milliseconds from the beginning of the episode | 
**end_time_ms** | **int** | End time of the segment in milliseconds from the beginning of the episode | 
**content_rating** | [**ContentRating**](ContentRating.md) |  | 
**episode** | **int** | Episode number this segment belongs to | 
**media_id** | **int** | Media ID this segment belongs to | 
**media_public_id** | **str** | Public ID of the media this segment belongs to | 
**text_ja** | [**SegmentTextJa**](SegmentTextJa.md) |  | 
**text_en** | [**SegmentTextEn**](SegmentTextEn.md) |  | 
**text_es** | [**SegmentTextEs**](SegmentTextEs.md) |  | 
**urls** | [**SegmentUrls**](SegmentUrls.md) |  | 

## Example

```python
from nadeshiko_api_client.models.segment import Segment

# TODO update the JSON string below
json = "{}"
# create an instance of Segment from a JSON string
segment_instance = Segment.from_json(json)
# print the JSON string representation of the object
print(Segment.to_json())

# convert the object into a dict
segment_dict = segment_instance.to_dict()
# create an instance of Segment from a dict
segment_from_dict = Segment.from_dict(segment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


