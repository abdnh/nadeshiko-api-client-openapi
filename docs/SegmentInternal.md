# SegmentInternal

Segment with internal fields. For write operations (create, update) all fields are always populated. For GET, optional fields are only populated when requested via include[]. 

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
**storage** | **str** | Storage backend for segment assets | [optional] 
**hashed_id** | **str** | Hash identifier for the segment | [optional] 
**storage_base_path** | **str** | Base path in the storage backend | [optional] 
**rating_analysis** | **Dict[str, object]** | Raw WD Tagger v3 classifier output used to derive content rating | [optional] 
**pos_analysis** | **Dict[str, object]** | POS tokenization results keyed by engine (sudachi, unidic) | [optional] 

## Example

```python
from nadeshiko_api_client.models.segment_internal import SegmentInternal

# TODO update the JSON string below
json = "{}"
# create an instance of SegmentInternal from a JSON string
segment_internal_instance = SegmentInternal.from_json(json)
# print the JSON string representation of the object
print(SegmentInternal.to_json())

# convert the object into a dict
segment_internal_dict = segment_internal_instance.to_dict()
# create an instance of SegmentInternal from a dict
segment_internal_from_dict = SegmentInternal.from_dict(segment_internal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


