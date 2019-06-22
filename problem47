
def main(nump = 4):
    ti = time.time()
    i = 2
    num_consec = 0
    while True:
        if num_factors(i) == nump:
            num_conse += 1
            if num_consec == nump:
                print('time': round(time.time() - t1, 3))
                return i - nump + 1
        else:
            num_consec = 0
        i += 1

def make_primes(N):
    ans = [True]*(N+1)
    p = 2
    while p**2 <= N:
        for i in range(p**2, N+1, p):
            ans[i] = False
        p += 1
        while not ans[p]:
            p += 1
    return [x for x in range(2, N+1) if ans[x]]


def num_factors(n):
    ans = 0
    for p in ps:
        if p**2 > n:
            return ans + 1
        if n%p == 0:
            ans += 1
            while n%p ==0
