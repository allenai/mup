# Multi Perspective Scientific Document Summarization

This repository contains the dataset and baseline models for the Multi Perspective Scientific Document Summarization (MuP) shared task to be held at [SDP in COLING 2022](https://sdproc.org/2022/index.html).

### Introduction

Generating summaries of scientific documents is known to be a challenging task. Majority of existing work in summarization assumes only one single best gold summary for each given document. Having only one gold summary negatively impacts our ability to evaluate the quality of summarization systems as writing summaries is a subjective activity. At the same time, annotating multiple gold summaries for scientific documents can be extremely expensive as it requires domain experts to read and understand long scientific documents. This shared task will enable exploring methods for generating multi-perspective summaries. We introduce a novel summarization corpus, leveraging data from scientific peer reviews to capture diverse perspectives from the reader's point of view.

Peer reviews in various scientific fields often include an introductory paragraph that summarizes the key contributions of a paper from the reviewer standpoint and each paper usually receives multiple reviews. We leverage data from OpenReview, an open and publicly available platform for scientific publishing.  We collect a corpus of papers and their reviews from venues on openreview such as ICLR, NeurIPS, and AKBC primarily from the AI, Machine Learning and Natural Language Processing fields. We use carefully designed heuristics to only include first paragraphs of reviews that are summary-like. We manually check the summaries obtained from this approach on a subset of the data and ensure the high quality of the summaries.
The corpus contains a total of 12K papers, and 27K summaries (with average number of 2.57 summaries per paper). The summaries are on average 100.1 words long (space tokenized).

If you use this dataset please cite:

### MuP Data and Instructions

# Training Data

### Submission Instructions

Evaluation Script: 

### Shared Task Timelines

Training Data Release:  <br />
Test Data Release:  <br />
Evaluation Period:  <br />
Results Submission:  <br />
Notification:  <br />
System Description Papers Due:  <br />
Reviews Notification:  <br />
Camera-Ready Papers Due:  <br />
Event at SDP @ COLING 2022:  <br />

### License

### Disclaimer

### MuP 2022 Organizers

1. Guy Feigenblat
2. Arman Cohan
3. Tirthankar Ghosal
4. Michal Shmueli-Scheuer

