<!-- Start SDK Example Usage [usage] -->
```python
import keymate_python_sdk

s = keymate_python_sdk.KeymatePythonSDK()


res = s.insertionplan("<YOUR_BEARER_TOKEN_HERE>", q='<value>')

if res.object is not None:
    # handle response
    pass

```
<!-- End SDK Example Usage [usage] -->