import numpy as np


# update/add code below ...
def ways(n, coin_types=[1,5,10]):
     """
    Returns the number of ways you can make change for a given amount of cents n
    Examples: function   --->      (num pennies, num nickels)
    """
    pennies=0
    nickels=0
    check=int(n/5)                             # using the remainder of change to distribute the nickels
    collect=[]
    if check !=0:                              # checking if there is at least one nickel possible
        for i in range(0,check+1):             # iterating over the possible nickles to create different ways 
            nickels=i
            pennies = n-(i*5)                  # subtracting the nickels to get the pennies possible
            collect.append((pennies,nickels))
    else:                                      # If no nickels are possible, the pennies are stored
        nickels=0
        pennies=n
        collect.append((pennies,nickels))
    return len(collect)


def lowest_score(names, scores):
    """
    Returns the name of the student with the lowest score.
    """
    data={n:s for n,s in zip(names, scores)}  # Create a dictionary of names and scores
    lowest=min(data.values())                 # Find the lowest score in the dictionary
    name=[k for k,v in data.items() if v==lowest] # Locate the key for the lowest score
    return name[0]


def sort_names(names, scores):
    """
    Returns the list of names of students in descending order of test score (i.e., a list of names, with associated scores in order from highest to lowest).
    """
    data= {n:s for n, s in zip(names, scores)} # Create a dictionary of names and scores
    sorted_scores=np.sort(scores)[::-1] #sorting scores by descending order
    sorted_data=[]
    for i in sorted_scores:
        name=[k for k,v in data.items() if v==i] # Find the name corresponding to the key from the sorted list
        sorted_data.append(name[0])              
    return sorted_data


#Test cases to check and verify the functions
names = np.array(['Hannah', 'Astrid', 'Abdul', 'Mauve', 'Jung'])
scores = np.array([99, 71, 85, 62, 91])
Test_case_change=ways(12),ways(30), ways(3)
Test_case_lowestscore= lowest_score(names,scores)
Test_case_sort_names=sort_names(names,scores)
