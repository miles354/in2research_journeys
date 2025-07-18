---
title: Week 4 - Completing Training Pipeline and Evaluating Model 
date: 2025-07-18
title: "16:00"
author: john
categories: ["pytorch", "models", "pipelines"]
layout: post
---

### Highlights
- Adding validation as part of the main training loop. This taught me the difference between what it means to train and validate a model. Importantly, during validation, only forward pass results are needed since we don't want to change the weights of our model via backpropogation. 
- After the training and validation loop, I added a feature where the model is evaluated using the test set. This is important since it tests the model on unseen data, and measures how well it can identify the different, distinct areas of the eye.

### This Week's Challenges
- Due to my laptop's memory constraints that I touched upon in last week's blog post, I had to downsize the dimensions of the images I used when training and validating the model. To do this, I created a bash script to resize all images in a given directory. However, I didn't realise that even though you provide your desired heigh and width pixel sizes, the new image will want to maintain the aspect ratio of the old image. This will result with inaccurate image dimensions. This was a challenge for me because it meant when these images were passed into the model, tensors couldn't be alligned because they had different dimensions. By changing the bash script and forcing the new images to ignore the previous aspect ratio, I got the model to accept them.
- Figuring out how to measure accuracy so it can be used to evaluate the model. To do this, I summed up how many elements in both the predicted labels and actual labels matched. By dividing this number by the total number of elements in the actual labels, this gives us a measure of how many pixels were assigned the correct label.

### Next Week's Plan
- Loading in a previously saved model and evaluating it using the test set, instead of having to create a new model everytime we want to use the test set.
- Exploring how K-Fold cross validation can be used to assess model performance.
