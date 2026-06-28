from database import DATASETS, get_dataset
from matcher import rank_items, get_available_options


def display_header():
    print("=" * 60)
    print("  PROJECT 3: AI RECOMMENDATION LOGIC")
    print("=" * 60)


def display_dataset_menu():
    print("\nSelect a category:")
    for i, (name, info) in enumerate(DATASETS.items(), 1):
        print(f"  {i}. {name.title()} - {info['description']}")


def get_user_choice(options_dict, prompt):
    print(f"\n{prompt}")
    for key, values in options_dict.items():
        print(f"  {key.title()}: {', '.join(values)}")

    user_prefs = {}
    for key, values in options_dict.items():
        while True:
            raw = input(f"\n  Enter {key} (comma-separated, or 'any'): ").strip().lower()
            if raw == "any" or raw == "":
                user_prefs[key] = []
                print(f"  -> Any {key} selected")
                break
            choices = [c.strip() for c in raw.split(",") if c.strip() in values]
            invalid = [c.strip() for c in raw.split(",") if c.strip() and c.strip() not in values]
            if invalid:
                print(f"  Invalid {key}: {', '.join(invalid)}")
                print(f"  Available: {', '.join(values)}")
                continue
            if choices:
                user_prefs[key] = choices
                print(f"  -> Selected {key}: {', '.join(choices)}")
                break

    return user_prefs


def display_recommendations(results, item_type):
    if not results:
        print(f"\nNo {item_type} found matching your preferences.")
        print("Try different or broader preferences.")
        return

    print(f"\n{'=' * 50}")
    print(f"  TOP {len(results)} {item_type.upper()} RECOMMENDED FOR YOU")
    print(f"{'=' * 50}")

    for rank, (item, score) in enumerate(results, 1):
        title = item["title"]
        match_pct = score * 100

        print(f"\n  #{rank} {title}")
        print(f"      Match: {'*' * int(match_pct // 10)}{'.' * (10 - int(match_pct // 10))} {match_pct:.0f}%")

        for key in item:
            if key in ("id", "title"):
                continue
            val = item[key]
            if isinstance(val, list):
                print(f"      {key.title()}: {', '.join(val)}")
            else:
                print(f"      {key.title()}: {val}")

    print(f"\n{'=' * 50}")


def main():
    display_header()

    display_dataset_menu()
    while True:
        choice = input("\nEnter choice (1-3): ").strip()
        if choice in ("1", "2", "3"):
            dataset_name = list(DATASETS.keys())[int(choice) - 1]
            break
        print("Invalid choice. Enter 1, 2, or 3.")

    dataset = get_dataset(dataset_name)
    options = get_available_options(dataset)
    user_prefs = get_user_choice(options, f"What are your {dataset_name} preferences?")

    print("\nFinding best matches...")
    results = rank_items(dataset, user_prefs, top_n=5)
    display_recommendations(results, dataset_name)
    input("\nPress Enter to exit...")


if __name__ == "__main__":
    main()
