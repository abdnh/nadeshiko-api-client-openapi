# nadeshiko_api_client.MediaApi

All URIs are relative to *https://api.nadeshiko.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_episode**](MediaApi.md#get_episode) | **GET** /v1/media/{mediaId}/episodes/{episodeNumber} | Get single episode
[**get_media**](MediaApi.md#get_media) | **GET** /v1/media/{id} | Get single media
[**get_segment**](MediaApi.md#get_segment) | **GET** /v1/media/{mediaId}/episodes/{episodeNumber}/segments/{id} | Get single segment
[**get_segment_by_uuid**](MediaApi.md#get_segment_by_uuid) | **GET** /v1/media/segments/{uuid} | Get segment by publicId
[**get_segment_context**](MediaApi.md#get_segment_context) | **GET** /v1/media/segments/{uuid}/context | Get surrounding context for a segment
[**get_series**](MediaApi.md#get_series) | **GET** /v1/media/series/{id} | Get series details
[**list_episodes**](MediaApi.md#list_episodes) | **GET** /v1/media/{mediaId}/episodes | List episodes for a media
[**list_media**](MediaApi.md#list_media) | **GET** /v1/media | List all media
[**list_series**](MediaApi.md#list_series) | **GET** /v1/media/series | List all series


# **get_episode**
> Episode get_episode(media_id, episode_number)

Get single episode

Returns a specific episode by media ID and episode number.


### Example

* Bearer (APIKey) Authentication (ApiKey):

```python
import nadeshiko_api_client
from nadeshiko_api_client.models.episode import Episode
from nadeshiko_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.nadeshiko.co
# See configuration.py for a list of all supported configuration parameters.
configuration = nadeshiko_api_client.Configuration(
    host = "https://api.nadeshiko.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (APIKey): ApiKey
configuration = nadeshiko_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with nadeshiko_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nadeshiko_api_client.MediaApi(api_client)
    media_id = 'V1StGXR8_Z5d' # str | Public ID of the media
    episode_number = 1 # int | Episode number

    try:
        # Get single episode
        api_response = api_instance.get_episode(media_id, episode_number)
        print("The response of MediaApi->get_episode:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaApi->get_episode: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **media_id** | **str**| Public ID of the media | 
 **episode_number** | **int**| Episode number | 

### Return type

[**Episode**](Episode.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_media**
> Media get_media(id, include=include)

Get single media

Returns a single media entry by its ID with full metadata.


### Example

* Bearer (APIKey) Authentication (ApiKey):

```python
import nadeshiko_api_client
from nadeshiko_api_client.models.media import Media
from nadeshiko_api_client.models.media_include_expansion import MediaIncludeExpansion
from nadeshiko_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.nadeshiko.co
# See configuration.py for a list of all supported configuration parameters.
configuration = nadeshiko_api_client.Configuration(
    host = "https://api.nadeshiko.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (APIKey): ApiKey
configuration = nadeshiko_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with nadeshiko_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nadeshiko_api_client.MediaApi(api_client)
    id = 'V1StGXR8_Z5d' # str | Media public ID
    include = [] # List[MediaIncludeExpansion] | Resources to expand in the media response (optional) (default to [])

    try:
        # Get single media
        api_response = api_instance.get_media(id, include=include)
        print("The response of MediaApi->get_media:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaApi->get_media: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Media public ID | 
 **include** | [**List[MediaIncludeExpansion]**](MediaIncludeExpansion.md)| Resources to expand in the media response | [optional] [default to []]

### Return type

[**Media**](Media.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_segment**
> Segment get_segment(media_id, episode_number, id)

Get single segment

Returns a specific segment by its ID within the media/episode hierarchy.


### Example

* Bearer (APIKey) Authentication (ApiKey):

```python
import nadeshiko_api_client
from nadeshiko_api_client.models.segment import Segment
from nadeshiko_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.nadeshiko.co
# See configuration.py for a list of all supported configuration parameters.
configuration = nadeshiko_api_client.Configuration(
    host = "https://api.nadeshiko.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (APIKey): ApiKey
configuration = nadeshiko_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with nadeshiko_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nadeshiko_api_client.MediaApi(api_client)
    media_id = 'V1StGXR8_Z5d' # str | Public ID of the media
    episode_number = 1 # int | Episode number
    id = 12345 # int | Segment ID

    try:
        # Get single segment
        api_response = api_instance.get_segment(media_id, episode_number, id)
        print("The response of MediaApi->get_segment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaApi->get_segment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **media_id** | **str**| Public ID of the media | 
 **episode_number** | **int**| Episode number | 
 **id** | **int**| Segment ID | 

### Return type

[**Segment**](Segment.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_segment_by_uuid**
> SegmentInternal get_segment_by_uuid(uuid, include=include)

Get segment by publicId

Returns a specific segment by its publicId. A shortcut alternative to the nested `/media/{mediaId}/episodes/{episodeNumber}/segments/{id}` path.

Pass `include[]=ratingAnalysis` and/or `include[]=posAnalysis` to receive raw analysis fields alongside the standard segment data.


### Example

* Bearer (APIKey) Authentication (ApiKey):

```python
import nadeshiko_api_client
from nadeshiko_api_client.models.segment_internal import SegmentInternal
from nadeshiko_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.nadeshiko.co
# See configuration.py for a list of all supported configuration parameters.
configuration = nadeshiko_api_client.Configuration(
    host = "https://api.nadeshiko.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (APIKey): ApiKey
configuration = nadeshiko_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with nadeshiko_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nadeshiko_api_client.MediaApi(api_client)
    uuid = '3fd94cef-a3e1-31ae-bc8d-e743f03e9c7e' # str | Segment publicId
    include = ['include_example'] # List[str] | Additional internal fields to include in the response (optional)

    try:
        # Get segment by publicId
        api_response = api_instance.get_segment_by_uuid(uuid, include=include)
        print("The response of MediaApi->get_segment_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaApi->get_segment_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Segment publicId | 
 **include** | [**List[str]**](str.md)| Additional internal fields to include in the response | [optional] 

### Return type

[**SegmentInternal**](SegmentInternal.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_segment_context**
> SegmentContextResponse get_segment_context(uuid, take=take, content_rating=content_rating)

Get surrounding context for a segment

Retrieves segments surrounding a specific segment within an episode.
Returns segments both before and after the target, providing dialogue context for how a sentence is used.


### Example

* Bearer (APIKey) Authentication (ApiKey):

```python
import nadeshiko_api_client
from nadeshiko_api_client.models.content_rating import ContentRating
from nadeshiko_api_client.models.segment_context_response import SegmentContextResponse
from nadeshiko_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.nadeshiko.co
# See configuration.py for a list of all supported configuration parameters.
configuration = nadeshiko_api_client.Configuration(
    host = "https://api.nadeshiko.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (APIKey): ApiKey
configuration = nadeshiko_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with nadeshiko_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nadeshiko_api_client.MediaApi(api_client)
    uuid = '3fd94cef-a3e1-31ae-bc8d-e743f03e9c7e' # str | Segment publicId
    take = 3 # int | Number of segments to return before and after the target (optional) (default to 3)
    content_rating = [nadeshiko_api_client.ContentRating()] # List[ContentRating] | Content ratings to include (omit for all ratings) (optional)

    try:
        # Get surrounding context for a segment
        api_response = api_instance.get_segment_context(uuid, take=take, content_rating=content_rating)
        print("The response of MediaApi->get_segment_context:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaApi->get_segment_context: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Segment publicId | 
 **take** | **int**| Number of segments to return before and after the target | [optional] [default to 3]
 **content_rating** | [**List[ContentRating]**](ContentRating.md)| Content ratings to include (omit for all ratings) | [optional] 

### Return type

[**SegmentContextResponse**](SegmentContextResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_series**
> SeriesWithMedia get_series(id, include=include)

Get series details

Returns a series with all media entries sorted by position.


### Example

* Bearer (APIKey) Authentication (ApiKey):

```python
import nadeshiko_api_client
from nadeshiko_api_client.models.media_include_expansion import MediaIncludeExpansion
from nadeshiko_api_client.models.series_with_media import SeriesWithMedia
from nadeshiko_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.nadeshiko.co
# See configuration.py for a list of all supported configuration parameters.
configuration = nadeshiko_api_client.Configuration(
    host = "https://api.nadeshiko.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (APIKey): ApiKey
configuration = nadeshiko_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with nadeshiko_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nadeshiko_api_client.MediaApi(api_client)
    id = 'V1StGXR8_Z5d' # str | Series public ID
    include = [] # List[MediaIncludeExpansion] | Resources to expand in the series response (optional) (default to [])

    try:
        # Get series details
        api_response = api_instance.get_series(id, include=include)
        print("The response of MediaApi->get_series:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaApi->get_series: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Series public ID | 
 **include** | [**List[MediaIncludeExpansion]**](MediaIncludeExpansion.md)| Resources to expand in the series response | [optional] [default to []]

### Return type

[**SeriesWithMedia**](SeriesWithMedia.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_episodes**
> EpisodeListResponse list_episodes(media_id, take=take, cursor=cursor)

List episodes for a media

Returns a paginated list of episodes for a specific media.


### Example

* Bearer (APIKey) Authentication (ApiKey):

```python
import nadeshiko_api_client
from nadeshiko_api_client.models.episode_list_response import EpisodeListResponse
from nadeshiko_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.nadeshiko.co
# See configuration.py for a list of all supported configuration parameters.
configuration = nadeshiko_api_client.Configuration(
    host = "https://api.nadeshiko.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (APIKey): ApiKey
configuration = nadeshiko_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with nadeshiko_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nadeshiko_api_client.MediaApi(api_client)
    media_id = 'V1StGXR8_Z5d' # str | Public ID of the media
    take = 50 # int | Maximum number of episodes to return (optional) (default to 50)
    cursor = '10' # str | Opaque pagination cursor token (optional)

    try:
        # List episodes for a media
        api_response = api_instance.list_episodes(media_id, take=take, cursor=cursor)
        print("The response of MediaApi->list_episodes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaApi->list_episodes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **media_id** | **str**| Public ID of the media | 
 **take** | **int**| Maximum number of episodes to return | [optional] [default to 50]
 **cursor** | **str**| Opaque pagination cursor token | [optional] 

### Return type

[**EpisodeListResponse**](EpisodeListResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_media**
> MediaListResponse list_media(take=take, cursor=cursor, category=category, query=query, include=include)

List all media

Returns a paginated list of media with full metadata, including cover/banner images, episode counts, and genres.
Supports filtering by category and text search.


### Example

* Bearer (APIKey) Authentication (ApiKey):

```python
import nadeshiko_api_client
from nadeshiko_api_client.models.media_include_expansion import MediaIncludeExpansion
from nadeshiko_api_client.models.media_list_response import MediaListResponse
from nadeshiko_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.nadeshiko.co
# See configuration.py for a list of all supported configuration parameters.
configuration = nadeshiko_api_client.Configuration(
    host = "https://api.nadeshiko.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (APIKey): ApiKey
configuration = nadeshiko_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with nadeshiko_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nadeshiko_api_client.MediaApi(api_client)
    take = 20 # int | Number of results per page (optional) (default to 20)
    cursor = 'cursor_example' # str | Opaque pagination cursor token (optional)
    category = 'ANIME' # str | Filter by media category (optional)
    query = 'steins' # str | Search query for filtering media by name (optional)
    include = [] # List[MediaIncludeExpansion] | Resources to expand in the media response (optional) (default to [])

    try:
        # List all media
        api_response = api_instance.list_media(take=take, cursor=cursor, category=category, query=query, include=include)
        print("The response of MediaApi->list_media:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaApi->list_media: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **take** | **int**| Number of results per page | [optional] [default to 20]
 **cursor** | **str**| Opaque pagination cursor token | [optional] 
 **category** | **str**| Filter by media category | [optional] 
 **query** | **str**| Search query for filtering media by name | [optional] 
 **include** | [**List[MediaIncludeExpansion]**](MediaIncludeExpansion.md)| Resources to expand in the media response | [optional] [default to []]

### Return type

[**MediaListResponse**](MediaListResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_series**
> SeriesListResponse list_series(take=take, cursor=cursor, query=query)

List all series

Returns a paginated list of media series groupings.


### Example

* Bearer (APIKey) Authentication (ApiKey):

```python
import nadeshiko_api_client
from nadeshiko_api_client.models.series_list_response import SeriesListResponse
from nadeshiko_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.nadeshiko.co
# See configuration.py for a list of all supported configuration parameters.
configuration = nadeshiko_api_client.Configuration(
    host = "https://api.nadeshiko.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (APIKey): ApiKey
configuration = nadeshiko_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with nadeshiko_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nadeshiko_api_client.MediaApi(api_client)
    take = 20 # int | Number of results per page (optional) (default to 20)
    cursor = 'cursor_example' # str | Opaque pagination cursor token (optional)
    query = 'bakuman' # str | Case-insensitive search across English, Japanese, and Romaji names (optional)

    try:
        # List all series
        api_response = api_instance.list_series(take=take, cursor=cursor, query=query)
        print("The response of MediaApi->list_series:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaApi->list_series: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **take** | **int**| Number of results per page | [optional] [default to 20]
 **cursor** | **str**| Opaque pagination cursor token | [optional] 
 **query** | **str**| Case-insensitive search across English, Japanese, and Romaji names | [optional] 

### Return type

[**SeriesListResponse**](SeriesListResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

