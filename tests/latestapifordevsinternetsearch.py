import keymateapi

s = keymateapi.Keymateapi(
    bearer_auth="969766f88135771cf250104b1aa25c6d1dcead5c",
)


res = s.internetsearch(inputwindowwords='10000', q='bitcoin', percentile='1', numofpages='5')

if res.two_hundred_application_json_object is not None:
    # handle response
    print(res.two_hundred_application_json_object)
    pass
