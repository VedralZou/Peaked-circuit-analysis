# Classical Analysis of Peaked Quantum Circuits

This repository explores classical strategies for extracting peak bitstrings from structured "peaked" quantum circuits, inspired by the MIT × BlueQubit Peaked Circuits Hackathon.

The goal is not to reproduce the tutorial, but to implement and compare three classical approaches for analyzing structured quantum circuits.

---

## Methods Implemented

### 1. Matrix Product State (MPS) Simulation
Uses tensor network compression to approximate quantum states.
Suitable for circuits with limited entanglement.

### 2. Marginal Attack (Single-Qubit Expectation Values)
Reconstructs the peak bitstring by evaluating single-qubit ⟨Z_i⟩ expectation values and exploiting output bias.

### 3. Pauli-Path Simulator (PPS) Marginal Attack
Uses backward Pauli propagation (Heisenberg picture) to efficiently compute expectation values for large circuits.

---

## Structure
cases/
mps_simulation.py
marginal_attack.py
pauli_path_attack.py

Each file demonstrates one classical method on a representative peaked circuit instance.

---

## Focus

This project investigates:

- Structural properties of peaked circuits
- Classical simulation limits
- Entanglement sensitivity
- Trade-offs between accuracy and runtime


## References

This project follows and implements methods described in:

- BlueQubit SDK Examples – Peaked Circuits Tutorial  
  https://app.bluequbit.io/tutorial/91OgcR5O1GqFpues  

- MIT × BlueQubit Peaked Circuits Hackathon
