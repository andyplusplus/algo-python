
def cheeshop(kind, *args, **keyss):
    print kind
    print
    for a in args:
        print a
    print
    keys = sorted(keyss.keys())
    for kw in keys:
        print kw, ":", keyss[kw]


cheeshop("1", "2", "3", "4",
         how="are",
         are="you")