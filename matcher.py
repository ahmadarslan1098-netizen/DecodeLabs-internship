from collections import Counter


def compute_similarity(item, user_prefs, attr_keys):
    score = 0
    total_possible = 0

    for key in attr_keys:
        if key not in item:
            continue
        item_vals = set(item[key]) if isinstance(item[key], list) else {item[key]}
        user_vals = set(user_prefs.get(key, []))

        if not user_vals:
            continue

        total_possible += len(user_vals)
        overlap = item_vals & user_vals
        score += len(overlap)

    if total_possible == 0:
        return 0
    return score / total_possible


def rank_items(dataset, user_prefs, top_n=5):
    attr_keys = dataset["attr_keys"]
    items = dataset["items"]

    scored = []
    for item in items:
        sim = compute_similarity(item, user_prefs, attr_keys)
        if sim > 0:
            scored.append((item, sim))

    scored.sort(key=lambda x: x[1], reverse=True)
    return scored[:top_n]


def get_available_options(dataset):
    attr_keys = dataset["attr_keys"]
    items = dataset["items"]
    options = {}

    for key in attr_keys:
        all_vals = []
        for item in items:
            val = item.get(key, [])
            if isinstance(val, list):
                all_vals.extend(val)
            else:
                all_vals.append(val)
        options[key] = sorted(set(all_vals))

    return options
