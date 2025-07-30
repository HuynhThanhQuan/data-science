# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a data science learning repository containing educational materials, implementations, and problem-solving exercises. The repository is organized into several key areas:

### Structure
- **data-mentor/**: Educational courses and homework assignments
  - `data-course/`: Course materials organized by subject (CP, CS, FD)
  - `techstack/`: Technology-specific learning materials (Python analytics, SQL)
- **data-structure/**: Python implementations of fundamental data structures
- **machine-learning/**: ML projects and experiments in Jupyter notebooks
  - `logreg/`: Logistic regression implementations
  - `nlp/`: Natural language processing projects
  - `tree-based/`: Decision tree algorithms (CART)
- **solving-problem/**: Algorithmic problem-solving notebooks
- **google-meridian/**: Google Meridian related projects

## Development Environment

### Primary Technologies
- **Python**: Main programming language for data structures and algorithms
- **Jupyter Notebooks**: Primary environment for machine learning and data analysis work
- **Git**: Version control (currently on master branch)

### Working with Jupyter Notebooks
- Use `NotebookRead` and `NotebookEdit` tools for .ipynb files
- Notebooks are the primary format for ML experiments and problem-solving exercises
- Key notebooks include NLP.ipynb, CART implementations, and various problem-solving exercises

### Working with Python Files
- Data structure implementations use classic Python classes
- Code style follows older Python conventions (created around 2018)
- Files include docstrings with creation dates and author information

## Code Architecture

### Data Structures Module (`data-structure/`)
Contains standalone implementations of:
- Binary Search Trees (`BinarySearchTree.py`)
- Linked Lists (`SingleLinkedList.py`, `DoubleLinkedList.py`) 
- Queues (`CircularQueue.py`, `PriorityQueue.py`)
- Stacks (`StackByLinkedList.py`)
- Deques (`Deque.py`)

Each implementation follows a consistent pattern with Node classes and main container classes.

### Machine Learning Projects
- Organized by algorithm type (logreg, tree-based, nlp)
- Uses Jupyter notebooks for experimentation and visualization
- Includes both theoretical explanations and practical implementations

### Problem Solving
- Algorithmic challenges implemented in Jupyter notebooks
- Focus on string processing, sequence analysis, and data structure manipulation
- Includes specialized functions for parentheses structure analysis and similarity comparison

## Development Notes

- No package management files (requirements.txt, pyproject.toml) - dependencies managed manually
- No automated testing framework detected
- Code follows educational/learning patterns rather than production standards
- Repository serves as a personal learning and reference collection