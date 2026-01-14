# nadeshiko_api_client.SearchApi

All URIs are relative to *https://api.brigadasos.xyz/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_context_sentence**](SearchApi.md#get_context_sentence) | **POST** /search/media/context | Get context for a sentence
[**get_recent_media**](SearchApi.md#get_recent_media) | **GET** /search/media/info | Get recent media
[**search_multiple_words**](SearchApi.md#search_multiple_words) | **POST** /search/media/match/words | Search by multiple queries
[**search_sentence**](SearchApi.md#search_sentence) | **POST** /search/media/sentence | Search by query


# **get_context_sentence**
> object get_context_sentence(context_request)

Get context for a sentence

Retrieve context for a specific sentence in media

### Example

* Api Key Authentication (apiKeyHeader):

```python
import nadeshiko_api_client
from nadeshiko_api_client.models.context_request import ContextRequest
from nadeshiko_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.brigadasos.xyz/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = nadeshiko_api_client.Configuration(
    host = "https://api.brigadasos.xyz/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyHeader
configuration.api_key['apiKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with nadeshiko_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nadeshiko_api_client.SearchApi(api_client)
    context_request = nadeshiko_api_client.ContextRequest() # ContextRequest | 

    try:
        # Get context for a sentence
        api_response = api_instance.get_context_sentence(context_request)
        print("The response of SearchApi->get_context_sentence:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->get_context_sentence: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **context_request** | [**ContextRequest**](ContextRequest.md)|  | 

### Return type

**object**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recent_media**
> object get_recent_media(size=size, sorted=sorted)

Get recent media

Retrieve information about recent media

### Example

* Api Key Authentication (apiKeyHeader):

```python
import nadeshiko_api_client
from nadeshiko_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.brigadasos.xyz/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = nadeshiko_api_client.Configuration(
    host = "https://api.brigadasos.xyz/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyHeader
configuration.api_key['apiKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with nadeshiko_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nadeshiko_api_client.SearchApi(api_client)
    size = 10 # int |  (optional) (default to 10)
    sorted = True # bool |  (optional) (default to True)

    try:
        # Get recent media
        api_response = api_instance.get_recent_media(size=size, sorted=sorted)
        print("The response of SearchApi->get_recent_media:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->get_recent_media: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **int**|  | [optional] [default to 10]
 **sorted** | **bool**|  | [optional] [default to True]

### Return type

**object**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_multiple_words**
> object search_multiple_words(search_multiple_words_request)

Search by multiple queries

Search for media matching multiple words

### Example

* Api Key Authentication (apiKeyHeader):

```python
import nadeshiko_api_client
from nadeshiko_api_client.models.search_multiple_words_request import SearchMultipleWordsRequest
from nadeshiko_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.brigadasos.xyz/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = nadeshiko_api_client.Configuration(
    host = "https://api.brigadasos.xyz/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyHeader
configuration.api_key['apiKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with nadeshiko_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nadeshiko_api_client.SearchApi(api_client)
    search_multiple_words_request = nadeshiko_api_client.SearchMultipleWordsRequest() # SearchMultipleWordsRequest | 

    try:
        # Search by multiple queries
        api_response = api_instance.search_multiple_words(search_multiple_words_request)
        print("The response of SearchApi->search_multiple_words:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->search_multiple_words: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_multiple_words_request** | [**SearchMultipleWordsRequest**](SearchMultipleWordsRequest.md)|  | 

### Return type

**object**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_sentence**
> ResponseV1 search_sentence(sentence_search_request)

Search by query

Search for sentences in the media database

### Example

* Api Key Authentication (apiKeyHeader):

```python
import nadeshiko_api_client
from nadeshiko_api_client.models.response_v1 import ResponseV1
from nadeshiko_api_client.models.sentence_search_request import SentenceSearchRequest
from nadeshiko_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.brigadasos.xyz/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = nadeshiko_api_client.Configuration(
    host = "https://api.brigadasos.xyz/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyHeader
configuration.api_key['apiKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with nadeshiko_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nadeshiko_api_client.SearchApi(api_client)
    sentence_search_request = nadeshiko_api_client.SentenceSearchRequest() # SentenceSearchRequest | 

    try:
        # Search by query
        api_response = api_instance.search_sentence(sentence_search_request)
        print("The response of SearchApi->search_sentence:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->search_sentence: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sentence_search_request** | [**SentenceSearchRequest**](SentenceSearchRequest.md)|  | 

### Return type

[**ResponseV1**](ResponseV1.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

