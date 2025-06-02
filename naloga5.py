from siamfc_lt import TrackerSiamFC
from run_tracker_test import evaluate_tracker
import io

def just_write(file, text):
    with io.open(file, 'a', encoding='utf-8') as file:
        file.write(text)

if __name__ == '__main__':
    tracker = TrackerSiamFC(net_path=r'C:\Faks\NMRV\Project5\siamfc_net.pth')
    dataset = r'C:\Faks\NMRV\Project5\dataset'
    
    resultsAll, scoresAll = evaluate_tracker(dataset, tracker, False, 0)

        

    
  
        
    
    
        
    
    