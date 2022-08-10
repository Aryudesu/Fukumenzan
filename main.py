import itertools

def input_str(mes = "input > "):
    while True:
        print(mes, end="")
        res = input()
        if len(res.split()) == 1:
            break
    return res


def input_num(mes = "InputNum > "):
    while True:
        try:
            print(mes, end="")
            return int(input())
        except Exception:
            print("this is not number")


N = input_num()
data = []
chset = set()
nums = [l for l in range(10)]
for n in range(N+1):
    S = input_str()
    for s in S:
        chset.add(s)
    data.append(S)
chlist = list(chset)
chl = len(chlist)
chd = dict()

for idx in range(chl):
    chd[chlist[idx]] = idx

if chl > 10:
    print("error")

for itr in itertools.permutations(nums, chl):
    num = list(itr)
    for dat in data:
        
        for d in dat:
            pass
