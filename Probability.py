import random

trails = [10,100,1000,10000]

for n in trails:
    tosses = [random.choice(["Head","Tail"]) for _ in range(100)]
    heads = tosses.count("Head")
    tails = tosses.count("Tail")

    prob_head = heads/100
    prob_tail = tails/100

    print("Number of trails :",trails)
    print("Number of heads :",heads)
    print("Number of tails :",tails)
    print("Probability of head :",round(prob_head,4))
    print("Probability of tail :",round(prob_tail,4))
    print("-" * 40)


n=6000
rolls = [random.randint(1,6) for _ in range(n)]

for outcome in range(1,7):
    count = rolls.count(outcome)
    probability = count/n

    print("Outcome:", outcome)
    print("Frequency:", count)
    print("Experimental Probability:", round(probability, 4))
    print()


n=10000
rolls = [random.randint(1,6) for _ in range(n)]

A ={1}
B={6}

Count_1 = sum([1 for x in rolls if x in A])
Count_6 = sum([1 for x in rolls if x in B])
Count_union = sum([1 for x in rolls if x in A or x in B])

print("Probability of A :",Count_1/n)
print("Probability of B :",Count_6/n)
print("Probability of A U B :",Count_union/n)
print("Probability of A + B :",(Count_1/n)+(Count_6/n))

print("-"*16)
print("Addition rule for overlapping events :")

rolls = [random.randint(1,6)]
A={2,4,6}
B={4,5,6}

A_intersection_B = A.intersection(B)
A_union_B = A.union(B)

probability_A = len(A)/6
probability_B = len(B)/6
probability_A_intersection_B = len(A_intersection_B)/6
probability_A_union_B = len(A_union_B)/6
result = probability_A+probability_B-probability_A_intersection_B

print("Probability of A :",probability_A)
print("Probability of B :",probability_B)
print("Probability of A intersection B :",probability_A_intersection_B)
print("Result :",result)
print("Probability of A union B :",probability_A_union_B)

print("-"*30)

n=10000
coin_toss = [random.choice(["Head","Tail"]) for _ in range(n)]
die_roll = [random.randint(1,6) for _ in range(n)]

A={"Head"}
B={2,4,6}

Probability_A = sum([1 for x in coin_toss if x in A])/n
Probability_B = sum([1 for x in die_roll if x in B])/n
count_intersection = sum(
    1 for i in range(n)
    if coin_toss[i] in A and die_roll[i] in B
)
left = count_intersection/n

result = Probability_A*Probability_B

print("left :",left)
print("right :",result)
