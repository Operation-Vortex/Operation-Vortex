import random

levels = ["INFO", "WARNING", "ERROR", "DEBUG"]
messages = [
    "User logged in",
    "Database connection failed",
    "Request processed",
    "Disk space low",
    "Payment timeout",
    "Cache miss",
    "Authentication failed",
    "File not found"
]

with open("server.log", "w") as f:
    for i in range(1_000_000):
        level = random.choice(levels)
        message = random.choice(messages)
        f.write(f"2025-03-30 {i % 24:02d}:00:00 [{level}] {message}\n")

print("Done. 1 million log lines written.")