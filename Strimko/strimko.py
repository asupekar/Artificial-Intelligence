#!/usr/bin/env python
# coding: utf-8

# ####  Strimko Solution
# 
# <span style="color:red">Aishwarya Supekar</span>

# In[1]:



from constraint import *


def possibleDomains(value, initialAssignments):
    return range(1,len(initialAssignments)+1)


def solveStrimko(initialAssignments, chains):
    problem = Problem()

    mylist = []
    for i in range(len(initialAssignments)):
        for j in range(len(initialAssignments[i])):
            mylist.append((i,j))
    
    for i in range(len(mylist)):
        problem.addVariable(mylist[i], possibleDomains(mylist[i], initialAssignments))
        
    rows = [] 
    for i in range(len(initialAssignments)):
        row = []
        for j in range(len(initialAssignments)):
            row.append((i,j))
        rows.append(row)
    
    cols = []
    for i in range(len(initialAssignments)):
        col = []
        for j in range(len(initialAssignments)):
            col.append((j,i))
        cols.append(col)
    
    for j in range(len(rows)):
        problem.addConstraint(AllDifferentConstraint(), rows[j])
        
    for k in range(len(cols)):
        problem.addConstraint(AllDifferentConstraint(), cols[k])
        
    for chain in chains:
        problem.addConstraint(AllDifferentConstraint(), chain)
    
    solution = problem.getSolution().values()
          
    res = list(solution)
    
    k =0;
    result = []
    for i in range(len(rows)):
        row = []
        for j in range(len(cols)):
            row.append(res[k])
            k += 1
        result.append(row)
    return [result]

