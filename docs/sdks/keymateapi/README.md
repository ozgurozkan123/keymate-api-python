# Keymateapi SDK


## Overview

Keymate.AI Web Search API: Enhances knowledge grounded responses by fetching URLs optimized for specific needs and performing authenticated internet searches.

### Available Operations

* [upsert](#upsert) - Inserts record to Keymate Memory.
* [query](#query) - Queries the user's Keymate Memory.
* [browseurl](#browseurl) - The plugin enables user to conduct web browsing by extracting the text content of a specified URL. It will generate title and content.
* [browse](#browse) - Fetch any URLs without proxy it would probably fail on major websites but quicker than browseurl 
* [search](#search) - Without proxies searches keyword on the internet and fetches urls and optimizes output
* [ultrafastsearch](#ultrafastsearch) - This plugin provides 10 ultra fast search results from multiple sources giving a more comprehensive view.
* [gptsbrowse](#gptsbrowse) - Fetch memory.keymate.ai URLs
* [internetsearch](#internetsearch) - Conduct an internet search

## upsert

It records the passed string in q parameter to keymate memory

### Example Usage

```python
import keymateapi

s = keymateapi.Keymateapi(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.upsert(q='I prefer Costa over Starbucks.')

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             | Example                                                                 |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `q`                                                                     | *str*                                                                   | :heavy_check_mark:                                                      | The context you are insertin to user's personal Keymate Memory history. | I prefer Costa over Starbucks.                                          |


### Response

**[operations.UpsertResponse](../../models/operations/upsertresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## query

It brings the data previously inserted by other sessions to user's Keymate Memory.

### Example Usage

```python
import keymateapi

s = keymateapi.Keymateapi(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.query(q='https://keymate.ai')

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                | Example                                                                    |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `q`                                                                        | *str*                                                                      | :heavy_check_mark:                                                         | The context you are searching from user's personal Keymate Memory history. | https://keymate.ai                                                         |


### Response

**[operations.QueryResponse](../../models/operations/queryresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## browseurl

This is the most powerful browsing endpoints it uses residential proxies and bypasses firewalls. Try this with Reddit, LinkedIn etc.

### Example Usage

```python
import keymateapi
from keymateapi.models import operations

s = keymateapi.Keymateapi(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.browseurl(request=operations.BrowseurlRequest(
    inputwindowwords='10000',
    q='https://keymate.ai',
    percentile='1',
    numofpages='1',
    paging='1',
))

if res.two_hundred_application_json_object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.BrowseurlRequest](../../models/operations/browseurlrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.BrowseurlResponse](../../models/operations/browseurlresponse.md)**
### Errors

| Error Object                 | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.BrowseurlResponseBody | 400                          | application/json             |
| errors.SDKError              | 4xx-5xx                      | */*                          |

## browse

Fetches URLs optimized for non heavily guarded websites

### Example Usage

```python
import keymateapi

s = keymateapi.Keymateapi(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.browse(q='http://impressive-silence.info', percentile='1', numofpages='1', paging='1')

if res.two_hundred_application_json_object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      | Example                                                                          |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `q`                                                                              | *str*                                                                            | :heavy_check_mark:                                                               | URL starting with https://memory.keymate.ai. Must be a valid URL.                |                                                                                  |
| `percentile`                                                                     | *str*                                                                            | :heavy_check_mark:                                                               | For adjusting response scope in case of 'ResponseTooLarge' error. Starts with 1. | 1                                                                                |
| `numofpages`                                                                     | *str*                                                                            | :heavy_check_mark:                                                               | Specifies the number of pages to return. Starts with 1 by default.               | 1                                                                                |
| `paging`                                                                         | *Optional[str]*                                                                  | :heavy_minus_sign:                                                               | Used for pagination. Increments for subsequent pages.                            | 1                                                                                |


### Response

**[operations.BrowseResponse](../../models/operations/browseresponse.md)**
### Errors

| Error Object                      | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.BrowseResponseBody         | 400                               | application/json                  |
| errors.BrowseResponseResponseBody | 401                               | application/json                  |
| errors.SDKError                   | 4xx-5xx                           | */*                               |

## search

Searches web using google and fetches URLs optimized for non heavily guarded websites

### Example Usage

```python
import keymateapi

s = keymateapi.Keymateapi(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.search(q='http://fake-flume.name', percentile='1', numofpages='1')

if res.two_hundred_application_json_object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      | Example                                                                          |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `q`                                                                              | *str*                                                                            | :heavy_check_mark:                                                               | URL starting with https://memory.keymate.ai. Must be a valid URL.                |                                                                                  |
| `percentile`                                                                     | *str*                                                                            | :heavy_check_mark:                                                               | For adjusting response scope in case of 'ResponseTooLarge' error. Starts with 1. | 1                                                                                |
| `numofpages`                                                                     | *str*                                                                            | :heavy_check_mark:                                                               | Specifies the number of pages to return. Starts with 1 by default.               | 1                                                                                |


### Response

**[operations.SearchResponse](../../models/operations/searchresponse.md)**
### Errors

| Error Object                      | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.SearchResponseBody         | 400                               | application/json                  |
| errors.SearchResponseResponseBody | 401                               | application/json                  |
| errors.SDKError                   | 4xx-5xx                           | */*                               |

## ultrafastsearch

This plugin uses official Google Plugin so it provides the fastest results available with edge processors. Use this endpoint first to give ultra fast quick and accurate responses,  the results are structured with clear summaries, making it easier for the user to quickly grasp the information.

### Example Usage

```python
import keymateapi

s = keymateapi.Keymateapi(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.ultrafastsearch(q='https://keymate.ai', percentile='100', numofpages='10')

if res.two_hundred_application_json_object is not None:
    # handle response
    pass

```

### Parameters

| Parameter           | Type                | Required            | Description         | Example             |
| ------------------- | ------------------- | ------------------- | ------------------- | ------------------- |
| `q`                 | *str*               | :heavy_check_mark:  | URL of the website. | https://keymate.ai  |
| `percentile`        | *str*               | :heavy_check_mark:  | Set it as '100'     | 100                 |
| `numofpages`        | *str*               | :heavy_check_mark:  | Set it as '10'      | 10                  |


### Response

**[operations.UltrafastsearchResponse](../../models/operations/ultrafastsearchresponse.md)**
### Errors

| Error Object                       | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| errors.UltrafastsearchResponseBody | 400                                | application/json                   |
| errors.SDKError                    | 4xx-5xx                            | */*                                |

## gptsbrowse

Fetches URLs optimized for https://memory.keymate.ai, requiring bearer token authentication. Reflects user info and provides contextually relevant rules for actions performed.

### Example Usage

```python
import keymateapi

s = keymateapi.Keymateapi(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.gptsbrowse(q='http://puzzled-advertisement.com', percentile='1', numofpages='1', paging='1')

if res.two_hundred_application_json_object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      | Example                                                                          |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `q`                                                                              | *str*                                                                            | :heavy_check_mark:                                                               | URL starting with https://memory.keymate.ai. Must be a valid URL.                |                                                                                  |
| `percentile`                                                                     | *str*                                                                            | :heavy_check_mark:                                                               | For adjusting response scope in case of 'ResponseTooLarge' error. Starts with 1. | 1                                                                                |
| `numofpages`                                                                     | *str*                                                                            | :heavy_check_mark:                                                               | Specifies the number of pages to return. Starts with 1 by default.               | 1                                                                                |
| `paging`                                                                         | *Optional[str]*                                                                  | :heavy_minus_sign:                                                               | Used for pagination. Increments for subsequent pages.                            | 1                                                                                |


### Response

**[operations.GptsbrowseResponse](../../models/operations/gptsbrowseresponse.md)**
### Errors

| Error Object                          | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| errors.GptsbrowseResponseBody         | 400                                   | application/json                      |
| errors.GptsbrowseResponseResponseBody | 401                                   | application/json                      |
| errors.SDKError                       | 4xx-5xx                               | */*                                   |

## internetsearch

Performs an internet search based on provided query. Utilizes 'Authorization' and custom headers for user identification and search customization.

### Example Usage

```python
import keymateapi

s = keymateapi.Keymateapi(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.internetsearch(inputwindowwords='8000', q='python', percentile='1', numofpages='6')

if res.two_hundred_application_json_object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              | Example                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `inputwindowwords`                                                                                                       | *str*                                                                                                                    | :heavy_check_mark:                                                                                                       | Set it as '8000' first if responsetoolarge occurs reduce it to 1000.                                                     | 8000                                                                                                                     |
| `q`                                                                                                                      | *str*                                                                                                                    | :heavy_check_mark:                                                                                                       | Search query                                                                                                             | python                                                                                                                   |
| `percentile`                                                                                                             | *str*                                                                                                                    | :heavy_check_mark:                                                                                                       | Start it as '1', increase to '6' if ResponseTooLarge occurs, only reduce to '3' or '4' if user requests it.              | 1                                                                                                                        |
| `numofpages`                                                                                                             | *str*                                                                                                                    | :heavy_check_mark:                                                                                                       | Start it as '6'. Retry the request by decreasing only this one if 'ResponseTooLarge' occurs. Should be between 1 and 10. | 6                                                                                                                        |


### Response

**[operations.InternetsearchResponse](../../models/operations/internetsearchresponse.md)**
### Errors

| Error Object                              | Status Code                               | Content Type                              |
| ----------------------------------------- | ----------------------------------------- | ----------------------------------------- |
| errors.InternetsearchResponseBody         | 400                                       | application/json                          |
| errors.InternetsearchResponseResponseBody | 401                                       | application/json                          |
| errors.SDKError                           | 4xx-5xx                                   | */*                                       |
