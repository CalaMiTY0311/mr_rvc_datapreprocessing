import os

def filepath():
    now_dir = os.path.dirname(os.path.abspath(__file__))
    testfile = os.path.join(now_dir, "testfiles")
    return testfile