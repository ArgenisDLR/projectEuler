def primes(n):
     #return a list of all primes < n
     ans = n*[True]
     ans[0] = ans[1] = False
     p = 2
     while p**2 < n:
         for i in range(p**2, n, p):
             ans[i] = False
         p += 1
         while not ans[p]:
             p += 1
     
     return [i for i in range(n) if ans[i]]
     
