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
    file_name = 'results4.csv'
    
    just_write(file_name, 'redetection_n,Precision,Recall,F-score\n')
    

    redetection_n = [5,10,20,30,40,50]
    for t in redetection_n:
        tracker.start_tracking_treshold = 3
        tracker.search_n = t
        print(f'redetection_n set to {t}')
        resultsAll, scoresAll = evaluate_tracker(dataset, tracker)
        
        pr, re, f = evaluate_performance(dataset, resultsAll, scoresAll)
        results.append({
            'treshold': t,
            'pr': pr,
            're': re,
            'f': f
        })
        
        just_write(file_name, f'{t},{pr:.4f},{re:.4f},{f:.4f}\n')
        

    
  
        
    
    
        
    
    