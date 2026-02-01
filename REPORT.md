# WiDS 5.0

This repository contains my implementation for the **Winter in Data Science (WiDS 5.0)** program at **IIT Bombay**. The project explores how we can automate mathematical reasoning using classical logic and optimized search algorithms.

## What’s inside?

### Week 1

I built the basic tools needed to handle logic expressions:
* **CNF Converter:** A tool to turn any logic statement into a standardized "Conjunctive Normal Form." It handles implications and De Morgan's laws recursively.
* **DPLL SAT Solver:** An implementation of the Davis-Putnam-Logemann-Loveland algorithm. It uses **Unit Propagation** to quickly solve propositional logic problems.
* **Robinson's Resolution:** A First-Order Logic (FOL) prover. I implemented the **Unification** algorithm with an **Occurs Check** to make sure the computer doesn't get stuck in infinite loops with variables.

### Week 2

* **Set of Support (SOS):** Forces the prover to only focus on clauses related to the goal, ignoring irrelevant axioms.
* **Subsumption:** A cleanup step that deletes redundant or weaker clauses so the memory doesn't blow up.
* **Given-Clause Algorithm:** The main loop that manages active and passive clauses to keep the search organized.
* **Heuristics:** I added a "weighting" system that prioritizes shorter clauses (since they are closer to finishing the proof).

## Project Structure
* `Week1/prop_logic/`: Code for CNF conversion and DPLL.
* `Week1/fol/`: Code for Robinson Resolution and Unification.
* `Week2/`: Theory and reading material links on 'how to make it fast?'

## Running the Code
Each week has an autograder to check the logic. 

```bash
# Test the Propositional Logic part
cd Week1/prop_logic
python3 autograder.py

# Test the FOL Resolution part
cd Week1/fol
python3 autograder.py
