import crawl_sw
import utils
import json
f = open("airports.json", 'r')
aps = json.loads(f.read())

dates = [
    "2018-08-01",
]

fareTypes = [
    "USD"
]

# dates = ["2018-07-{}".format("0{}".format(i) if len(str(i)) == 1 else "{}".format(i)) for i in range(14, 15)]
deps = [ap["id"] for ap in aps]

for d in dates:
    for dep in deps:
        for ap in aps:
            for fareType in fareTypes:
                if dep != ap["id"]:
                    fname = "out/{}/{}/{}/{}.json".format(dep, d, fareType, ap["id"])
                    utils.make_sure_exists(fname)
                    try:
                        if len(open(fname, 'r').read()) > 0: continue
                    except: pass
                    try:
                        f2 = open(fname, 'w')
                        f2.truncate()
                        f2.write(json.dumps(crawl_sw.SWAFlightReq(ap["id"], dep, d, fareType).getStops("MDW"), indent=4, sort_keys=True))
                        f2.close()
                    except Exception as e:
                        print (e)
