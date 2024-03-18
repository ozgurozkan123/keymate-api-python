import keymate_api

print(vars(keymate_api.KeymateAPI))
s = keymate_api.KeymateAPI("969766f88135771cf250104b1aa25c6d1dcead5c")


res = s.hybrid("percentile='1'","numofpages='1'" , q='test')

if res.object is not None:
    # handle response
    pass
