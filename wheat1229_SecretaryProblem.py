# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt

num_roommates = 50 #number of roommates to select from
desired_M = 10 #number of interviews
top_N = 1 #top N candidates
num_iterations = 10000

# array of individual roommates and their ranks
roommate = np.arange(1, num_roommates + 1)

# store roommate score after each interview
roommate_scores = np.zeros(desired_M)

 # store probability of best roommate
prob_top_N_roommate = np.zeros(desired_M, dtype = float)

# store probability of no roommate (0)
prob_no_roommate = np.zeros(desired_M, dtype = float)


M = 0 # initial interviews in 'look' phase
while M < desired_M:#checks bounds of look phase

    iteration = 0 #start at iteration 0
    while iteration < num_iterations:#overall iterations

        np.random.shuffle(roommate) #shuffles roommates so they're random
        best_look_phase_score = 0 #reset value of best roommate in look phase
        
        #Begin Look Phase
        for interview in range(0,M):#conduct M interviews

            #updates hightest look phase score
            if roommate[interview] > best_look_phase_score:
                best_look_phase_score = roommate[interview]

        #Begin Leap Phase
        final_roommate_score = 0 #no roommates at first\

        #begin interviewing at candidate M
        for interview in range(M,num_roommates):
    
            #select the first one that is better than best in look phase
            if roommate[interview] > best_look_phase_score:
                final_roommate_score = roommate[interview]
                break#winner

        #running tally of all roommate scores
        roommate_scores[M] += final_roommate_score

        #example: top 5 roommate ranks 26 to 30 or (30-(5-1)) to (30 -(1-1))
        if final_roommate_score >= (num_roommates - (top_N - 1)):

            #running tally of all top N roommates found
            prob_top_N_roommate[M] += 1

        if final_roommate_score == 0:
            prob_no_roommate[M] += 1#running tally of no roommates found

        iteration += 1#increment iteration

    #find overall average roommate score after iterations
    roommate_scores[M] /= num_iterations
    #find overall probability of best roommate
    prob_top_N_roommate[M] /= num_iterations
    #find overall probability of no roommates
    prob_no_roommate[M] /= num_iterations

    M += 1#increment M

#print ideal N
N = np.max(prob_top_N_roommate)
print("Interview " + str(N) + " roommates then leap!")

#plot results
x = np.arange(0,desired_M)
plt.subplot(2,1,1)
plt.plot(x, prob_top_N_roommate,'-bo')
plt.grid()
plt.title('Best Roommate Odds vs Number of Interviews')
plt.ylabel('Probability of Selecting Best Roommate')
plt.subplot(2,1,2)
plt.plot(x, prob_no_roommate,'-ro')
plt.grid()
plt.title('No Roommate Odds vs Number of Interviews')
plt.ylabel('Probability of Selecting No Roommate')
plt.xlabel('Number Interviews in Look Phase (M)')
