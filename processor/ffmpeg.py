import os

dir = os.path.dirname(os.path.abspath(__file__))
# print(dir)
ff_path = os.path.join(dir, "ff_path")
os.environ["PATH"] = f'{os.environ["PATH"]};{ff_path}'

# print(ff_path)
