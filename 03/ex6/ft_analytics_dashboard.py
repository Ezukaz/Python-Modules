#!/usr/bin/env python3

def comprehension_demo() -> None:
    leaderboard = [
        {"player": "EP_Farm", "score": 8500, "rank": 45, "acc": 97.2},
        {"player": "ExamCrusher", "score": 9200, "rank": 23, "acc": 99.1},
        {"player": "BonusEater", "score": 7800, "rank": 89, "acc": 94.5},
        {"player": "SinCity42", "score": 7100, "rank": 156, "acc": 98.8}
    ]

    # Set comps
    players = {p["player"] for p in leaderboard}
    elite_ranks = {p["rank"] for p in leaderboard if p["rank"] <= 50}
    high_acc_players = {p["player"] for p in leaderboard if p["acc"] > 98}
    # List comps
    ranks = [p["rank"] for p in leaderboard]
    scores = [p["score"] for p in leaderboard]
    score_ratios = [round(score/rank, 1) for score, rank in zip(scores, ranks)]
    # Dict comps
    players_ranks = {p["player"]: p["rank"] for p in leaderboard}
    efficiencies = {
        p["player"]: round(p["score"]/p["rank"], 1) for p in leaderboard
    }
    rank_ranges = {
        f"{r}-{r+49}": sum(1 for p in leaderboard if r <= p["rank"] < r+50)
        for r in [1, 51, 101]
    }

    total_stats = {
        "total_players": len(players),
        "top_ratio": max(p for p in score_ratios),
        "elite_count": sum(1 for _ in elite_ranks),
        "high_acc_players": len(high_acc_players),
        # Get the key of the highest value
        "best_harvester": max(efficiencies, key=efficiencies.get),
        "highest_rank": min(players_ranks, key=players_ranks.get),
        "missing_range": [r for r, c in rank_ranges.items() if c == 0],
    }

    # Print Output
    print("=== Game Analytics Dashboard ===\n")
    print("=== Set Comprehension Examples ===")
    print(f"High accuracy players: {high_acc_players}")
    print(f"Elite online ranks: {elite_ranks}")
    print(f"Active players: {players}\n")

    print("=== Dict Comprehension Examples ===")
    print(f"Rank: {players_ranks}")
    print(f"Efficiency: {efficiencies}")
    print(f"Rank range count: {rank_ranges}\n")

    print("=== List Comprehension Examples ===")
    print(f"Online ranks: {ranks}")
    print(f"Gained scores: {scores}")
    print(f"Score rates: {score_ratios}\n")

    print("=== Combined Analysis ===")
    print(f"Total players: {total_stats['total_players']}")
    print(f"Highest rate: {total_stats['top_ratio']}")
    print(f"Elite players: {total_stats['elite_count']}")
    print(f"High accuracy players: {total_stats['high_acc_players']}")
    print(f"Best harvester: {total_stats['best_harvester']}")
    print(f"Current highest rank: {total_stats['highest_rank']}")
    print(f"Rank ranges not currently online: {total_stats['missing_range']}")


if __name__ == "__main__":
    comprehension_demo()
