from fuzzywuzzy import fuzz

def extract_target_line(lines):
    best_score = 0
    best_line = None

    for line in lines:
        score = fuzz.partial_ratio("_1_", line)

        if score > best_score:
            best_score = score
            best_line = line

    # 75% similarity means acceptable
    if best_score >= 70:
        return best_line
    return None
