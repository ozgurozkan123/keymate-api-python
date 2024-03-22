import keymateapi
from keymateapi.models import operations
s = keymateapi.Keymateapi(
    bearer_auth="969766f88135771cf250104b1aa25c6d1dcead5c",
)

req = operations.BrowseurlRequest(
    inputwindowwords='80000',
    q='https://news.ycombinator.com',
    percentile='1',
    numofpages='1',
    paging='1'
)

res = s.browseurl(req)

if res.two_hundred_application_json_object is not None:
    # handle response
    print(res.two_hundred_application_json_object)
    pass
