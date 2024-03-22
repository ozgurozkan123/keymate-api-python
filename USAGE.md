<!-- Start SDK Example Usage [usage] -->
```python
import keymateapi

s = keymateapi.Keymateapi(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.upsert(q='<value>')

if res.object is not None:
    # handle response
    pass

```
<!-- End SDK Example Usage [usage] -->