#!/usr/bin/env python3
from typing import Generator
import time


def event_generator(count: int) -> Generator:
    players = ['alice', 'bob', 'charlie', 'diana', 'eve']
    events = ['killed monster', 'found treasure', 'leveled up', 'completed quest', 'joined party']
    
    player_index = 0
    event_index = 0
    level = 1
    
    for i in range(count):
        player = players[player_index]
        event = events[event_index]
        
        yield {
            'id': i + 1,
            'player': player,
            'level': level,
            'action': event
        }
        
        player_index = (player_index + 1) % len(players)
        event_index = (event_index + 2) % len(events)
        level = (level % 20) + 1


def filter_high_level(events: Generator, min_level: int) -> Generator:
    for event in events:
        if event['level'] >= min_level:
            yield event


def filter_by_action(events: Generator, action: str) -> Generator:
    for event in events:
        if action in event['action']:
            yield event


def fibonacci_generator(limit: int) -> Generator:
    a = 0
    b = 1
    count = 0
    
    while count < limit:
        yield a
        temp = a
        a = b
        b = temp + b
        count = count + 1


def prime_generator(limit: int) -> Generator:
    count = 0
    num = 2
    
    while count < limit:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        
        if is_prime:
            yield num
            count = count + 1
        
        num = num + 1


print("=== Game Data Stream Processor ===\n")
print("Processing 1000 game events...")
print()

start_time = time.time()

total_events = 0
high_level_count = 0
treasure_count = 0
levelup_count = 0

event_stream = event_generator(1000)

displayed = 0
for event in event_stream:
    total_events = total_events + 1
    
    if event['level'] >= 10:
        high_level_count = high_level_count + 1
    
    if 'treasure' in event['action']:
        treasure_count = treasure_count + 1
    
    if 'leveled up' in event['action']:
        levelup_count = levelup_count + 1
    
    if displayed < 3:
        print(f"Event {event['id']}: Player {event['player']} (level {event['level']}) {event['action']}")
        displayed = displayed + 1

print("...")
print()

end_time = time.time()
processing_time = round(end_time - start_time, 3)

print("=== Stream Analytics ===")
print(f"Total events processed: {total_events}")
print(f"High-level players (10+): {high_level_count}")
print(f"Treasure events: {treasure_count}")
print(f"Level-up events: {levelup_count}\n")
print("Memory usage: Constant (streaming)")
print(f"Processing time: {processing_time} seconds")
print()

print("=== Generator Demonstration ===")

fib_list = []
fib_gen = fibonacci_generator(10)
for num in fib_gen:
    fib_list = fib_list + [str(num)]
fib_str = ", ".join(fib_list)
print(f"Fibonacci sequence (first 10): {fib_str}")

prime_list = []
prime_gen = prime_generator(5)
for num in prime_gen:
    prime_list = prime_list + [str(num)]
prime_str = ", ".join(prime_list)
print(f"Prime numbers (first 5): {prime_str}")
print()

