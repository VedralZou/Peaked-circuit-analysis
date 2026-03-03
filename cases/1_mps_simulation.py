import time
import warnings
import os

# os.environ["BLUEQUBIT_PPS_DO_NO_USE_PARALLEL_COMPUTE"] = "1"
os.environ["BLUEQUBIT_DEQART_INTERNAL_DISABLE_STRICT_VALIDATIONS"] = "1"

warnings.filterwarnings("ignore", category=UserWarning)

import numpy as np
import requests
from qiskit import QuantumCircuit

import bluequbit
bq = bluequbit.init()


# --------------------------
# Get Circuits
# --------------------------
def load_qasm(name: str) -> QuantumCircuit:
    """
    Load QASM2 circuit text from GitHub raw, then parse into a Qiskit QuantumCircuit.
    This follows the BlueQubit tutorial pattern.
    """
    url = f"https://raw.githubusercontent.com/BlueQubitDev/sdk-examples/main/peaked_circuits/qasm/{name}"
    qasm = requests.get(url).text
    return QuantumCircuit.from_qasm_str(qasm)


# --------------------------
# MPS Simulation (case)
# --------------------------
if __name__ == "__main__":
    # For MPS case, we use a larger circuit where full statevector is impractical.
    # (Following your plan: P4)
    qc = load_qasm("P4_gentle_mound.qasm")

    print("Qubits:", qc.num_qubits)
    print("Gate counts:", qc.count_ops())

    # Run MPS simulation
    shots = 500
    bond_dim = 32

    t0 = time.time()
    results_mps = bq.run(
        qc,
        device="mps.cpu",
        shots=shots,
        options={"mps_bond_dimension": bond_dim},
    )
    dt = time.time() - t0

    counts = results_mps.get_counts()

    # Sort and print top-10
    top10 = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:10]
    peak_bitstring = top10[0][0]

    print(f"\nMPS simulation runtime: {dt:.2f} s")
    print("Top-10 most frequent bitstrings (MPS):")
    for b, c in top10:
        print(f"{b}: {c}")

    print("\nPeak bitstring inferred from MPS samples:", peak_bitstring)
