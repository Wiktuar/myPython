a = 7825
count = 0
res = list(filter(lambda x: x.isdigit(), str(a)))
int_res = map(int, res)
print(sum(int_res))

