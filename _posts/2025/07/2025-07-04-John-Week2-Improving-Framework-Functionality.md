---
title: Week 2 - Improving Framework Functionality
date: 2025-07-04
time: "15:00"
author: john
categories: ["pytorch", "models", "convolutional neural networks", "software engineering"]
layout: post
---


### Highlights

- After struggling to install the onnxsim, I figured out the issue was to do with python3.12-dev not being installed onto WSL2. Since cmake requires Python development files and they didn't exist on my machine, an error was being thrown. After installing pythn3.12-dev, the project now runs properly. I then updated the documentation detailing my issue and how I fixed it.
- Since the framework was supposed to on laptops with GPU and my laptop doesn't have one, I've had to add some extra functionality so I can run the project locally. After making these changes, I opened a pull request so future users are able to utilise the framework.
- Added new functionality so intermediate directories are built when saving model performance metrics.
- Continued reading and using other materials to understand CNNs and how to optimise our model.

### This Week's Challenges

- Learning PyTorch syntax to understand how the models in papers I'm reading are implemented.
- Trying to change hardcoded values in the project's code without breaking something.

### Next Week's Plan

- Figure out a way to safely deal with hardcoded values in the project's code.
- Split the image dataset we use into separate train, test, and validation datasets so we can better understand the model's effectiveness. 
