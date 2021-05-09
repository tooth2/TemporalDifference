# Continuous Space 

## Background 
1. MountainCar-v0
A car is on a one-dimensional track, positioned between two "mountains". The goal is to drive up the mountain on the right; 
however, the car's engine is not strong enough to scale the mountain in a single pass. 
Therefore, the only way to succeed is to drive back and forth to build up momentum.

- Environment details
MountainCar-v0 defines "solving" as getting average reward of -110.0 over 100 consecutive trials.
This problem was first described by Andrew Moore in his PhD thesis [Andrew Moore](https://www.cl.cam.ac.uk/techreports/UCAM-CL-TR-209.pdf)

2. MountainCarContinuous-v0
Same task with MountainCar-v0 Here, Here, this is the continuous version and the reward is greater if you spend less energy to reach the goal

- Environment details
MountainCarContinuous-v0 defines "solving" as getting average reward of 90.0 over 100 consecutive trials.

## Discretization
- discretize continuous state spaces
- use tabular solution methods to solve complex tasks
- the Mountain Car environment

## Tile-Coding
- a method for discretizing continuous state spaces that enables better generalization

## Reference 
- 1990, Andrew Moore Dissertation[Efficient memory-based learning for robot control](https://www.cl.cam.ac.uk/techreports/UCAM-CL-TR-209.pdf)
- 1998, Manuela Veloso [Tree Based Discretization for Continuous State Space Reinforcement Learning](http://www.cs.cmu.edu/~mmv/papers/will-aaai98.pdf)
- 2002, Andrew Moore [Variable Resolution Discretization in Optimal Control](https://link.springer.com/content/pdf/10.1023%2FA%3A1017992615625.pdf)
