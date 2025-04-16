#!/usr/bin/env python

# Simple test script to verify Python environment
print("Python environment is working correctly")

# Try to import common packages that should be in requirements.txt
try:
    import requests
    print("Successfully imported requests")
except ImportError:
    print("Failed to import requests")

try:
    import supabase
    print("Successfully imported supabase")
except ImportError:
    print("Failed to import supabase") 