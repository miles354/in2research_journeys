---
title: Week 4 – Setting Up Reinforcement Learning and Heuristic Algorithms
date: 2025-07-18
time: "18:00"
author: miles
categories: ["Proximal Policy Optimisation", "quantum circuit optimisation", "heuristic algorithm"]
layout: post
---


### What is my project about?

I am building a machine learning model that predicts errors, and using these to optimise quantum circuits.
### Why use Quantum Computers, and what problems exist?
* Quantum computers promise revolutionary speedups due to quantum mechanical effects, however its reliability is limited by noisy hardware. My project aims to use AI to increase efficiency and error-awareness in Noisy Intermediate Scale Quantum (NISQ) devices, prior to Quantum Error Correction (QEC).
### Overall Goal
* Develop an AI-enhanced Quantum Circuit Optimiser (QCO)
* Predict the effects of quantum noise (qubit decoherence, quantum gate and measurement errors)
* Recommend optimisations to improve the efficiency of quantum circuits.
### Tasks completed this week

| Task                                                                                                                         | Checklist |
|------------------------------------------------------------------------------------------------------------------------------|:--------:|
| Setting up Heuristic Algorithm as Benchmark for QCO (Simulated Annealing)| ✔        |
| Set up an RL Policy (PPO)| ✔        |
| Set up a RL Gym Environment | ✔        |
| Enlisted and incorporated a set of Quantum Gate Rules into RL| ✔        |
| Converted my circuit generator into a function which feeds circuits into RL environment| ✔         |

###Simulated Annealing

Simulated annealing is used as a known benchmark, a heuristic algorithm which has been chosen to compare results of QCO against Reinforcement Learning.
This algorithm is known to optimise and find solutions - however, most importantly trained to not react abruptly to local minima.
The aim is to compare how much these reduce gate and depth count by.

### Policy

PPO is used, using Stablebaselines3. This is used over policies such as DQN as it typically works better in multi-discrete action spaces. It is also used in the main paper referenced in Week 2.
Currently still working on making my agent work, there is a problem with my code which is causing my overall reward to remain -1.00.

### Gym Environment

In my gym environment, I have defined the action space with 6 actions:

            0: "delete",
            1: "replace",
            2: "keep",
            3: "swap",
            4: "cancel",
            5: "commute"

Where "delete" and "cancel" have the highest rewards as they actively reduce the gate count
Other actions such as swaps and replaces have a partial negative reward to discourage meaningless gate movements.

### IBM Hardware Constraint Decomposition

My decomposed (or native) circuits now abide IBM Superconducting qubit constraints
Includes Quantum Hardware constraints: In IBM they use a 1D Chain Topology, coding has been implemented in the decomposed gate rules so that  non-adjacent multi-qubit gates have been decomposed to groups of swap gates, then controlled X gates.
E.g. CNOT(Q2,Q4) = SWAP(Q2,Q3),SWAP(Q3,Q4) = CNOT(Q2,Q3),CNOT(Q3,Q2),CNOT(Q2,Q3)CNOT(Q3,Q4),CNOT(Q4,Q3),CNOT(Q3,Q4)

I have come to terms with the fact, this constraint depending how far multi-qubit gates act upon makes the number of gates squarely proportional longer, and has the potential to dominate the decomposed gate set and not learn much (especially with 3-qubit gates for example a CCX(0,3,19) in a 20 qubit circuit, which would amount to 93 CX gates!).
It is also much more difficult for an environment to recognise gate identities globally, for eg identifiying that 2 CCX gates CCX(0,3,19) CCX(0,3,19) = I, it would be much more difficult to identify that the two sets of 93 gates make the Identity matrix (I) than just two CCX.

With all of this in mind, I intend to use QCO on the original circuit and then decompose the circuit; and then compare the gate and depth count reductions.

### Gate Rules

A list of Gate Identities can be found in my quantum_rules.py file; where I discuss and identify Gate equivalent operations such as gate identities HH = I, or commutable gates like CX and Rz commute (i.e CX(target q)Rz(q) = Rz(q)CX(target q)) however CX and X do not (i.e. CX(target q)X(q) /= X(q)CX(target q)).
Aim of rules like these are to influence RL of what operations are logically equivalent; in the hopes of making a more efficient circuit dataset.

### Next week’s plan

* Test and compare Simulated Annealing and RL trained agency on Quantum Circuits
* Fix my RL Agency / Environment
