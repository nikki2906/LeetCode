class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for n in range(1, n+1):
            if n % 3 == 0 and n % 5 == 0:
                res.append("FizzBuzz")
            elif n % 3 == 0:
                res.append("Fizz")
            elif n % 5 == 0: 
                res.append("Buzz")
            else:
                res.append(str(n))
        return res