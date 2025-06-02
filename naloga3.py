from siamfc_lt import TrackerSiamFC
from performance_evaluation import evaluate_performance
from run_tracker_test import evaluate_tracker
import io

def just_write(file, text):
    with io.open(file, 'a', encoding='utf-8') as file:
        file.write(text)

if __name__ == '__main__':
    tracker = TrackerSiamFC(net_path=r'C:\Faks\NMRV\Project5\siamfc_net.pth')
    dataset = r'C:\Faks\NMRV\Project5\dataset'
    
    results = []
    
    just_write('results.csv', 'Threshold,Precision,Recall,F-score\n')
    

    tresholds = [2.0, 2.5]
    
    for t in tresholds:
        tracker.start_tracking_treshold = t
        print(f'Threshold set to {t}')
        resultsAll, scoresAll = evaluate_tracker(dataset, tracker)
        
        pr, re, f = evaluate_performance(dataset, resultsAll, scoresAll)
        results.append({
            'treshold': t,
            'pr': pr,
            're': re,
            'f': f
        })
        
        just_write('results.csv', f'{t},{pr:.4f},{re:.4f},{f:.4f}\n')
        
    print('Results:')
    for t, (pr, re, f) in results.items():
        print(f'Threshold: {t}, Precision: {pr:.4f}, Recall: {re:.4f}, F-score: {f:.4f}')
    
  
        
    
    