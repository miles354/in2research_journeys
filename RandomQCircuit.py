#Same as DefinedQCircuit.py but with randomised number of qubits and gates
import matplotlib
matplotlib.use("Agg")  # Non-GUI backend

import random
from math import pi
import matplotlib.pyplot as plt

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector, partial_trace
from qiskit.visualization import circuit_drawer
from qiskit.visualization.bloch import Bloch

# Parameters
num_qubits = random.randint(3,6)
num_gates = random.randint(15,30)
# Gate options
single_qubit_gates = ['h', 'x', 'y', 'z', 'rx', 'ry', 'rz', 't', 's', 'sdg']
two_qubit_gates = ['cx', 'cz', 'swap']
three_qubit_gates = ['ccx', 'ccz']

# Create random circuit
qc = QuantumCircuit(num_qubits)
for i in range(num_gates):
    gate_type = random.choice(single_qubit_gates + two_qubit_gates + three_qubit_gates)

    if gate_type in single_qubit_gates:
        q = random.randint(0, num_qubits - 1)
        if gate_type in ['rx', 'ry', 'rz']:
            angle = random.choice([pi * 1/4, pi * 1/2, pi * 3/4, pi, pi * 5/4, pi * 3/2, pi * 7/4, pi * 2])
            getattr(qc, gate_type)(angle, q)
        else:
            getattr(qc, gate_type)(q)

    elif gate_type in two_qubit_gates and num_qubits >= 2:
        q1, q2 = random.sample(range(num_qubits), 2)
        getattr(qc, gate_type)(q1, q2)

    elif gate_type in three_qubit_gates and num_qubits >= 3:
        q1, q2, q3 = random.sample(range(num_qubits), 3)
        getattr(qc, gate_type)(q1, q2, q3)

# Save circuit diagram as image (not just drawing)
circuit_img = circuit_drawer(qc, output="mpl")
circuit_img.savefig("circuit_random_diagram.png")

# Simulate final state
state = Statevector.from_instruction(qc)

# Reduced density matrices for each qubit
reduced_dms = [partial_trace(state, [j for j in range(num_qubits) if j != i]) for i in range(num_qubits)]

# Bloch vector calculation
def get_bloch_components(dm):
    x = 2 * dm.data[0, 1].real
    y = 2 * dm.data[0, 1].imag
    z = dm.data[0, 0].real - dm.data[1, 1].real
    return [x, y, z]

# Save Bloch spheres for each qubit
for i, dm in enumerate(reduced_dms):
    b = Bloch()
    b.add_vectors(get_bloch_components(dm))
    b.title = f"Qubit {i}"
    b.save(f"bloch_random_qubit_{i}.png")
    b.render()

depth = qc.depth()
print("Circuit depth:", depth)
print("Gate Count", num_gates)
