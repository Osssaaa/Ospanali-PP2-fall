def solve(numheads, numlegs):
    rabbits = (numlegs/2) - numheads
    chicken = numheads - rabbits
    print(f'there is {int(rabbits)} rabits and {int(chicken)} chickens')
solve(int(input('Number of heads: ')), int(input('number of legs: ')) )