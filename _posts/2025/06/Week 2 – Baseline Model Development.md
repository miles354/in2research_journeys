---
title: "Week 2 – Baseline Model Development"
date: 2025-06-20
time: "17:00"
author: hirraa
categories: ["nlp", "machine learning", "sentiment analysis","social media"]
layout: post 
---

## Week 2 – Baseline Model Development


This week I added **COVID-19 sentiment** 🦠📱 alongside **adverse drug reaction (ADR) detection** 💊🫨 to my dataset pipelines. I chose these two topics because the pandemic offers a large, accessible source for sentiment analysis datasets with reliable labels, especially around topics like long-COVID trends, while ADR posts deliver crucial early signals for pharmacovigilance, as mentioned last week. 


---

### Data Pipeline & Splits
I concatenated multiple cleaned datasets into a single DataFrame, then applied a **random**, stratified 80/20 train/test split (using `random_state=42`) so that both the training and testing sets include examples from every source.

I also, tested the best models on entirely separate datasets to see overfitting and generalisability .

| Task             | Training & Test (80/20)                        | External Validation                           |
|------------------|------------------------------------------------|-----------------------------------------------|
| COVID sentiment  | [`Instagram`](https://arxiv.org/abs/2410.03293), Tweets, Reddit API                     |   A   different datatset of tweets  |
| ADR detection    | [`PsyTAR`](https://doi.org/10.1016/j.dib.2019.103838) (annotated patient forum posts),  Reddit API      | [`CADEC-v2`](https://doi.org/10.1016/j.jbi.2024.104744) (annotated patient forum posts)                  |

⭐ These pipeline splits ensure that models only see part of each source during training and are then challenged on completely new data during external evaluation.


---



- For **ADR detection**, I used a comprehensive drug term list and minimal tokenisation to preserve medication names.  
- For **COVID sentiment**, I applied more cleaning (lowercasing, stopword removal, stemming) and handled emojis as sentiment cues to reduce noise.

These steps ensured each task received the right level of text normalisation.

---

### Baseline models trained  
I built three pipelines using [`TF-IDF`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html) vectorisation and tuned hyperparameters with 5-fold `GridSearchCV`:

⭐ 
[`GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html) tests different hyperparameter values with cross-validation to find settings that best balance bias and variance.

- **`Naïve Bayes`** (α = 0.01, 0.1, 1.0, 5.0)  

- **`Logistic Regression`** (C = 0.01, 0.1, 1, 10; with class weighting)  

- **`Random Forest`** (n_estimators = 100, 200; max_depth = None, 10; min_samples_split = 2)

I recorded each model’s optimal hyperparameters and stored the corresponding best model in a dictionary, ensuring that every evaluation reused the exact same models for  reproducibility.

---

### Performance: Macro-AUC  
Before summarising, I plotted ROC curves to inspect the true-positive vs. false-positive trade-offs. Below are the macro averaged ROC-AUC scores for train/test split vs. external dataset tests:

#### COVID sentiment (one-vs-rest)

| Model                   | Train/Test Split | Test only: Twitter |
|-------------------------|:----------------:|:-------:|
| Naïve Bayes             | 0.84             | 0.75    |
| **Logistic Regression** | **0.92**         | **0.82** |
| Random Forest           | 0.92             | 0.78    |

#### ADR detection (binary)

| Model                   | Train/Test Split |Test only: `CADEC_v2`  |
|-------------------------|:----------------:|:------:|
| Naïve Bayes             | 0.86             | 0.84   |
| **Logistic Regression** |0.89              | 0.89   |
| Random Forest           |**0.89**          |**0.90**|

**Bold* indicates the top performer in each column. ADR’s AUC stays steady on `CADEC_v2`, while sentiment dips on Twitter could be overfitting.

 #### **Below are the macro averaged ROC curves for Train/Test Split:** 

<img src="/images/2025/06/adr_roc.jpg" alt="ADR" width="48%" /> <img src="/images/2025/06/covid_sentiment_roc.jpg" alt="COVID" width="48%" />

---

### Key takeaways 🥡: 
- **`Logistic Regression`** offered the best mix of accuracy and stability, with minimal drop from train/test to external sets.  
- **`Random Forest`** matched LR on ADR and even led on the CADEC test, but didn’t perform as well for sentiment on new tweets.  
- **`Naïve Bayes`** was quick to train but didn’t perform as well as the other models.
- Class imbalance in ADR detection: most forum posts report reactions, so very few non-ADR examples, considering [`SMOTE`](https://imbalanced-learn.org/stable/references/generated/imblearn.over_sampling.SMOTE.html)  to oversample the minority class could help address this.
- The more pronounced AUC decline on COVID sentiment highlights how rapidly changing slang and topic shifts can undermine model performance.

---


### Challenges 🤔❓
- Balancing two label schemes (binary ADR vs. sentiment) required custom evaluation scripts.  
- Hyperparameter searches via `GridSearchCV` introduce long training times and require more compute.

---
## Summary


**Completed this week:**  

✅  Added COVID-19 sentiment to the pipeline alongside ADR detection and confirmed that shared TF-IDF features work well for both social media and clinical terminology.  

✅  Constructed and tuned three baseline pipelines (Naïve Bayes, Logistic Regression, Random Forest) with hyperparameter search, saving best models.  

✅  Validated performance with macro averaged ROC-AUC on the train/test split and truly external datasets (new tweets and CADEC-v2), showing minimal overfitting.

**Up next:**

➡️ 🧠 `Deep Learning` phase of the project implementing Transformer-based models (BERT and RoBERTa), training them on the cleaned dataset, and tuning hyperparameters for optimal performance.
