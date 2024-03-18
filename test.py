import keymate_api

s = keymate_api.KeymateAPI("969766f88135771cf250104b1aa25c6d1dcead5c")


res = s.insertionplan(q='tes')

if res.object is not None:
    # handle response
    pass
