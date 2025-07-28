---
title: Week 5 – Updating Simulated Annealing for QCO
date: 2025-07-25
time: "17:00:00"
author: miles
categories: ["Simulating Annealing", "quantum circuit optimisation"]
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
| Generated a Simulated Annealing algorithm for QCO | ✔        |
| Updated my RL Policy | ✔        |

### This week

Alot of work has been done to make my Simulated Annealing algorithm's work; including messing around with gate and depth fidelity parameters and cooling temperatures, to ensure my algorithm does operate Quantum circuits.
I do seem to be having an issue with consistenly getting the algorithm to optimise circuits AND keep them logically quivalent; they seem to be closer to equivalence now - however, still not reliably complete fidelity (please note - I have not yet added noise to my system, so this should not be here.)
I have added equivalence checks on the states of each qubit, in addition to plotting graphs to demonstrate reduced gate and depth count after optimisation.

### Next week’s plan

* Continue to check my gate identity logic; to ensure my Simulated Annealing algorithms run with 100% fidelity.
* Simulate and add noise to the circuit (test optimisations of this with simulated annealing)
* Resolve the issue I have with my RL policy which is causing a constant -ve reward and no modified circuit.
* Convert my circuit generator into a function which feeds circuits into RL environment
