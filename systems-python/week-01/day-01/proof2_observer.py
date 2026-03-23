# PROOF 2: Measuring changes the system
import sys

x = 20000
print("=== The Observer Effect ===")
print(f"Object value: {x}")
print(f"Reference count: {sys.getrefcount(x)}")
print("Expected 1. Got more.")
print("The act of measuring added a reference.")
print("Observation changed the system.")