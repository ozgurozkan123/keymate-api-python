<!-- Start SDK Example Usage [usage] -->
```python
import keymateapi

s = keymateapi.KeymateAPI()


res = s.insertionplan("<YOUR_BEARER_TOKEN_HERE>", q='<value>')

if res.object is not None:
    # handle response
    pass

```
<!-- End SDK Example Usage [usage] -->