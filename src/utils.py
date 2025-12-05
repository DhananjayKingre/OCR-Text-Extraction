import json
import os
from datetime import datetime

def save_json(output_folder, img_name, extracted_text, all_text_lines=None):

    os.makedirs(output_folder, exist_ok=True)
    
    data = {
        "image": img_name,
        "extracted_target_text": extracted_text,
        "timestamp": datetime.now().isoformat(),
        "all_detected_lines": all_text_lines if all_text_lines else []
    }
    
    out_path = os.path.join(
        output_folder,
        img_name.replace(".jpg", ".json").replace(".png", ".json").replace(".jpeg", ".json")
    )
    
    with open(out_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    
    return out_path

def calculate_accuracy(results_folder, ground_truth_file=None):
 
    if not ground_truth_file or not os.path.exists(ground_truth_file):
        return None
    
    with open(ground_truth_file, 'r') as f:
        ground_truth = json.load(f)
    
    correct = 0
    total = len(ground_truth)
    
    for img_name, true_value in ground_truth.items():
        json_file = os.path.join(results_folder, img_name.replace('.jpg', '.json'))
        
        if os.path.exists(json_file):
            with open(json_file, 'r') as f:
                result = json.load(f)
                if result['extracted_target_text'] == true_value:
                    correct += 1
    
    accuracy = (correct / total) * 100 if total > 0 else 0
    return accuracy

def save_screenshot(img_path, output_folder):
   
    import cv2
    img = cv2.imread(img_path)
    if img is not None:
        os.makedirs(output_folder, exist_ok=True)
        filename = os.path.basename(img_path)
        output_path = os.path.join(output_folder, f"screenshot_{filename}")
        cv2.imwrite(output_path, img)
        return output_path
    return None
