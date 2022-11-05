
def play():

    from random import shuffle
    
    envelope = [100, 0, 0]

    shuffle(envelope)

    pick1 = envelope.pop(1)

    i = envelope.index(0)

    envelope.pop(i)

    pick2 = envelope[0]

    return pick1, pick2

sum1 = 0
sum2 = 0

for i in range(1000):
    pick_1, pick_2 = play()
    sum1 += pick_1
    sum2 += pick_2


print (sum1, sum2)
print (sum1/sum2)
    


