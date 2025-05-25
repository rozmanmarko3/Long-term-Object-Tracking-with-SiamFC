from siamfc_lt import TrackerSiamFC
from performance_evaluation import evaluate_performance
from run_tracker_test import evaluate_tracker

if __name__ == '__main__':
    tracker = TrackerSiamFC(net_path=r'C:\Faks\NMRV\Project5\siamfc_net.pth')
    dataset = r'C:\Faks\NMRV\Project5\dataset'
    
    results = {}
    
    tresholds = [3,3.5,4,4.5,5,5.5,6]
    tresholds = [4]
    for t in tresholds:
        tracker.start_tracking_treshold = t
        print(f'Threshold set to {t}')
        resultsAll, scoresAll = evaluate_tracker(dataset, tracker)
        pr, re, f = evaluate_performance(dataset,None, resultsAll, scoresAll)
        results[t] = (pr, re, f)
        
    print('Results:')
    for t, (pr, re, f) in results.items():
        print(f'Threshold: {t}, Precision: {pr:.4f}, Recall: {re:.4f}, F-score: {f:.4f}')
    
    #save_results(results, 'results.yaml')
    import yaml
    with open('results.yaml', 'w') as f:
        yaml.dump(results, f, default_flow_style=False)
    
    