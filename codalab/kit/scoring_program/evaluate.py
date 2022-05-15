#!/usr/bin/env python
import os.path
import sys
import numpy as np

try:
    # installing dependencies
    os.system("pip install rouge-score")
    os.system("pip install pandas")
    os.system("pip install bert-score")
except Exception as e:
    print("Error occurred while installing dependencies ", e)
    exit()

input_dir = sys.argv[1]
output_dir = sys.argv[2]

submit_dir = os.path.join(input_dir, 'res')
truth_dir = os.path.join(input_dir, 'ref')

if not os.path.isdir(submit_dir):
    print(f"{submit_dir} doesn't exist")


def evaluate_metrics(test_annotation_file, user_submission_file, use_bertscore=True):
    from rouge_score import rouge_scorer
    import pandas as pd
    from bert_score import score as bert_score_func

    metrics = ['rouge1', 'rouge2', 'rougeL']
    ground_truth_df = pd.read_csv(test_annotation_file)
    print(f"processing ground truth file + {test_annotation_file}")
    submission_df = pd.read_csv(user_submission_file)
    print(f"processing submission file {user_submission_file}")

    scorer = rouge_scorer.RougeScorer(metrics, use_stemmer=True)
    results = {"rouge1_f": [], "rouge1_r": [], "rouge2_f": [], "rouge2_r": [], "rougeL_f": [], "rougeL_r": []}
    if len(ground_truth_df['paper_id'].unique()) == len(submission_df['paper_id'].unique()):
        print("Warning, number of unique 'paper_id's in submission is not equal to number of unique 'paper_id's in "
              "ground truth")

    bertscore_summaries = ([], [])
    for index, ground_truth_row in ground_truth_df.iterrows():
        ground_truth_summary = ground_truth_row['summary']
        article_id = ground_truth_row['paper_id']
        submission_summary_row = submission_df.loc[submission_df['paper_id'] == article_id]
        if submission_summary_row.empty:
            print(f"paper with id '{article_id}' wasn't found in submission")
            raise Exception(f"paper with id '{article_id}' wasn't found in submission")
        elif len(submission_summary_row.index) != 1:
            print(f"More than one summary submission for paper with id '{article_id}'")
            raise Exception(f"More than one summary submission for paper with id '{article_id}'")

        submission_summary = submission_summary_row.iloc[0]['summary']

        print(f"evaluating summary for article with id '{article_id}'")
        scores = scorer.score(ground_truth_summary.strip(), submission_summary.strip())
        final_score = []
        for rouge_metric in metrics:
            results[rouge_metric + "_f"].append(scores[rouge_metric].fmeasure)
            results[rouge_metric + "_r"].append(scores[rouge_metric].recall)
            final_score += [scores[rouge_metric].fmeasure]

        if use_bertscore:
            bertscore_summaries[0].append(submission_summary.strip())
            bertscore_summaries[1].append(ground_truth_summary.strip())

    metrics_scores = {rouge_metric: np.average(rouge_metric_scores)
                      for (rouge_metric, rouge_metric_scores) in results.items()}

    if use_bertscore:
        (P, R, F) = bert_score_func(cands=bertscore_summaries[0], refs=bertscore_summaries[1], lang="en")
        metrics_scores['BERTScore_P'] = P.mean().item()
        metrics_scores['BERTScore_R'] = R.mean().item()
        metrics_scores['BERTScore_F'] = F.mean().item()
        final_score += [F.mean().item()]

    metrics_scores['Metrics_Avg'] = sum(final_score) / len(final_score)
    return metrics_scores


if os.path.isdir(submit_dir) and os.path.isdir(truth_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_filename = os.path.join(output_dir, 'scores.txt')
    output_file = open(output_filename, 'w')

    truth_file = os.path.join(truth_dir, "testing.csv")
    submission_answer_file = os.path.join(submit_dir, "testing.csv")

    eval_scores = evaluate_metrics(test_annotation_file=truth_file, user_submission_file=submission_answer_file)
    for metric, metric_score in eval_scores.items():
        output_file.write(f"{metric}:{(metric_score * 100):.2f}\n")
    output_file.close()
