pset = set(make_primes(10**6))

def main():
    t1 = time.time()

    print('time:', round(time.time() - t1, 3))
    return


def find_conns(p):
    pdigs = list(str(p))
    print(pdigs)
    ans = []
    #rule 2
    #take off 1st digit
    if p >= 10 and pdigs[1] != '0': #only if at least 2 digits and 2nd digit != 0
        short = int(''.join(pdigs[1:]))
        if short in pset:
            ans.append(short)
    base = str(p)        
    for first in '123456789':
        long = int(first + base)
        if long in pset:
            ans.append(long)

    #rule 1
    numdig = len(pdigs)
    #replace with 0
    for place in range(1, numdig):
        tmp = pdigs[:]
        if tmp[place] != '0':
            tmp[place] = '0'
            if int(''.join(tmp)) in pset:
                ans.append(int(''.join(tmp)))
        
    for place in range(numdig):
        orig = pdigs[place]
        tmp = pdigs[:] #['1', '2', '3']
        for new in '123456789':
            if new != orig:
                tmp[place] = new
                if int(''.join(tmp)) in pset:
                    ans.append(int(''.join(tmp)))
    return ans
        
def make_conn_dict(N):
    ans = dict()
    for p in plst2:
        if p < N:
            ans[p] = [x for x in find_conns(p) if x < N]
    return ans

