#!/usr/bin/env python3
"""Exercise 6: Data Alchemist - Comprehension mastery dashboard"""


def demonstrate_comprehensions() -> None:
    """Demonstrate all comprehension types for game analytics."""

    # Sample data
    player_scores = [
        ("alice", 2300),
        ("bob", 1800),
        ("charlie", 2150),
        ("diana", 2200)
    ]
    achievements = {
        "alice": ["first_kill", "level_10", "boss_slayer"],
        "bob": ["first_kill", "speed_demon"],
        "charlie": ["level_10", "boss_slayer", "collector", "treasure_hunter"]
    }
    regions = ["north", "east", "central", "north", "east"]

    print("=== Game Analytics Dashboard ===")

    print("\n=== List Comprehension Examples ===")
    high_scorers = [name for name, score in player_scores if score > 2000]
    print(f"High scorers (>2000): {high_scorers}")

    doubled_scores = [score * 2 for name, score in player_scores]
    print(f"Scores doubled: {doubled_scores}")

    active_players = [name for name in achievements.keys()]
    print(f"Active players: {active_players}")

    print("\n=== Dict Comprehension Examples ===")
    score_dict = {name: score for name, score in player_scores}
    print(f"Player scores: {score_dict}")

    score_cats = {}
    for name, score in player_scores:
        if score > 2000:
            score_cats.setdefault("high", 0)
            score_cats["high"] += 1
        elif score > 1800:
            score_cats.setdefault("medium", 0)
            score_cats["medium"] += 1
        else:
            score_cats.setdefault("low", 0)
            score_cats["low"] += 1
    print(f"Score categories: {score_cats}")

    ach_counts = {player: len(achs) for player, achs in achievements.items()}
    print(f"Achievement counts: {ach_counts}")

    print("\n=== Set Comprehension Examples ===")
    unique_players = {name for name, _ in player_scores}
    print(f"Unique players: {unique_players}")

    unique_achievements = {
        ach for achs in achievements.values() for ach in achs
    }
    print(f"Unique achievements: {unique_achievements}")

    active_regions = {region for region in regions}
    print(f"Active regions: {active_regions}")

    print("\n=== Combined Analysis ===")
    total_players = len(unique_players)
    avg_score = sum(score for _, score in player_scores) / len(player_scores)
    top_player = max(player_scores, key=lambda x: x[1])
    print(f"Total players: {total_players}")
    print(f"Total unique achievements: {len(unique_achievements)}")
    print(f"Average score: {avg_score:.1f}")
    print(
        f"Top performer: {top_player[0]} ({top_player[1]} points, "
        f"{ach_counts[top_player[0]]} achievements)"
    )


if __name__ == "__main__":
    demonstrate_comprehensions()
