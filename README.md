# Keymate-API


<!-- Start SDK Installation -->
# SDK Installation

```bash
pip install Keymate-API==0.1.0 # ONLY USE 0.1.0
```
<!-- End SDK Installation -->

## SDK Example Usage
<!-- Start SDK Example Usage -->

Only search and browse like the example below works on this sdk for more operations refer to this openapi.json https://server.searchweb.keymate.ai/.well-known/openapi.json input parameters are correct but I always recommend you to parse responses manually because they might change quickly.
```python

import keymate_api
from keymate_api.models import operations

s = keymate_api.KeymateAPI(
    bearer_auth="",
)


res = s.search(numofpages='3', percentile='3', q='bitcoin')

if res.two_hundred_application_json_object is not None:
    # handle response
    pass

res = s.search(numofpages='1', percentile='1', q='https://news.ycombinator.com')

if res.two_hundred_application_json_object is not None:
    # handle response
    pass

```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
# Available Resources and Operations

## [KeymateAPI SDK](docs/sdks/keymateapi/README.md)

* [search](docs/sdks/keymateapi/README.md#search) - Search Google and fetch HTML content and PDF summary content from the links at the same time in one go.
* [search_and_browse](docs/sdks/keymateapi/README.md#search_and_browse) - Search Google and fetch HTML content and PDF summary content from the links at the same time in one go.
* [ultrafastsearch](docs/sdks/keymateapi/README.md#ultrafastsearch) - This plugin provides 10 ultra fast search results from multiple sources giving a more comprehensive view.

<!-- End SDK Available Operations -->

<!-- Start Dev Containers -->



<!-- End Dev Containers -->

<!-- Start Error Handling -->
# Error Handling

Handling errors in your SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.


## Example

```python
import keymate_api
from keymate_api.models import operations

s = keymate_api.KeymateAPI(
    bearer_auth="",
)


res = None
try:
    res = s.search(numofpages='string', percentile='string', q='http://impressive-silence.info')

except (400_application/json_object) as e:
    print(e) # handle exception



if res.two_hundred_application_json_object is not None:
    # handle response
    pass
```
<!-- End Error Handling -->

<!-- Start Server Selection -->
# Server Selection

## Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `https://server.searchweb.keymate.ai` | None |

For example:

```python
import keymate_api
from keymate_api.models import operations

s = keymate_api.KeymateAPI(
    server_idx=0,
    bearer_auth="",
)


res = s.search(numofpages='string', percentile='string', q='http://impressive-silence.info')

if res.two_hundred_application_json_object is not None:
    # handle response
    pass
```


## Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:

```python
import keymate_api
from keymate_api.models import operations

s = keymate_api.KeymateAPI(
    server_url="https://server.searchweb.keymate.ai",
    bearer_auth="",
)


res = s.search(numofpages='string', percentile='string', q='http://impressive-silence.info')

if res.two_hundred_application_json_object is not None:
    # handle response
    pass
```
<!-- End Server Selection -->

<!-- Start Custom HTTP Client -->
# Custom HTTP Client

The Python SDK makes API calls using the (requests)[https://pypi.org/project/requests/] HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.


For example, you could specify a header for every request that your sdk makes as follows:

```python
import keymate_api
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = keymate_api.KeymateAPI(client: http_client)
```


<!-- End Custom HTTP Client -->

<!-- Start Authentication -->

# Authentication

## Per-Client Security Schemes

Your SDK supports the following security scheme globally:

| Name          | Type          | Scheme        |
| ------------- | ------------- | ------------- |
| `bearer_auth` | http          | HTTP Bearer   |

To authenticate with the API the `bearer_auth` parameter must be set when initializing the SDK client instance. For example:

```python
import keymate_api
from keymate_api.models import operations

s = keymate_api.KeymateAPI(
    bearer_auth="",
)


res = s.search(numofpages='string', percentile='string', q='http://impressive-silence.info')

if res.two_hundred_application_json_object is not None:
    # handle response
    pass
```
<!-- End Authentication -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release!

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
