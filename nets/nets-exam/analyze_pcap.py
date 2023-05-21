with open("dns_responses.txt", "r") as f:
    lines = f.readlines()


records = [x.strip().split(",") for x in lines]

r = {}
for record in records:
    split_i = record.index("<Root>")
    dns = record[:split_i]
    ips = record[split_i+1:]
    for d in dns:
        if d in r:
            if set(ips) != r[d]:
                print(f"{d} ips are not the same old: {set(ips).difference(r[d])}, new: {r[d].difference(ips)}")
        else:
            r[d] = set(ips)

