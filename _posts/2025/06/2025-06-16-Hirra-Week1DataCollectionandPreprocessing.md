---
title: Week 1 – Data Collection and Pre-processing
date: 2025-06-16
time: "11:30"
author: Hirra
categories: ["nlp", "preprocessing", "sentiment-analysis", "pharmacovigilance"]
layout: post
---

### What the project is about 
I’m building NLP tools that detect **adverse drug reactions (ADRs)** and the surrounding **sentiment** from social-media posts.

### Why social-media text? 
* Real-world language: informal and varied
* Early signals: users report side-effects quickly
* Patient-centred insights into daily life impact

### Tasks completed this week

| Task                                                                                                                         | Checklist |
|------------------------------------------------------------------------------------------------------------------------------|:--------:|
| Selected four datasets: two patient‐forums (PsyTAR, CADEC‐v2), Reddit (self-labelled using Reddit API), and Twitter (SMM4H-20). | ✔        |
| Created preprocessing scripts:<br>• **`classic_preprocess`** – heavy cleaning, stemming, tokenisation (for traditional ML).<br>• **`preprocess_transformer`** – minimal cleaning, preserving negations, numbers, and drug terms (for deep-learning models). | ✔        |


### Early challenges 
Reddit data was straightforward to collect; Twitter required careful handling due to stricter access terms.

### Next week’s plan
* Train baseline Machine Learning models (Naïve Bayes and Logistic Regression). 
