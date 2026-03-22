# nadeshiko_api_client.SearchApi

All URIs are relative to *https://api.nadeshiko.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_search_stats**](SearchApi.md#get_search_stats) | **POST** /v1/search/stats | Get search statistics
[**search**](SearchApi.md#search) | **POST** /v1/search | Search segments by query
[**search_words**](SearchApi.md#search_words) | **POST** /v1/search/words | Search by multiple words


# **get_search_stats**
> SearchStatsResponse get_search_stats(search_stats_request=search_stats_request)

Get search statistics

Returns statistics for search filters and category tabs without fetching segment rows.

This endpoint is optimized for UI filter panels:
- `media` powers the media dropdown on the right side.
- `categories` powers category tabs below the search bar.

The stats are scoped by query and category filters, but are not narrowed by a selected media/episode.


### Example

* Bearer (APIKey) Authentication (ApiKey):

```python
import nadeshiko_api_client
from nadeshiko_api_client.models.search_stats_request import SearchStatsRequest
from nadeshiko_api_client.models.search_stats_response import SearchStatsResponse
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
    api_instance = nadeshiko_api_client.SearchApi(api_client)
    search_stats_request = nadeshiko_api_client.SearchStatsRequest() # SearchStatsRequest |  (optional)

    try:
        # Get search statistics
        api_response = api_instance.get_search_stats(search_stats_request=search_stats_request)
        print("The response of SearchApi->get_search_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->get_search_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_stats_request** | [**SearchStatsRequest**](SearchStatsRequest.md)|  | [optional] 

### Return type

[**SearchStatsResponse**](SearchStatsResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
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

# **search**
> SearchResponse search(search_request=search_request)

Search segments by query

The primary search endpoint for finding Japanese segments and their translations across indexed media (anime, J-Drama).

This endpoint uses Elasticsearch with advanced Japanese text analysis supporting multiple input types (romaji, kanji, kana) and providing intelligent field-based boosting.

**Query Features**
- **Multi-language Support:** Search using Japanese (kanji/kana), Romaji, or English/Spanish
- **Boolean Operators:** `AND`, `OR`, `NOT` supported (e.g., `(cat OR dog) AND bird`)
- **Phrase Matching:** Use quotes for exact phrases (e.g., `"good morning"`), or pass `exactMatch: true` to the request body
- **Wildcards:** `te*t` format (leading wildcards not supported)
- **Smart Field Selection:** Automatically chooses optimal search fields based on input type

**Input Type Handling**
| Input Type | Search Strategy |
|------------|-----------------|
| **Romaji** (`go`, `taberu`) | Boosts EN/ES translations, reading form (pronunciation), and base form |
| **Kanji** (`食べる`, `彼女`) | Searches content and base form (dictionary form). Ignores matches by reading (homophones). |
| **Kana** (`たべる`, `かのじょ`) | Standard search across content, base form, and reading form |
| **English/Spanish** | Direct translation search |


### Example

* Bearer (APIKey) Authentication (ApiKey):

```python
import nadeshiko_api_client
from nadeshiko_api_client.models.search_request import SearchRequest
from nadeshiko_api_client.models.search_response import SearchResponse
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
    api_instance = nadeshiko_api_client.SearchApi(api_client)
    search_request = nadeshiko_api_client.SearchRequest() # SearchRequest |  (optional)

    try:
        # Search segments by query
        api_response = api_instance.search(search_request=search_request)
        print("The response of SearchApi->search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_request** | [**SearchRequest**](SearchRequest.md)|  | [optional] 

### Return type

[**SearchResponse**](SearchResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
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

# **search_words**
> SearchMultipleResponse search_words(search_multiple_request)

Search by multiple words

Searches for multiple words simultaneously and aggregates results by media.

Unlike the main search endpoint, this returns a summary of matches per media rather than individual segments.


### Example

* Bearer (APIKey) Authentication (ApiKey):

```python
import nadeshiko_api_client
from nadeshiko_api_client.models.search_multiple_request import SearchMultipleRequest
from nadeshiko_api_client.models.search_multiple_response import SearchMultipleResponse
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
    api_instance = nadeshiko_api_client.SearchApi(api_client)
    search_multiple_request = {"words":["彼女","私"],"exactMatch":false} # SearchMultipleRequest | 

    try:
        # Search by multiple words
        api_response = api_instance.search_words(search_multiple_request)
        print("The response of SearchApi->search_words:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->search_words: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_multiple_request** | [**SearchMultipleRequest**](SearchMultipleRequest.md)|  | 

### Return type

[**SearchMultipleResponse**](SearchMultipleResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
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

