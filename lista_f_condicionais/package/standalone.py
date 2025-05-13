from pathlib import Path
print('Running' if __name__ == '__main__' else 'Importing', Path(__file__).resolve())
from . import module  # explicit relative import