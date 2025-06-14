import argparse
import os
import cv2

from tools.sequence_utils import VOTSequence
from tools.sequence_utils import save_results
from siamfc_lt import TrackerSiamFC


def evaluate_tracker(dataset_path, network_path, results_dir, visualize):
    
    sequences = []
    with open(os.path.join(dataset_path, 'list.txt'), 'r') as f:
        for line in f.readlines():
            sequences.append(line.strip())

    tracker = TrackerSiamFC(net_path=network_path)

    for sequence_name in sequences:
        
        print('Processing sequence:', sequence_name)

        bboxes_path = os.path.join(results_dir, '%s_bboxes.txt' % sequence_name)
        scores_path = os.path.join(results_dir, '%s_scores.txt' % sequence_name)

        if os.path.exists(bboxes_path) and os.path.exists(scores_path):
            print('Results on this sequence already exists. Skipping.')
            continue
        
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
            #print(f'Processing frame {i}/{sequence.length() - 1}')

            img = cv2.imread(sequence.frame(i))
            prediction, score, draw = tracker.update(img)
            results.append(prediction)
            scores.append([score])

            if visualize:
                tl_ = (int(round(prediction[0])), int(round(prediction[1])))
                br_ = (int(round(prediction[0] + prediction[2])), int(round(prediction[1] + prediction[3])))
                if draw:
                    cv2.rectangle(img, tl_, br_, (0, 0, 255), 1)

                cv2.imshow('win', img)
                key_ = cv2.waitKey(10)
                if key_ == 27:
                    exit(0)
        
        save_results(results, bboxes_path)
        save_results(scores, scores_path)


parser = argparse.ArgumentParser(description='SiamFC Runner Script')

parser.add_argument("--dataset", help="Path to the dataset", required=True, action='store')
parser.add_argument("--net", help="Path to the pre-trained network", required=True, action='store')
parser.add_argument("--results_dir", help="Path to the directory to store the results", required=True, action='store')
parser.add_argument("--visualize", help="Show ground-truth annotations", required=False, action='store_true')

args = parser.parse_args()

evaluate_tracker(args.dataset, args.net, args.results_dir, args.visualize)
