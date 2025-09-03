import numpy as np


# update/add code below ...
def ways(n, coin_types=[1,5,10]):
    pennies=0
    nickels=0
    check=int(n/5)
    collect=[]
    if check !=0:
        for i in range(0,check+1):
            nickels=i
            pennies=n-(i*5)
            collect.append((pennies,nickels))
    else:
        nickels=0
        pennies=n
        collect.append((pennies,nickels))
    return len(collect)

def lowest_score(names, scores):
    data={n:s for n,s in zip(names, scores)}
    lowest=min(data.values())
    name=[k for k,v in data.items() if v==lowest]
    return name[0]

def sort_names(names, scores):
    data= {n:s for n, s in zip(names, scores)}
    sorted_scores=np.sort(scores)[::-1]
    sorted_data=[]
    for i in sorted_scores:
        name=[k for k,v in data.items() if v==i]
        sorted_data.append((name[0],i))
    return sorted_data
