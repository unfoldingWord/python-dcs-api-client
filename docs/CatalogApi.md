# dcs_api_client.CatalogApi

All URIs are relative to *http://localhost/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalog_get_entry**](CatalogApi.md#catalog_get_entry) | **GET** /catalog/entry/{owner}/{repo}/{ref} | Catalog entry
[**catalog_get_metadata**](CatalogApi.md#catalog_get_metadata) | **GET** /catalog/entry/{owner}/{repo}/{ref}/metadata | Catalog entry metadata (manifest.yaml in JSON format)
[**catalog_list_languages**](CatalogApi.md#catalog_list_languages) | **GET** /catalog/owners | Catalog list owners
[**catalog_list_subjects**](CatalogApi.md#catalog_list_subjects) | **GET** /catalog/subjects | Catalog list subjects
[**catalog_search**](CatalogApi.md#catalog_search) | **GET** /catalog/search | Catalog search
[**catalog_search_owner**](CatalogApi.md#catalog_search_owner) | **GET** /catalog/search/{owner} | Catalog search by owner
[**catalog_search_repo**](CatalogApi.md#catalog_search_repo) | **GET** /catalog/search/{owner}/{repo} | Catalog search by repo


# **catalog_get_entry**
> CatalogEntry catalog_get_entry(owner, repo, ref)

Catalog entry

### Example
```python
from __future__ import print_function
import time
import dcs_api_client
from dcs_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = dcs_api_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: AuthorizationHeaderToken
configuration = dcs_api_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = dcs_api_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: SudoHeader
configuration = dcs_api_client.Configuration()
configuration.api_key['Sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Sudo'] = 'Bearer'
# Configure API key authorization: SudoParam
configuration = dcs_api_client.Configuration()
configuration.api_key['sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo'] = 'Bearer'
# Configure API key authorization: TOTPHeader
configuration = dcs_api_client.Configuration()
configuration.api_key['X-GITEA-OTP'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-GITEA-OTP'] = 'Bearer'
# Configure API key authorization: Token
configuration = dcs_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = dcs_api_client.CatalogApi(dcs_api_client.ApiClient(configuration))
owner = 'owner_example' # str | name of the owner
repo = 'repo_example' # str | name of the repo
ref = 'ref_example' # str | release tag or default branch

try:
    # Catalog entry
    api_response = api_instance.catalog_get_entry(owner, repo, ref)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogApi->catalog_get_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| name of the owner | 
 **repo** | **str**| name of the repo | 
 **ref** | **str**| release tag or default branch | 

### Return type

[**CatalogEntry**](CatalogEntry.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **catalog_get_metadata**
> dict(str, object) catalog_get_metadata(owner, repo, ref)

Catalog entry metadata (manifest.yaml in JSON format)

### Example
```python
from __future__ import print_function
import time
import dcs_api_client
from dcs_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = dcs_api_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: AuthorizationHeaderToken
configuration = dcs_api_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = dcs_api_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: SudoHeader
configuration = dcs_api_client.Configuration()
configuration.api_key['Sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Sudo'] = 'Bearer'
# Configure API key authorization: SudoParam
configuration = dcs_api_client.Configuration()
configuration.api_key['sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo'] = 'Bearer'
# Configure API key authorization: TOTPHeader
configuration = dcs_api_client.Configuration()
configuration.api_key['X-GITEA-OTP'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-GITEA-OTP'] = 'Bearer'
# Configure API key authorization: Token
configuration = dcs_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = dcs_api_client.CatalogApi(dcs_api_client.ApiClient(configuration))
owner = 'owner_example' # str | name of the owner
repo = 'repo_example' # str | name of the repo
ref = 'ref_example' # str | release tag or default branch

try:
    # Catalog entry metadata (manifest.yaml in JSON format)
    api_response = api_instance.catalog_get_metadata(owner, repo, ref)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogApi->catalog_get_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| name of the owner | 
 **repo** | **str**| name of the repo | 
 **ref** | **str**| release tag or default branch | 

### Return type

**dict(str, object)**

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **catalog_list_languages**
> list[str] catalog_list_languages(owner=owner, lang=lang, stage=stage, subject=subject, resource=resource, format=format, checking_level=checking_level, book=book, metadata_type=metadata_type, metadata_version=metadata_version, direction=direction, is_gl=is_gl, partial_match=partial_match)

Catalog list owners

### Example
```python
from __future__ import print_function
import time
import dcs_api_client
from dcs_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = dcs_api_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: AuthorizationHeaderToken
configuration = dcs_api_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = dcs_api_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: SudoHeader
configuration = dcs_api_client.Configuration()
configuration.api_key['Sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Sudo'] = 'Bearer'
# Configure API key authorization: SudoParam
configuration = dcs_api_client.Configuration()
configuration.api_key['sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo'] = 'Bearer'
# Configure API key authorization: TOTPHeader
configuration = dcs_api_client.Configuration()
configuration.api_key['X-GITEA-OTP'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-GITEA-OTP'] = 'Bearer'
# Configure API key authorization: Token
configuration = dcs_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = dcs_api_client.CatalogApi(dcs_api_client.ApiClient(configuration))
owner = 'owner_example' # str | list only lannguages with entries in the given owners(s). To match multiple, give the parameter multiple times or give a list comma delimited. Will perform an exact match (case insensitive) unlesss partialMatch=true (optional)
lang = 'lang_example' # str | list only the given languages(s) if they have entries in the catalog meeting the criteria given (e.g. way to test an language has a given owner and/or subject) (optional)
stage = 'stage_example' # str | list only languages of the given stage or lower, with low to high being: \"prod\" - return only the production subjects (default); \"preprod\" - return pre-production and production subjects; \"draft\" - return only draft, pre-product and production subjects; \"latest\" - return all subjects in the catalog for all stages (optional)
subject = 'subject_example' # str | list only languages with the the given subject(s). Multiple resources are ORed. (optional)
resource = 'resource_example' # str | list only languages with the given resource identifier(s). Multiple resources are ORed. (optional)
format = 'format_example' # str | list only languages with the given content format (usfm, text, markdown, etc.). Multiple formats are ORed. (optional)
checking_level = 'checking_level_example' # str | list only for languages with the given checking level(s). Can be 1, 2 or 3 (optional)
book = 'book_example' # str | list only languages with the given book(s) (project ids). To match multiple, give the parameter multiple times or give a list comma delimited. Will perform an exact match (case insensitive) (optional)
metadata_type = 'metadata_type_example' # str | list only languages with the given metadata type (e.g. rc, tc, ts, sb). . <empty> or \"all\" for all. Default is rc (optional)
metadata_version = 'metadata_version_example' # str | list only languages with the  given metadatay version. Does not apply if metadataType is \"all\" or empty (optional)
direction = 'direction_example' # str | list only languages of the given language direction, \"ltr\" or \"rtl\". (optional)
is_gl = true # bool | list only languages of they are (true) or are not (false) a gatetway language. (optional)
partial_match = true # bool | if true, owner, language and subject search fields will use partial match (LIKE) when querying the catalog. Default is false (optional)

try:
    # Catalog list owners
    api_response = api_instance.catalog_list_languages(owner=owner, lang=lang, stage=stage, subject=subject, resource=resource, format=format, checking_level=checking_level, book=book, metadata_type=metadata_type, metadata_version=metadata_version, direction=direction, is_gl=is_gl, partial_match=partial_match)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogApi->catalog_list_languages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| list only lannguages with entries in the given owners(s). To match multiple, give the parameter multiple times or give a list comma delimited. Will perform an exact match (case insensitive) unlesss partialMatch&#x3D;true | [optional] 
 **lang** | **str**| list only the given languages(s) if they have entries in the catalog meeting the criteria given (e.g. way to test an language has a given owner and/or subject) | [optional] 
 **stage** | **str**| list only languages of the given stage or lower, with low to high being: \&quot;prod\&quot; - return only the production subjects (default); \&quot;preprod\&quot; - return pre-production and production subjects; \&quot;draft\&quot; - return only draft, pre-product and production subjects; \&quot;latest\&quot; - return all subjects in the catalog for all stages | [optional] 
 **subject** | **str**| list only languages with the the given subject(s). Multiple resources are ORed. | [optional] 
 **resource** | **str**| list only languages with the given resource identifier(s). Multiple resources are ORed. | [optional] 
 **format** | **str**| list only languages with the given content format (usfm, text, markdown, etc.). Multiple formats are ORed. | [optional] 
 **checking_level** | **str**| list only for languages with the given checking level(s). Can be 1, 2 or 3 | [optional] 
 **book** | **str**| list only languages with the given book(s) (project ids). To match multiple, give the parameter multiple times or give a list comma delimited. Will perform an exact match (case insensitive) | [optional] 
 **metadata_type** | **str**| list only languages with the given metadata type (e.g. rc, tc, ts, sb). . &lt;empty&gt; or \&quot;all\&quot; for all. Default is rc | [optional] 
 **metadata_version** | **str**| list only languages with the  given metadatay version. Does not apply if metadataType is \&quot;all\&quot; or empty | [optional] 
 **direction** | **str**| list only languages of the given language direction, \&quot;ltr\&quot; or \&quot;rtl\&quot;. | [optional] 
 **is_gl** | **bool**| list only languages of they are (true) or are not (false) a gatetway language. | [optional] 
 **partial_match** | **bool**| if true, owner, language and subject search fields will use partial match (LIKE) when querying the catalog. Default is false | [optional] 

### Return type

**list[str]**

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **catalog_list_subjects**
> list[str] catalog_list_subjects(owner=owner, lang=lang, stage=stage, subject=subject, resource=resource, format=format, checking_level=checking_level, book=book, metadata_type=metadata_type, metadata_version=metadata_version, partial_match=partial_match)

Catalog list subjects

### Example
```python
from __future__ import print_function
import time
import dcs_api_client
from dcs_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = dcs_api_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: AuthorizationHeaderToken
configuration = dcs_api_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = dcs_api_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: SudoHeader
configuration = dcs_api_client.Configuration()
configuration.api_key['Sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Sudo'] = 'Bearer'
# Configure API key authorization: SudoParam
configuration = dcs_api_client.Configuration()
configuration.api_key['sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo'] = 'Bearer'
# Configure API key authorization: TOTPHeader
configuration = dcs_api_client.Configuration()
configuration.api_key['X-GITEA-OTP'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-GITEA-OTP'] = 'Bearer'
# Configure API key authorization: Token
configuration = dcs_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = dcs_api_client.CatalogApi(dcs_api_client.ApiClient(configuration))
owner = 'owner_example' # str | list only subjects in the given owner(s). To match multiple, give the parameter multiple times or give a list comma delimited. (optional)
lang = 'lang_example' # str | list only subjects in the given language(s). To match multiple, give the parameter multiple times or give a list comma delimited. Will perform an exact match (case insensitive) unlesss partialMatch=true (optional)
stage = 'stage_example' # str | list only subjects of the given stage or lower, with low to high being: \"prod\" - return only the production subjects (default); \"preprod\" - return pre-production and production subjects; \"draft\" - return only draft, pre-product and production subjects; \"latest\" - return all subjects in the catalog for all stages (optional)
subject = 'subject_example' # str | list only the given subjects if they are in the catalog meeting the criteria given (e.g. way to test a given language has the given subject) (optional)
resource = 'resource_example' # str | list only subjects with the given resource identifier. Multiple resources are ORed. (optional)
format = 'format_example' # str | list only subjects with the given content format (usfm, text, markdown, etc.). Multiple formats are ORed. (optional)
checking_level = 'checking_level_example' # str | list only for subjects with the given checking level(s). Can be 1, 2 or 3 (optional)
book = 'book_example' # str | list only subjects with the given book(s) (project ids). To match multiple, give the parameter multiple times or give a list comma delimited. Will perform an exact match (case insensitive) (optional)
metadata_type = 'metadata_type_example' # str | list only subjects with the given metadata type (e.g. rc, tc, ts, sb). . <empty> or \"all\" for all. Default is rc (optional)
metadata_version = 'metadata_version_example' # str | list only subjects with the  given metadatay version. Does not apply if metadataType is \"all\" or empty (optional)
partial_match = true # bool | if true, owner, subject and language search fields will use partial match (LIKE) when querying the catalog. Default is false (optional)

try:
    # Catalog list subjects
    api_response = api_instance.catalog_list_subjects(owner=owner, lang=lang, stage=stage, subject=subject, resource=resource, format=format, checking_level=checking_level, book=book, metadata_type=metadata_type, metadata_version=metadata_version, partial_match=partial_match)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogApi->catalog_list_subjects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| list only subjects in the given owner(s). To match multiple, give the parameter multiple times or give a list comma delimited. | [optional] 
 **lang** | **str**| list only subjects in the given language(s). To match multiple, give the parameter multiple times or give a list comma delimited. Will perform an exact match (case insensitive) unlesss partialMatch&#x3D;true | [optional] 
 **stage** | **str**| list only subjects of the given stage or lower, with low to high being: \&quot;prod\&quot; - return only the production subjects (default); \&quot;preprod\&quot; - return pre-production and production subjects; \&quot;draft\&quot; - return only draft, pre-product and production subjects; \&quot;latest\&quot; - return all subjects in the catalog for all stages | [optional] 
 **subject** | **str**| list only the given subjects if they are in the catalog meeting the criteria given (e.g. way to test a given language has the given subject) | [optional] 
 **resource** | **str**| list only subjects with the given resource identifier. Multiple resources are ORed. | [optional] 
 **format** | **str**| list only subjects with the given content format (usfm, text, markdown, etc.). Multiple formats are ORed. | [optional] 
 **checking_level** | **str**| list only for subjects with the given checking level(s). Can be 1, 2 or 3 | [optional] 
 **book** | **str**| list only subjects with the given book(s) (project ids). To match multiple, give the parameter multiple times or give a list comma delimited. Will perform an exact match (case insensitive) | [optional] 
 **metadata_type** | **str**| list only subjects with the given metadata type (e.g. rc, tc, ts, sb). . &lt;empty&gt; or \&quot;all\&quot; for all. Default is rc | [optional] 
 **metadata_version** | **str**| list only subjects with the  given metadatay version. Does not apply if metadataType is \&quot;all\&quot; or empty | [optional] 
 **partial_match** | **bool**| if true, owner, subject and language search fields will use partial match (LIKE) when querying the catalog. Default is false | [optional] 

### Return type

**list[str]**

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **catalog_search**
> CatalogSearchResults catalog_search(q=q, owner=owner, repo=repo, tag=tag, lang=lang, stage=stage, subject=subject, resource=resource, format=format, checking_level=checking_level, book=book, metadata_type=metadata_type, metadata_version=metadata_version, partial_match=partial_match, include_history=include_history, show_ingredients=show_ingredients, sort=sort, order=order, page=page, limit=limit)

Catalog search

### Example
```python
from __future__ import print_function
import time
import dcs_api_client
from dcs_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = dcs_api_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: AuthorizationHeaderToken
configuration = dcs_api_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = dcs_api_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: SudoHeader
configuration = dcs_api_client.Configuration()
configuration.api_key['Sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Sudo'] = 'Bearer'
# Configure API key authorization: SudoParam
configuration = dcs_api_client.Configuration()
configuration.api_key['sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo'] = 'Bearer'
# Configure API key authorization: TOTPHeader
configuration = dcs_api_client.Configuration()
configuration.api_key['X-GITEA-OTP'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-GITEA-OTP'] = 'Bearer'
# Configure API key authorization: Token
configuration = dcs_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = dcs_api_client.CatalogApi(dcs_api_client.ApiClient(configuration))
q = 'q_example' # str | keyword(s). Can use multiple `q=<keyword>`s or a comma-delimited string for more than one keyword. Is case insensitive (optional)
owner = 'owner_example' # str | search only for entries with the given owner name(s). Will perform an exact match (case insensitive) unlesss partialMatch=true (optional)
repo = 'repo_example' # str | search only for entries with the given repo name(s). To match multiple, give the parameter multiple times or give a list comma delimited. Will perform an exact match (case insensitive) unlesss partialMatch=true (optional)
tag = 'tag_example' # str | search only for entries with the given release tag(s). To match multiple, give the parameter multiple times or give a list comma delimited. Will perform an exact match (case insensitive) (optional)
lang = 'lang_example' # str | search only for entries with the given language(s). To match multiple, give the parameter multiple times or give a list comma delimited. Will perform an exact match (case insensitive) unlesss partialMatch=true (optional)
stage = 'stage_example' # str | specifies which release stage to be return of these stages: \"prod\" - return only the production releases (default); \"preprod\" - return the pre-production release if it exists instead of the production release; \"draft\" - return the draft release if it exists instead of pre-production or production release; \"latest\" - return the default branch (e.g. master) if it is a valid RC instead of the above (optional)
subject = 'subject_example' # str | search only for entries with the given subject(s). To match multiple, give the parameter multiple times or give a list comma delimited. Will perform an exact match (case insensitive) unlesss partialMatch=true (optional)
resource = 'resource_example' # str | resource identifier. Multiple resources are ORed. (optional)
format = 'format_example' # str | content format (usfm, text, markdown, etc.). Multiple formats are ORed. (optional)
checking_level = 'checking_level_example' # str | search only for entries with the given checking level(s). Can be 1, 2 or 3 (optional)
book = 'book_example' # str | search only for entries with the given book(s) (project ids). To match multiple, give the parameter multiple times or give a list comma delimited. Will perform an exact match (case insensitive) (optional)
metadata_type = 'metadata_type_example' # str | return repos only with metadata of this type (e.g. rc, tc, ts, sb). <empty> or \"all\" for all. Default is rc (optional)
metadata_version = 'metadata_version_example' # str | return repos only with the version of metadata given. Does not apply if metadataType is \"all\" (optional)
partial_match = true # bool | if true, subject, owner and repo search fields will use partial match (LIKE) when querying the catalog. Default is false (optional)
include_history = true # bool | if true, all releases, not just the latest, are included. Default is false (optional)
show_ingredients = true # bool | if true, the list of ingredients (files/projects) in the resource and their file paths will be listed for each entry. Default is true (optional)
sort = 'sort_example' # str | sort repos alphanumerically by attribute. Supported values are \"subject\", \"title\", \"reponame\", \"tag\", \"released\", \"lang\", \"releases\", \"stars\", \"forks\". Default is by \"language\", \"subject\" and then \"tag\" (optional)
order = 'order_example' # str | sort order, either \"asc\" (ascending) or \"desc\" (descending). Default is \"asc\", ignored if \"sort\" is not specified. (optional)
page = 56 # int | page number of results to return (1-based) (optional)
limit = 56 # int | page size of results, defaults to no limit (optional)

try:
    # Catalog search
    api_response = api_instance.catalog_search(q=q, owner=owner, repo=repo, tag=tag, lang=lang, stage=stage, subject=subject, resource=resource, format=format, checking_level=checking_level, book=book, metadata_type=metadata_type, metadata_version=metadata_version, partial_match=partial_match, include_history=include_history, show_ingredients=show_ingredients, sort=sort, order=order, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogApi->catalog_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| keyword(s). Can use multiple &#x60;q&#x3D;&lt;keyword&gt;&#x60;s or a comma-delimited string for more than one keyword. Is case insensitive | [optional] 
 **owner** | **str**| search only for entries with the given owner name(s). Will perform an exact match (case insensitive) unlesss partialMatch&#x3D;true | [optional] 
 **repo** | **str**| search only for entries with the given repo name(s). To match multiple, give the parameter multiple times or give a list comma delimited. Will perform an exact match (case insensitive) unlesss partialMatch&#x3D;true | [optional] 
 **tag** | **str**| search only for entries with the given release tag(s). To match multiple, give the parameter multiple times or give a list comma delimited. Will perform an exact match (case insensitive) | [optional] 
 **lang** | **str**| search only for entries with the given language(s). To match multiple, give the parameter multiple times or give a list comma delimited. Will perform an exact match (case insensitive) unlesss partialMatch&#x3D;true | [optional] 
 **stage** | **str**| specifies which release stage to be return of these stages: \&quot;prod\&quot; - return only the production releases (default); \&quot;preprod\&quot; - return the pre-production release if it exists instead of the production release; \&quot;draft\&quot; - return the draft release if it exists instead of pre-production or production release; \&quot;latest\&quot; - return the default branch (e.g. master) if it is a valid RC instead of the above | [optional] 
 **subject** | **str**| search only for entries with the given subject(s). To match multiple, give the parameter multiple times or give a list comma delimited. Will perform an exact match (case insensitive) unlesss partialMatch&#x3D;true | [optional] 
 **resource** | **str**| resource identifier. Multiple resources are ORed. | [optional] 
 **format** | **str**| content format (usfm, text, markdown, etc.). Multiple formats are ORed. | [optional] 
 **checking_level** | **str**| search only for entries with the given checking level(s). Can be 1, 2 or 3 | [optional] 
 **book** | **str**| search only for entries with the given book(s) (project ids). To match multiple, give the parameter multiple times or give a list comma delimited. Will perform an exact match (case insensitive) | [optional] 
 **metadata_type** | **str**| return repos only with metadata of this type (e.g. rc, tc, ts, sb). &lt;empty&gt; or \&quot;all\&quot; for all. Default is rc | [optional] 
 **metadata_version** | **str**| return repos only with the version of metadata given. Does not apply if metadataType is \&quot;all\&quot; | [optional] 
 **partial_match** | **bool**| if true, subject, owner and repo search fields will use partial match (LIKE) when querying the catalog. Default is false | [optional] 
 **include_history** | **bool**| if true, all releases, not just the latest, are included. Default is false | [optional] 
 **show_ingredients** | **bool**| if true, the list of ingredients (files/projects) in the resource and their file paths will be listed for each entry. Default is true | [optional] 
 **sort** | **str**| sort repos alphanumerically by attribute. Supported values are \&quot;subject\&quot;, \&quot;title\&quot;, \&quot;reponame\&quot;, \&quot;tag\&quot;, \&quot;released\&quot;, \&quot;lang\&quot;, \&quot;releases\&quot;, \&quot;stars\&quot;, \&quot;forks\&quot;. Default is by \&quot;language\&quot;, \&quot;subject\&quot; and then \&quot;tag\&quot; | [optional] 
 **order** | **str**| sort order, either \&quot;asc\&quot; (ascending) or \&quot;desc\&quot; (descending). Default is \&quot;asc\&quot;, ignored if \&quot;sort\&quot; is not specified. | [optional] 
 **page** | **int**| page number of results to return (1-based) | [optional] 
 **limit** | **int**| page size of results, defaults to no limit | [optional] 

### Return type

[**CatalogSearchResults**](CatalogSearchResults.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **catalog_search_owner**
> CatalogSearchResults catalog_search_owner(owner, q=q, repo=repo, tag=tag, lang=lang, stage=stage, subject=subject, resource=resource, format=format, checking_level=checking_level, book=book, metadata_type=metadata_type, metadata_version=metadata_version, partial_match=partial_match, include_history=include_history, show_ingredients=show_ingredients, sort=sort, order=order, page=page, limit=limit)

Catalog search by owner

### Example
```python
from __future__ import print_function
import time
import dcs_api_client
from dcs_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = dcs_api_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: AuthorizationHeaderToken
configuration = dcs_api_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = dcs_api_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: SudoHeader
configuration = dcs_api_client.Configuration()
configuration.api_key['Sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Sudo'] = 'Bearer'
# Configure API key authorization: SudoParam
configuration = dcs_api_client.Configuration()
configuration.api_key['sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo'] = 'Bearer'
# Configure API key authorization: TOTPHeader
configuration = dcs_api_client.Configuration()
configuration.api_key['X-GITEA-OTP'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-GITEA-OTP'] = 'Bearer'
# Configure API key authorization: Token
configuration = dcs_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = dcs_api_client.CatalogApi(dcs_api_client.ApiClient(configuration))
owner = 'owner_example' # str | owner of the returned entries
q = 'q_example' # str | keyword(s). Can use multiple `q=<keyword>`s or a comma-delimited string for more than one keyword. Is case insensitive (optional)
repo = 'repo_example' # str | search only for entries with the given repo name(s). To match multiple, give the parameter multiple times or give a list comma delimited. Will perform an exact match (case insensitive) unlesss partialMatch=true (optional)
tag = 'tag_example' # str | search only for entries with the given release tag(s). To match multiple, give the parameter multiple times or give a list comma delimited. Will perform an exact match (case insensitive) (optional)
lang = 'lang_example' # str | search only for entries with the given language(s). To match multiple, give the parameter multiple times or give a list comma delimited. Will perform an exact match (case insensitive) unlesss partialMatch=true (optional)
stage = 'stage_example' # str | specifies which release stage to be return of these stages: \"prod\" - return only the production releases (default); \"preprod\" - return the pre-production release if it exists instead of the production release; \"draft\" - return the draft release if it exists instead of pre-production or production release; \"latest\" -return the default branch (e.g. master) if it is a valid RC instead of the above (optional)
subject = 'subject_example' # str | search only for entries with the given subject(s). To match multiple, give the parameter multiple times or give a list comma delimited. Will perform an exact match (case insensitive) unlesss partialMatch=true (optional)
resource = 'resource_example' # str | resource identifier. Multiple resources are ORed. (optional)
format = 'format_example' # str | content format (usfm, text, markdown, etc.). Multiple formats are ORed. (optional)
checking_level = 'checking_level_example' # str | search only for entries with the given checking level(s). Can be 1, 2 or 3 (optional)
book = 'book_example' # str | search only for entries with the given book(s) (project ids). To match multiple, give the parameter multiple times or give a list comma delimited. Will perform an exact match (case insensitive) (optional)
metadata_type = 'metadata_type_example' # str | return repos only with metadata of this type (e.g. rc, tc, ts, sb). . <empty> or \"all\" for all. Default is rc (optional)
metadata_version = 'metadata_version_example' # str | return repos only with the version of metadata given. Does not apply if metadataType is \"all\" (optional)
partial_match = true # bool | if true, subject, owner and repo search fields will use partial match (LIKE) when querying the catalog. Default is false (optional)
include_history = true # bool | if true, all releases, not just the latest, are included. Default is false (optional)
show_ingredients = true # bool | if true, the list of ingredients (files/projects) in the resource and their file paths will be listed for each entry. Default is true (optional)
sort = 'sort_example' # str | sort repos alphanumerically by attribute. Supported values are \"subject\", \"title\", \"reponame\", \"tag\", \"released\", \"lang\", \"releases\", \"stars\", \"forks\". Default is by \"language\", \"subject\" and then \"tag\" (optional)
order = 'order_example' # str | sort order, either \"asc\" (ascending) or \"desc\" (descending). Default is \"asc\", ignored if \"sort\" is not specified. (optional)
page = 56 # int | page number of results to return (1-based) (optional)
limit = 56 # int | page size of results, defaults to no limit (optional)

try:
    # Catalog search by owner
    api_response = api_instance.catalog_search_owner(owner, q=q, repo=repo, tag=tag, lang=lang, stage=stage, subject=subject, resource=resource, format=format, checking_level=checking_level, book=book, metadata_type=metadata_type, metadata_version=metadata_version, partial_match=partial_match, include_history=include_history, show_ingredients=show_ingredients, sort=sort, order=order, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogApi->catalog_search_owner: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the returned entries | 
 **q** | **str**| keyword(s). Can use multiple &#x60;q&#x3D;&lt;keyword&gt;&#x60;s or a comma-delimited string for more than one keyword. Is case insensitive | [optional] 
 **repo** | **str**| search only for entries with the given repo name(s). To match multiple, give the parameter multiple times or give a list comma delimited. Will perform an exact match (case insensitive) unlesss partialMatch&#x3D;true | [optional] 
 **tag** | **str**| search only for entries with the given release tag(s). To match multiple, give the parameter multiple times or give a list comma delimited. Will perform an exact match (case insensitive) | [optional] 
 **lang** | **str**| search only for entries with the given language(s). To match multiple, give the parameter multiple times or give a list comma delimited. Will perform an exact match (case insensitive) unlesss partialMatch&#x3D;true | [optional] 
 **stage** | **str**| specifies which release stage to be return of these stages: \&quot;prod\&quot; - return only the production releases (default); \&quot;preprod\&quot; - return the pre-production release if it exists instead of the production release; \&quot;draft\&quot; - return the draft release if it exists instead of pre-production or production release; \&quot;latest\&quot; -return the default branch (e.g. master) if it is a valid RC instead of the above | [optional] 
 **subject** | **str**| search only for entries with the given subject(s). To match multiple, give the parameter multiple times or give a list comma delimited. Will perform an exact match (case insensitive) unlesss partialMatch&#x3D;true | [optional] 
 **resource** | **str**| resource identifier. Multiple resources are ORed. | [optional] 
 **format** | **str**| content format (usfm, text, markdown, etc.). Multiple formats are ORed. | [optional] 
 **checking_level** | **str**| search only for entries with the given checking level(s). Can be 1, 2 or 3 | [optional] 
 **book** | **str**| search only for entries with the given book(s) (project ids). To match multiple, give the parameter multiple times or give a list comma delimited. Will perform an exact match (case insensitive) | [optional] 
 **metadata_type** | **str**| return repos only with metadata of this type (e.g. rc, tc, ts, sb). . &lt;empty&gt; or \&quot;all\&quot; for all. Default is rc | [optional] 
 **metadata_version** | **str**| return repos only with the version of metadata given. Does not apply if metadataType is \&quot;all\&quot; | [optional] 
 **partial_match** | **bool**| if true, subject, owner and repo search fields will use partial match (LIKE) when querying the catalog. Default is false | [optional] 
 **include_history** | **bool**| if true, all releases, not just the latest, are included. Default is false | [optional] 
 **show_ingredients** | **bool**| if true, the list of ingredients (files/projects) in the resource and their file paths will be listed for each entry. Default is true | [optional] 
 **sort** | **str**| sort repos alphanumerically by attribute. Supported values are \&quot;subject\&quot;, \&quot;title\&quot;, \&quot;reponame\&quot;, \&quot;tag\&quot;, \&quot;released\&quot;, \&quot;lang\&quot;, \&quot;releases\&quot;, \&quot;stars\&quot;, \&quot;forks\&quot;. Default is by \&quot;language\&quot;, \&quot;subject\&quot; and then \&quot;tag\&quot; | [optional] 
 **order** | **str**| sort order, either \&quot;asc\&quot; (ascending) or \&quot;desc\&quot; (descending). Default is \&quot;asc\&quot;, ignored if \&quot;sort\&quot; is not specified. | [optional] 
 **page** | **int**| page number of results to return (1-based) | [optional] 
 **limit** | **int**| page size of results, defaults to no limit | [optional] 

### Return type

[**CatalogSearchResults**](CatalogSearchResults.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **catalog_search_repo**
> CatalogSearchResults catalog_search_repo(owner, repo, q=q, owner2=owner2, repo2=repo2, tag=tag, lang=lang, stage=stage, subject=subject, resource=resource, format=format, checking_level=checking_level, book=book, metadata_type=metadata_type, metadata_version=metadata_version, partial_match=partial_match, include_history=include_history, show_ingredients=show_ingredients, sort=sort, order=order, page=page, limit=limit)

Catalog search by repo

### Example
```python
from __future__ import print_function
import time
import dcs_api_client
from dcs_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = dcs_api_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: AuthorizationHeaderToken
configuration = dcs_api_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = dcs_api_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: SudoHeader
configuration = dcs_api_client.Configuration()
configuration.api_key['Sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Sudo'] = 'Bearer'
# Configure API key authorization: SudoParam
configuration = dcs_api_client.Configuration()
configuration.api_key['sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo'] = 'Bearer'
# Configure API key authorization: TOTPHeader
configuration = dcs_api_client.Configuration()
configuration.api_key['X-GITEA-OTP'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-GITEA-OTP'] = 'Bearer'
# Configure API key authorization: Token
configuration = dcs_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = dcs_api_client.CatalogApi(dcs_api_client.ApiClient(configuration))
owner = 'owner_example' # str | owner of the returned entries
repo = 'repo_example' # str | name of the repo of the returned entries
q = 'q_example' # str | keyword(s). Can use multiple `q=<keyword>`s or a comma-delimited string for more than one keyword. Is case insensitive (optional)
owner2 = 'owner_example' # str | search only for entries with the given owner name(s). Will perform an exact match (case insensitive) unlesss partialMatch=true (optional)
repo2 = 'repo_example' # str | search only for entries with the given repo name(s). To match multiple, give the parameter multiple times or give a list comma delimited. Will perform an exact match (case insensitive) unlesss partialMatch=true (optional)
tag = 'tag_example' # str | search only for entries with the given release tag(s). To match multiple, give the parameter multiple times or give a list comma delimited. Will perform an exact match (case insensitive) (optional)
lang = 'lang_example' # str | search only for entries with the given language(s). To match multiple, give the parameter multiple times or give a list comma delimited. Will perform an exact match (case insensitive) unlesss partialMatch=true (optional)
stage = 'stage_example' # str | specifies which release stage to be return of these stages: \"prod\" - return only the production releases (default); \"preprod\" - return the pre-production release if it exists instead of the production release; \"draft\" - return the draft release if it exists instead of pre-production or production release; \"latest\" -return the default branch (e.g. master) if it is a valid RC instead of the above (optional)
subject = 'subject_example' # str | search only for entries with the given subject(s). To match multiple, give the parameter multiple times or give a list comma delimited. Will perform an exact match (case insensitive) unlesss partialMatch=true (optional)
resource = 'resource_example' # str | resource identifier. Multiple resources are ORed. (optional)
format = 'format_example' # str | content format (usfm, text, markdown, etc.). Multiple formats are ORed. (optional)
checking_level = 'checking_level_example' # str | search only for entries with the given checking level(s). Can be 1, 2 or 3 (optional)
book = 'book_example' # str | search only for entries with the given book(s) (project ids). To match multiple, give the parameter multiple times or give a list comma delimited. Will perform an exact match (case insensitive) (optional)
metadata_type = 'metadata_type_example' # str | return repos only with metadata of this type (e.g. rc, tc, ts, sb). <empty> or \"all\" for all. Default is rc (optional)
metadata_version = 'metadata_version_example' # str | return repos only with the version of metadata given. Does not apply if metadataType is \"all\" (optional)
partial_match = true # bool | if true, subject, owner and repo search fields will use partial match (LIKE) when querying the catalog. Default is false (optional)
include_history = true # bool | if true, all releases, not just the latest, are included. Default is false (optional)
show_ingredients = true # bool | if true, the list of ingredients (files/projects) in the resource and their file paths will be listed for each entry. Default is true (optional)
sort = 'sort_example' # str | sort repos alphanumerically by attribute. Supported values are \"subject\", \"title\", \"reponame\", \"tag\", \"released\", \"lang\", \"releases\", \"stars\", \"forks\". Default is by \"language\", \"subject\" and then \"tag\" (optional)
order = 'order_example' # str | sort order, either \"asc\" (ascending) or \"desc\" (descending). Default is \"asc\", ignored if \"sort\" is not specified. (optional)
page = 56 # int | page number of results to return (1-based) (optional)
limit = 56 # int | page size of results, defaults to no limit (optional)

try:
    # Catalog search by repo
    api_response = api_instance.catalog_search_repo(owner, repo, q=q, owner2=owner2, repo2=repo2, tag=tag, lang=lang, stage=stage, subject=subject, resource=resource, format=format, checking_level=checking_level, book=book, metadata_type=metadata_type, metadata_version=metadata_version, partial_match=partial_match, include_history=include_history, show_ingredients=show_ingredients, sort=sort, order=order, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogApi->catalog_search_repo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the returned entries | 
 **repo** | **str**| name of the repo of the returned entries | 
 **q** | **str**| keyword(s). Can use multiple &#x60;q&#x3D;&lt;keyword&gt;&#x60;s or a comma-delimited string for more than one keyword. Is case insensitive | [optional] 
 **owner2** | **str**| search only for entries with the given owner name(s). Will perform an exact match (case insensitive) unlesss partialMatch&#x3D;true | [optional] 
 **repo2** | **str**| search only for entries with the given repo name(s). To match multiple, give the parameter multiple times or give a list comma delimited. Will perform an exact match (case insensitive) unlesss partialMatch&#x3D;true | [optional] 
 **tag** | **str**| search only for entries with the given release tag(s). To match multiple, give the parameter multiple times or give a list comma delimited. Will perform an exact match (case insensitive) | [optional] 
 **lang** | **str**| search only for entries with the given language(s). To match multiple, give the parameter multiple times or give a list comma delimited. Will perform an exact match (case insensitive) unlesss partialMatch&#x3D;true | [optional] 
 **stage** | **str**| specifies which release stage to be return of these stages: \&quot;prod\&quot; - return only the production releases (default); \&quot;preprod\&quot; - return the pre-production release if it exists instead of the production release; \&quot;draft\&quot; - return the draft release if it exists instead of pre-production or production release; \&quot;latest\&quot; -return the default branch (e.g. master) if it is a valid RC instead of the above | [optional] 
 **subject** | **str**| search only for entries with the given subject(s). To match multiple, give the parameter multiple times or give a list comma delimited. Will perform an exact match (case insensitive) unlesss partialMatch&#x3D;true | [optional] 
 **resource** | **str**| resource identifier. Multiple resources are ORed. | [optional] 
 **format** | **str**| content format (usfm, text, markdown, etc.). Multiple formats are ORed. | [optional] 
 **checking_level** | **str**| search only for entries with the given checking level(s). Can be 1, 2 or 3 | [optional] 
 **book** | **str**| search only for entries with the given book(s) (project ids). To match multiple, give the parameter multiple times or give a list comma delimited. Will perform an exact match (case insensitive) | [optional] 
 **metadata_type** | **str**| return repos only with metadata of this type (e.g. rc, tc, ts, sb). &lt;empty&gt; or \&quot;all\&quot; for all. Default is rc | [optional] 
 **metadata_version** | **str**| return repos only with the version of metadata given. Does not apply if metadataType is \&quot;all\&quot; | [optional] 
 **partial_match** | **bool**| if true, subject, owner and repo search fields will use partial match (LIKE) when querying the catalog. Default is false | [optional] 
 **include_history** | **bool**| if true, all releases, not just the latest, are included. Default is false | [optional] 
 **show_ingredients** | **bool**| if true, the list of ingredients (files/projects) in the resource and their file paths will be listed for each entry. Default is true | [optional] 
 **sort** | **str**| sort repos alphanumerically by attribute. Supported values are \&quot;subject\&quot;, \&quot;title\&quot;, \&quot;reponame\&quot;, \&quot;tag\&quot;, \&quot;released\&quot;, \&quot;lang\&quot;, \&quot;releases\&quot;, \&quot;stars\&quot;, \&quot;forks\&quot;. Default is by \&quot;language\&quot;, \&quot;subject\&quot; and then \&quot;tag\&quot; | [optional] 
 **order** | **str**| sort order, either \&quot;asc\&quot; (ascending) or \&quot;desc\&quot; (descending). Default is \&quot;asc\&quot;, ignored if \&quot;sort\&quot; is not specified. | [optional] 
 **page** | **int**| page number of results to return (1-based) | [optional] 
 **limit** | **int**| page size of results, defaults to no limit | [optional] 

### Return type

[**CatalogSearchResults**](CatalogSearchResults.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

