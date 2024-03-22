# SearchResponseResponseBody

Unauthorized access due to missing or invalid authorization details.


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        | Example                                                            |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `http_meta`                                                        | [components.HTTPMetadata](../../models/components/httpmetadata.md) | :heavy_check_mark:                                                 | N/A                                                                |                                                                    |
| `error`                                                            | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | N/A                                                                | Missing Authorization header or unsupported authorization type     |