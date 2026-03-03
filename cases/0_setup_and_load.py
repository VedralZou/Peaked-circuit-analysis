#example of import qasm file

import numpy as np
import requests
from qiskit import QuantumCircuit

import bluequbit
bq = bluequbit.init()

# Get Circuits (local file from your repo)
qc = QuantumCircuit.from_qasm_file("circuits/P1_little_peak.qasm")

print("Qubits:", qc.num_qubits)
print("Gate counts:", qc.count_ops())
