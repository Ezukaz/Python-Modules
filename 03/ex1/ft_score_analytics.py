#!/usr/bin/env python3
"""Exercise 1: Score Cruncher - List-based player score analytics"""

import sys
from typing import List


def analyze_scores(score_args: List[str]) -> None:
    """Analyze player scores from command line using lists."""
    print("=== Player Score Analytics ===")

    if len(score_args) <= 1:
        print("No scores provided.")
        print("Usage: python3 ft_score_analytics.py <scores>...")
        return

    scores: List[int] = []
    for arg in score_args[1:]:
        try:
            scores.append(int(arg))
        except ValueError:
            print(f"Invalid score '{arg}' - skipping")
            continue

    if not scores:
        print("No valid scores found.")
        return

    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {sum(scores) / len(scores):.1f}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    analyze_scores(sys.argv)
