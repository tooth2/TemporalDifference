import numpy as np
from collections import defaultdict
import random

class Agent:

    def __init__(self, nA=6):
        """ Initialize agent.

        Params
        ======
        - nA: number of actions available to the agent
        """
        self.nA = nA
        self.Q = defaultdict(lambda: np.zeros(self.nA))
        #epsilon
        self.epsilon = 0.005
        self.gamma = 0.9 # 0.8
        self.alpha = 0.05 # 0.07
        ## 9.52 when gamma 0.9, alpha 0.05 100000 episodes 
        

    def get_probs(self,Q_s):
        """ obtains the action probabilities corresponding to epsilon-greedy policy """
        policy_s = np.ones(self.nA) * self.epsilon / self.nA
        #best_a = np.argmax(Q_s)
        policy_s[np.argmax(Q_s)] = 1 - self.epsilon + (self.epsilon / self.nA)
        return policy_s
    
    def select_action(self, state):
        """ Given the state, select an action.
        accepts the environment state as input
        returns the agent's choice of action

        Params
        ======
        - state: the current state of the environment

        Returns
        =======
        - action: an integer, compatible with the task's action space
        """
        #return np.random.choice(self.nA)
        act_space = [i for i in range(0, self.nA)]
        action = np.random.choice(np.arange(self.nA),
                                  p = self.get_probs(self.Q[state])) if state in self.Q else random.choice(act_space)
        return action

    def step(self, state, action, reward, next_state, done):
        """ Update the agent's knowledge, using the most recently sampled tuple.
        accepts a (state, action, reward, next_state) tuple as input
        sampled tuple of experience to update the agent's knowledge of the problem
        
        Params
        ======
        - state: the previous state of the environment
        - action: the agent's previous choice of action
        - reward: last reward received
        - next_state: the current state of the environment
        - done: whether the episode is complete (True or False)
        """
        #self.Q[state][action] += 1
        
        a_t_1 = self.select_action(next_state)
        self.Q[state][action] = self.Q[state][action] + self.alpha * (reward + self.gamma * (self.Q[next_state][a_t_1]) - self.Q[state][action])