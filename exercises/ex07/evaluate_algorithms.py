"""Analyze runtime and memory usage."""

__author__ = "730411985"

# kept getting error that 'exercises doesnt exist so found below solution online'
import sys
sys.path.append('/Users/alanaq/Desktop/comp110-24s-workspace')

import matplotlib.pyplot as plt
from exercises.ex07.runtime_analysis_functions import evaluate_runtime
from exercises.ex07.runtime_analysis_functions import evaluate_memory_usage

START_SIZE: int = 0
END_SIZE: int = 1000

usage = evaluate_memory_usage("selection_sort", START_SIZE, END_SIZE)
plt.plot(usage)
plt.title("Memory Usage Analysis of Selection Sort - alanaq")
plt.show()
 
usage = evaluate_memory_usage("insertion_sort", START_SIZE, END_SIZE)
plt.plot(usage)
plt.title("Memory Usage Analysis of Insertion Sort - alanaq")
plt.show()