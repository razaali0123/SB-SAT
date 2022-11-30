# Attention Prediction using Eye-Tracking Data

## Project Aim and Exploration
The aim of the project will be to predict the level of text comprehension using the reader's eye movement data. After each indivitual 
read 4 published SAT passages, they had to answer corresponding SAT and selfevaluation questionnaires.
The scores from these questionnaires can act as a metric for measuring `attention` of a reader.

In the project, we will try to explore different dimensions and answer some questions like:
- Can the eye movement of an `indivitual` over a specific passage be used to predict the attention on other passages.
- Can the eye movement of an `indivitual` over a specific passage be used to predict the attention of other subject on the same passage. 
- Can the eye movement generalize by predicing `attention` of any subject on any passage.
- Exploring the importance of features while predicitng.
- Carrying out statistical tests to verify whether native english speakers tend to be more attentive than non-native.
- Carrying out statistical tests to verify whether subject's cognitive and mental states effects attention level.

## Dataset Description
I will be using the public eye-movement data available here:
```
https://github.com/ahnchive/SB-SAT
```

It consists of the eye movement data from 95 undergraduate students reading four SAT passages for comprehension, and their responses on comprehension questions and selfevaluation questionnaires (e.g., subjective difficulty of passage).
All reading passages and questions were selected from the SAT
practice set from their official website: https://collegereadiness.
collegeboard.org/sat/practice. (Reference: https://www3.cs.stonybrook.edu/~arunab/papers/etra20.pdf)

### Raw fixation dataset 
`18sat_fixfinal.csv` contains raw eyemovement measures recorded using Eyelink 1000 (1000hz sampling rate). This file also contains which word of the passage the current gaze is fixated on (`CURRENT_FIX_INTEREST_AREA_LABEL` column). We exported all eye-movement measures using SR Research Eyelink Data Viewer program. You can see the detailed description about each eye-movement measure in their [manual](https://www.sr-research.com/support/attachment.php?aid=663). `18sat_trialfinal.csv` contains eye-movment measures are averaged or aggreaged for each trial (each page). Additional details about the other variables:

- RECORDING_SESSION_LABEL: subject id
- INDEX: trial id
- type: whether this trial belongs to reading or question
- book_name: reading passage name id
- book:	reading passage integer id
- page: current page number for each reading passage
- total_page: total page number for each reading passage
- RT: total reading time for each page
- answer: subject's key response
- correct_answer: correct response (no correct reponse for reading trials, replaced as -99)
- page_name: the filename used for image stimuli (in stimuli folder)


### Question Response 
`18sat_labels.csv` has subject demographics and preprocessed question responses for model training (see paper for details how we preprocess this data)

- subj: subject id
- language: native langauge
- native: whether native langauge is english (0-no, 1-yes)
- book: reading passage id
- acc: average passage accuracy
- acc_level: average passage accuracy level in quartile (0: lowest 25%, 1: 25-50%, 2: 50-75%, 3: highest 25%)
- subj_acc: individual’s comprehension score averaged over all four passages 
- subj_acc_level: subj_acc level in quartile (0: lowest 25%, 1: 25-50%, 2: 50-75%, 3: highest 25%)
- other variables; subject's subjective evaluation on their cognitive and mental states while reading this passage (default is higher the number, higher the state, number range from 0 to 3)
  - confidence: How confident were you when answering to the previous comprehension questions (overall)?
  - difficulty: How do you rate the difficulty level of the passage you read?
  - familiarity: How familiar are you with the topic of this passage?
  - interest: How interesting this passage was?
  - pressured: How much pressure did you feel during reading?
  - sleepiness How sleepy were you during reading this passage
  - sleephours: How long did you sleep last night?(0: less than 3 hours, 1: 3-6 hours, 2: 6-9 hours, 3: more than 9 hours)
  - recognition: Have you read this passage before? (0:no, 1:yes)	


