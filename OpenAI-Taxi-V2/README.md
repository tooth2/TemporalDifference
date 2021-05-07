# OpenAI Gym’s Taxi-v2 Task 
Using OpenAI Gym's Taxi-v2 environment to design an algorithm to teach a taxi agent to navigate a small gridworld. 

## OpenAI Gym environment

## Structure 
- agent.py: Reinforcement learning agent using Temporal-Difference Methods 
- monitor.py: The interact function tests how well the agent learns from interaction with the environment.
- main.py: main program to check the performance of the agent

## Detail
the environment for 20,000 episodes specified in monitor.py, 
returns two variables: `avg_rewards` and `best_avg_reward`.
- `avg_rewards`: a deque where `avg_rewards[i]` is the average (undiscounted) return collected by the agent from episodes i+1 to episode i+100, inclusive. So, for instance, `avg_rewards[0]` is the average return collected by the agent over the first 100 episodes.
- `best_avg_reward`: the largest entry in `avg_rewards`. This is the final score to represent agent performance in the task.

- `__init__()` : define any needed instance variables such as number of actions available to the agent (nA) and initialize the action values (Q) to an empty dictionary of arrays. e.g the value of epsilon if the agent uses an epsilon-greedy policy for selecting actions.
- `select_action()` : accepts the environment state as input and returns the agent's choice of action. 
- `step()`: accepts a (state, action, reward, next_state) tuple as input, along with the done variable, which is True if the episode has ended --> to use the sampled tuple of experience to update the agent's knowledge of the problem.

## Result
OpenAI Gym defines "solving" this task as getting an average return of 9.7 over 100 consecutive trials, at least an average return of at least 9.1 over 100 consecutive trials (best_avg_reward > 9.1).

