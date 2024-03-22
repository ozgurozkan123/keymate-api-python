import keymateapi

s = keymateapi.Keymateapi(
    bearer_auth="969766f88135771cf250104b1aa25c6d1dcead5c",
)


res = s.upsert(q='Used the api to insert this')

if res.object is not None:
    # handle response
    print(res.object)
    pass
