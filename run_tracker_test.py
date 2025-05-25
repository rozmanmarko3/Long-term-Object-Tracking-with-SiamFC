import argparse
import os
import cv2

from tools.sequence_utils import VOTSequence
from tools.sequence_utils import save_results
from siamfc_lt import TrackerSiamFC
from performance_evaluation import evaluate_performance

def evaluate_tracker(dataset_path, tracker):
    visualize = True
    sequences = []
    with open(os.path.join(dataset_path, 'list.txt'), 'r') as f:
        for line in f.readlines():
            sequences.append(line.strip())
    resultsAll = {}
    scoresAll = {}

    for sequence_name in sequences:
        
        print('Processing sequence:', sequence_name)


        
        sequence = VOTSequence(dataset_path, sequence_name)
        initFrame = 0
        img = cv2.imread(sequence.frame(initFrame))
        gt_rect = sequence.get_annotation(initFrame)
        tracker.init(img, gt_rect)
        results = [gt_rect]
        scores = [[10000]]  # a very large number - very confident at initialization

        if visualize:
            cv2.namedWindow('win', cv2.WINDOW_AUTOSIZE)
        for i in range(1 + initFrame, sequence.length()):
            print(f'Processing frame {i}/{sequence.length() - 1}')

            img = cv2.imread(sequence.frame(i))
            prediction, score = tracker.update(img)
            results.append(prediction)
            scores.append([score])

            if visualize:
                tl_ = (int(round(prediction[0])), int(round(prediction[1])))
                br_ = (int(round(prediction[0] + prediction[2])), int(round(prediction[1] + prediction[3])))
                cv2.rectangle(img, tl_, br_, (0, 0, 255), 1)

                cv2.imshow('win', img)
                key_ = cv2.waitKey(10)
                if key_ == 27:
                    exit(0)
        
        resultsAll[sequence_name] = results
        scoresAll[sequence_name] = scores
    
    return resultsAll, scoresAll


