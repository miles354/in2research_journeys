import matplotlib
matplotlib.use("Agg")  # Use non-GUI backend for image saving

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector, partial_trace
from qiskit.visualization.bloch import Bloch
import matplotlib.pyplot as plt
from math import pi

# Create the circuit
qc = QuantumCircuit(4)

# Layer 1: Initialization and superposition
qc.h(0)
qc.h(1)
qc.h(2)
qc.h(3)

# Layer 2: Entanglement
qc.cx(0, 1)
qc.cy(1, 2)
qc.cx(3, 1)
qc.cz(0, 2)

# Layer 3: Conditional logic and entanglement
qc.ccz(0, 1, 2)
qc.ccx(2, 1, 0)

# Layer 4: Rotations and phase shifts
qc.rx(pi / 3, 0)
qc.ry(pi / 4, 1)
qc.rz(pi / 5, 2)

# Layer 5: More gates for depth
qc.cz(0, 2)
qc.swap(1, 2)
qc.ry(pi / 2, 1)
qc.t(2)
qc.sdg(0)

# Draw and save the circuit diagram
qc.draw("mpl", filename="circuit_test_diagram.png")

# Simulate final state
state = Statevector.from_instruction(qc)

# Get reduced density matrices for each individual qubit
reduced_dms = [partial_trace(state, [j for j in range(4) if j != i]) for i in range(4)]

# Function to extract Bloch vector components
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
    b.save(f"bloch__test_qubit_{i}.png")
    b.render()

