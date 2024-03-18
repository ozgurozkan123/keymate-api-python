# GptsbrowseRequest


## Fields

| Field                                                                                                            | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `q`                                                                                                              | *str*                                                                                                            | :heavy_check_mark:                                                                                               | URL of the website. Url should be starting with https://memory.keymate.ai                                        |
| `percentile`                                                                                                     | *str*                                                                                                            | :heavy_check_mark:                                                                                               | Start it as '1', increase to '2' if ResponseTooLarge occurs you can multiply it with 2 for each retry.           |
| `numofpages`                                                                                                     | *str*                                                                                                            | :heavy_check_mark:                                                                                               | Set it as '1'                                                                                                    |
| `paging`                                                                                                         | *Optional[str]*                                                                                                  | :heavy_minus_sign:                                                                                               | Set it as '1' first then according to results you can increase it by one to get the other part of the same page. |