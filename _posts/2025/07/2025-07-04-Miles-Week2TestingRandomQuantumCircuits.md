---
title: Week 2 – Testing Random Quantum Circuits
date: 2025-07-04
time: "15:00"
author: miles
categories: ["reinforcement learning", "quantum circuit optimisation", "qiskit"]
layout: post
---

### What is my project about?

I am building a machine learning model that predicts errors, and using these to optimise quantum circuits.

### Why use Quantum Computers, and what problems exist?

* Quantum computers promise revolutionary speedups due to quantum mechanical effects, however its reliability is limited by noisy hardware. My project aims to use AI to increase efficiency and error-awareness in Noisy Intermediate Scale Quantum (NISQ) devices, prior to Quantum Error Correction (QEC).

### Overall Goal

* Develop an AI-enhanced quantum circuit optimiser.
* Predict the effects of quantum noise (qubit decoherence, quantum gate and measurement errors)
* Recommend optimisations to improve the efficiency of quantum circuits.

### Tasks completed this week

| Task                                                                                                                         | Checklist |
|------------------------------------------------------------------------------------------------------------------------------|:--------:|
| Identified & compared key reference papers to structure my work around | ✔        |
| Generated random Quantum Circuit datasets| ✔        |

### Next week’s plan

* Begin to generate datasets which match IBM's hardware constraints (i.e. 1D Chain Topology - allowing connectivity between adjacent qubits)
* Define my environment: states, actions, rewards
* Try a simple reward with just optimised depth count (like in the key paper)
* Convert my circuit generator into a function which feeds circuits into RL environment
