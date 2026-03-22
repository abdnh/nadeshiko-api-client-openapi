import os
from pprint import pprint
import nadeshiko_api_client
from nadeshiko_api_client.rest import ApiException

configuration = nadeshiko_api_client.Configuration(
    access_token = os.environ["NADESHIKO_API_KEY"]
)

with nadeshiko_api_client.ApiClient(configuration) as api_client:
    api_instance = nadeshiko_api_client.SearchApi(api_client)
    search_request = nadeshiko_api_client.SearchRequest()
    query = nadeshiko_api_client.SearchRequestQuery()
    query.search = "行方不明"
    search_request.query = query
    sort = nadeshiko_api_client.SearchRequestSort()
    sort.mode = "RANDOM"
    sort.seed = 42
    search_request.sort = sort
    try:
        api_response = api_instance.search(search_request)
        pprint(api_response.to_json())
    except ApiException as e:
        print("Exception when calling SearchApi->search_request: %s\n" % e)
