---
title: Week 3 - First Merge and Developing a Training Pipeline
date: 2025-07-11
time: "15:00"
author: john
categories: ["pytorch", "training"]
layout: post
---

### Highlights

- On Monday, I completed my first merge into the main branch of the project repository. My changes included the work I completed last week, as well as improving the way we select the transforms for initialising our training set.
- Previously, we hardcoded the transformations within ```train.mobious.py```. This makes future use of the file inflexible, and means if we wanted to change the combination of transformations used, we would have to manually change the values passed into the MobiousDataset constructor. To fix this, I added a new section in the config file so the user can specify transformations. These are then passed into the constructor as arguments. Doing this simplifies the process of selecting transformations.

### This Week's Challenges

- Figuring out how to split our dataset of images into separate training, validation, and test sets. This has involved me looking at different materials, such as Stack Overflow threads and PyTorch documentation, to accomplish this.
- When loading in the training set, I get a RuntimeError stating I don't have enough memory. I suspect this is because I don't have enough RAM. After looking at GitHub issue threads that have had similar issues, I've increased the amount of virtual memory I have in my system settings. This did not fix my issue, but at least it's a start.

### Next Week's Plan
- Try to create a solution to my memory issue. It could potentially be due to the size of the images, but could be worth exploring if tweaking the batch size improves my situation.
- Succesfully split our dataset into the training, validation, and test sets, and run the program so I don't get another RuntimeError.
