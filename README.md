# Temporal Difference 
A Python Implementation for various Temporal Difference methods 

## Structure
* Temporal_Difference.ipynb - the corresponding solutions
* plot_utils.py - contains a plotting function for visualizing state-value functions and policies
* check_test.py - contains unit tests to check the validity of your implementations

## Project Environment 
0. Environment :  [CliffWalkingEnv](https://github.com/openai/gym/blob/master/gym/envs/toy_text/cliffwalking.py)
   ```
    This is a simple implementation of the Gridworld Cliff
    reinforcement learning task.
    Adapted from Example 6.6 from Reinforcement Learning: An Introduction
    by Sutton and Barto:
    http://people.inf.elte.hu/lorincz/Files/RL_2006/SuttonBook.pdf
    With inspiration from:  https://github.com/dennybritz/reinforcement-learning/blob/master/lib/envs/cliff_walking.py
    The board is a 4x12 matrix, with (using Numpy matrix indexing):
        [3, 0] as the start at bottom-left
        [3, 11] as the goal at bottom-right
        [3, 1..10] as the cliff at bottom-center
    Each time step incurs -1 reward, and stepping into the cliff incurs -100 reward 
    and a reset to the start. An episode terminates when the agent reaches the goal.    
    ```


## Project Background
Compare to Monte Carlo (MC) prediction methods, MC must wait until the end of an episode to update the value function estimate, whereas, temporal-difference (TD) methods update the value function after every time step.

1. TD Control: Sarsa 
Sarsa(0) (or Sarsa) is an on-policy TD control method. It is guaranteed to converge to the optimal action-value function q∗, as long as the step-size parameter α is sufficiently small and ϵ is chosen to satisfy the Greedy in the Limit with Infinite Exploration (GLIE) conditions.

2. TD Control: Q-learning
Sarsamax (or Q-Learning) is an off-policy TD control method. It is guaranteed to converge to the optimal action value function q∗, under the same conditions that guarantee convergence of the Sarsa control algorithm.

3. TD Control: Expected Sarsa
Expected Sarsa is an on-policy TD control method. It is guaranteed to converge to the optimal action value function q∗, under the same conditions that guarantee convergence of Sarsa and Sarsamax.

This algorithm has four arguments:

* env: This is an instance of an OpenAI Gym environment.
* num_episodes: This is the number of episodes that are generated through agent-environment interaction.
* alpha: This is the step-size parameter for the update step.
* gamma: This is the discount rate. It must be a value between 0 and 1, inclusive (default value: 1).

The algorithm returns as output:
* Q: This is a dictionary (of one-dimensional arrays) where Q[s][a] is the estimated action value corresponding to state s and action a.

## Analysis/Result
On-policy TD control methods (like Expected Sarsa and Sarsa) have better online performance than off-policy TD control methods (like Q-learning).
Expected Sarsa generally achieves better performance than Sarsa.

### Reference 
* [OpenAI Gym](https://github.com/openai/gym/blob/master/gym/envs/toy_text/cliffwalking.py)
* [Cliff Walking](https://github.com/dennybritz/reinforcement-learning/blob/master/lib/envs/cliff_walking.py)
