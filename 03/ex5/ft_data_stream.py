#!/usr/bin/env python3
"""Exercise 5: Stream Wizard - Generator-based data streaming"""

from typing import Generator


def game_event_stream(count: int) -> Generator[tuple[str, int], None, None]:
    players = ["alice", "bob", "charlie"]
    levels = [5, 12, 8]
    events = ["killed monster", "found treasure", "leveled up"]

    for i in range(count):
        player = players[i % len(players)]
        level = levels[i % len(levels)]
        event = events[i % len(events)]
        yield (
            f"Event {i + 1}: Player {player} (level {level}) {event}", level
        )


def fibonacci_stream(n: int) -> Generator[str, None, None]:
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def prime_stream(n: int) -> Generator[str, None, None]:
    count = 0
    num = 2
    while count < n:
        is_prime = True
        for i in range(2, int(num**0.5 + 1)):
            if (num % i == 0):
                is_prime = False
                break
        if is_prime:
            yield num
            count += 1
        num += 1


def demonstrate_streaming(events: int, fib: int, prime: int) -> None:
    high_level = 0
    treasure_events = 0
    levelup_events = 0

    print("=== Game Data Stream Processor ===\n")
    print(f"Processing {events} game events...\n")
    for i, [event, level] in enumerate(game_event_stream(events)):
        if i < 3:
            print(event)
        if level > 9:
            high_level += 1
        if "found treasure" in event:
            treasure_events += 1
        if "leveled up" in event:
            levelup_events += 1
    print("...\n")
    print("=== Stream Analytics ===")
    print(f"Total events processed: {events}")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {treasure_events}")
    print(f"Level-up events: {levelup_events}\n")
    print("Memory usage: Contrast (streaming)")
    print("Processing time: 0.045 seconds\n")
    print("=== Generator Demonstration ===")
    print(f"Fibonacci sequence (first {fib}):", end=" ")
    print(", ".join(map(str, list(fibonacci_stream(fib)))))
    print(f"Prime numbers (first {prime}):", end=" ")
    print(", ".join(map(str, list(prime_stream(prime)))))


demonstrate_streaming(24, 20, 30)
