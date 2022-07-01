# Multi Perspective Scientific Document Summarization

This repository contains the dataset and baseline models for the Multi Perspective Scientific Document Summarization (MuP) shared task to be held at [SDP in COLING 2022](https://sdproc.org/2022/index.html).

## Important announcements (May 16, 2022) :
- See below the timeline for the task.
- If you would like to participate please fill up this [form](https://forms.gle/K2UECKvmghzDHUpo7).

## Introduction

Generating summaries of scientific documents is known to be a challenging task. Majority of existing work in summarization assumes only one single best gold summary for each given document. Having only one gold summary negatively impacts our ability to evaluate the quality of summarization systems as writing summaries is a subjective activity. At the same time, annotating multiple gold summaries for scientific documents can be extremely expensive as it requires domain experts to read and understand long scientific documents. This shared task will enable exploring methods for generating multi-perspective summaries. We introduce a novel summarization corpus, leveraging data from scientific peer reviews to capture diverse perspectives from the reader's point of view.

Peer reviews in various scientific fields often include an introductory paragraph that summarizes the key contributions of a paper from the reviewer standpoint and each paper usually receives multiple reviews. We leverage data from OpenReview, an open and publicly available platform for scientific publishing.  We collect a corpus of papers and their reviews from venues on openreview such as ICLR, NeurIPS, and AKBC primarily from the AI, Machine Learning and Natural Language Processing fields. We use carefully designed heuristics to only include first paragraphs of reviews that are summary-like. We manually check the summaries obtained from this approach on a subset of the data and ensure the high quality of the summaries.
The corpus contains a total of around 10K papers, and 26.5K summaries (with average number of 2.57 summaries per paper). The summaries are on average 100.1 words long (space tokenized).

This is the distribution of number of summaries:
| Num of Summaries | Num of Papers |
| --- | --- |
| 1| 2276 |
| 2| 3039 |
| 3 | 2867 |
| 4 | 1827|
| 5| 225|
| >5 | 257|


If you use this dataset please cite:

## MuP Data and Instructions

You can download the data in one of the following ways:

### Download

You can directly download the full data from this [link](https://ai2-s2-research-public.s3-us-west-2.amazonaws.com/mup-dataset/mup.zip).  
`Expected size:  405M`

```bash
wget https://ai2-s2-research-public.s3-us-west-2.amazonaws.com/mup-dataset/mup.zip
```

The downloaded zip file includes the following files:

Simplified csv files (includes the preprocessed first 2000 tokens of each paper):  
```
training.csv   
validation.csv
```

Jsonlines file containing the full text of papers with section information. 
This is the output of the pdf parsing program (ScinceParse) and would be useful if you want to utilize the full paper or information about sections or additional metadata.

```
training_complete.jsonl   
validation_complete.jsonl
```

### Through Huggingface datasets library

The dataset is also hosted on Huggingface.
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

## Test Data

Here is the link to the test data: https://ai2-s2-research-public.s3-us-west-2.amazonaws.com/mup-dataset/testing_with_paper_release.jsonl.zip

## Evaluation Scheme

The intrinsic evaluation will be done by ROUGE, using ROUGE-1, -2, -L metrics. The average of the ROUGE-F scores obtained against the multiple summaries would be used for final ranking.

## Submission Instructions
We will use [Codalab](https://codalab.lisn.upsaclay.fr/) to evaluate submissions against the hidden test set.
Please follow the below instructions to evaluate and report your team results: 
1. Create a [Codalab](https://codalab.lisn.upsaclay.fr/) account 
2. In the "User Settings" pane, and under "Competition settings", set "Team name" to the name you are using for the shared task (this name will appear in the leaderboard)
3. Create a `testing.csv` file with your system generated summaries on the test set. The submission should be **a single csv file** containing **all generated test set summaries**. The file should have two columns: 
```csv
paper_id,summary
```
3. Compress `testing.csv` file into `testing.zip` file
4. Login to Codalab, select the competition: [https://codalab.lisn.upsaclay.fr/competitions/5676](https://codalab.lisn.upsaclay.fr/competitions/5676)
5. Select the Participate tab--> [Submit / View Results](https://codalab.lisn.upsaclay.fr/competitions/5676#participate-submit_results). Select the Submit button and choose your local `testing.zip` file (from step 3). The table below the Submit button will show the status of your submission.
6. Once the submission is uploaded and evaluated against the hidden test set the status will change to Finished. You can choose to report your results to the leaderboard or to download the scores to a text file by selecting the `Download output from scoring step` option. 

**Make sure to report the highest obtained score to the leaderboard before the evaluation period ends**

Evaluation Script: https://github.com/allenai/mup/blob/main/codalab/kit/scoring_program/evaluate.py

## Leaderboard
[https://codalab.lisn.upsaclay.fr/competitions/5676#results](https://codalab.lisn.upsaclay.fr/competitions/5676#results)

## Shared Task Timelines

Training Data Release:  May 10, 2022  <br />
Test Data Release:  June 30, 2022 <br />
Evaluation Period:  July 15, 2022 <br />
System Description Papers Due:  August 1, 2022<br />
Reviews Notification:  August 15, 2022 <br />
Camera-Ready Papers Due:  September 5, 2022<br />
Event at SDP @ COLING 2022:  October 16/17, 2022<br />

## License

The data is released under the 'ODC-BY' license.

## Disclaimer

## MuP 2022 Organizers

1. [Guy Feigenblat - Piiano](https://Piiano.com)
2. [Arman Cohan- AI2](http://armancohan.com/)
3. [Tirthankar Ghosal- Institute of Formal and Applied Linguistics, Charles University, Czech Republic](https://elitr.eu/tirthankar-ghosal/)
4. [Michal Shmueli-Scheuer - IBM Research AI](https://researcher.watson.ibm.com/researcher/view.php?person=il-SHMUELI)

