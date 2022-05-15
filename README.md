# Multi Perspective Scientific Document Summarization

This repository contains the dataset and baseline models for the Multi Perspective Scientific Document Summarization (MuP) shared task to be held at [SDP in COLING 2022](https://sdproc.org/2022/index.html).

### Introduction

Generating summaries of scientific documents is known to be a challenging task. Majority of existing work in summarization assumes only one single best gold summary for each given document. Having only one gold summary negatively impacts our ability to evaluate the quality of summarization systems as writing summaries is a subjective activity. At the same time, annotating multiple gold summaries for scientific documents can be extremely expensive as it requires domain experts to read and understand long scientific documents. This shared task will enable exploring methods for generating multi-perspective summaries. We introduce a novel summarization corpus, leveraging data from scientific peer reviews to capture diverse perspectives from the reader's point of view.

Peer reviews in various scientific fields often include an introductory paragraph that summarizes the key contributions of a paper from the reviewer standpoint and each paper usually receives multiple reviews. We leverage data from OpenReview, an open and publicly available platform for scientific publishing.  We collect a corpus of papers and their reviews from venues on openreview such as ICLR, NeurIPS, and AKBC primarily from the AI, Machine Learning and Natural Language Processing fields. We use carefully designed heuristics to only include first paragraphs of reviews that are summary-like. We manually check the summaries obtained from this approach on a subset of the data and ensure the high quality of the summaries.
The corpus contains a total of around 10K papers, and 26.5K summaries (with average number of 2.57 summaries per paper). The summaries are on average 100.1 words long (space tokenized).

This is the distribution of number of summaries:
| Num of Summaries | Num of Papers |
| --- | --- |
| 1| 2846 |
| 2| 2471 |
| 3 | 2871 |
| 4 | 1826|
| 5| 224|
| >5 | 256|


If you use this dataset please cite:

### MuP Data and Instructions

The dataset is hosted on Huggingface.
https://huggingface.co/datasets/allenai/mup

You can easily download and use the dataset as following:

```python
# pip install datasets

from datasets import load_dataset

data = load_dataset('allenai/mup')

print(data['train'].shape[0])  # should print 18934
print(data['validation'].shape[0])  # should print 3604
```

We encourage that you try your development on the validation data and use the training set for both training and hyperparameter tuning. 
Please do not use the validation data for training. 

# Test Data

Test data will be released at the evaluation stage. See the timeline below.

# Evaluation Scheme

The intrinsic evaluation will be done by ROUGE, using ROUGE-1, -2, -L metrics. In addition to that, BERTScore would be used. The average of the scores obtained against the multiple summaries would be used for final ranking.

### Submission Instructions

Evaluation Script: https://github.com/allenai/mup/blob/main/codalab/kit/scoring_program/evaluate.py

### Leaderboard
TBD

### Shared Task Timelines

Training Data Release:  May 10, 2022  <br />
Test Data Release:  June 30, 2022 <br />
Evaluation Period:  July 15, 2022 <br />
System Description Papers Due:  August 1, 2022<br />
Reviews Notification:  August 15, 2022 <br />
Camera-Ready Papers Due:  September 5, 2022<br />
Event at SDP @ COLING 2022:  October 16/17, 2022<br />

### License

### Disclaimer

### MuP 2022 Organizers

1. [Guy Feigenblat - Piiano](https://Piiano.com)
2. [Arman Cohan- AI2](http://armancohan.com/)
3. [Tirthankar Ghosal- Institute of Formal and Applied Linguistics, Charles University, Czech Republic](https://elitr.eu/tirthankar-ghosal/)
4. [Michal Shmueli-Scheuer - IBM Research AI](https://researcher.watson.ibm.com/researcher/view.php?person=il-SHMUELI)

