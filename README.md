# Streamlit Quantum App

**Live App URL:** https://app-quantum-app-rb4iw7spj9rql3f8gbgpt7.streamlit.app/

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://app-quantum-app-rb4iw7spj9rql3f8gbgpt7.streamlit.app/)

An interactive web application built with Streamlit to visualize, simulate, and experiment with quantum computing concepts in real-time.

## Features

- **Quantum Circuit Builder:** Interactively design quantum circuits using standard logic gates (H, X, Y, Z, CNOT, etc.).
- **Real-Time Simulation:** Simulate quantum states and visualize measurement probability distributions instantly.
- **Statevector & Bloch Sphere Visualization:** Intuitive graphical representations of quantum states on the Bloch sphere.
- **Educational Tool:** Designed to make quantum mechanics and computing concepts approachable for beginners and researchers alike.

---

## Extended Description

The **Streamlit Quantum App** bridges the gap between complex quantum mechanics and intuitive visual comprehension. While quantum computing promises revolutionary advancements in cryptography, optimization, and molecular modeling, grasping the underlying mathematics (such as vector spaces, complex amplitudes, and entanglement) presents a steep learning curve. This platform functions as a no-code/low-code interactive laboratory for real-time quantum experimentation.

### Deep-Dive Core Mechanics

* **Dynamic Circuit Assembly & State Tracking:** As users add, remove, or modify gates on the front-end canvas, the application dynamically re-calculates the statevector under the hood. It maps individual qubit manipulations into Kronecker products of unitary matrices, providing a continuous look into state transitions without requiring the user to execute manual linear algebra operations.
    
* **The Bloch Sphere Intuition:** For single-qubit operations, the application tracks and projects the state onto a 3D Bloch Sphere. This allows users to physically *see* what an operation like a Hadamard ($H$) or a Pauli-X gate does—transforming abstract complex numbers into explicit geometric rotations along the $X$, $Y$, and $Z$ axes.
    
* **Simulated Quantum Stochasticity:** Beyond mathematical statevectors, the application includes a measurement simulator. Users can define the number of execution "shots" (e.g., 1024 runs), simulating how a theoretical quantum superposition collapses into definitive classical bitstrings ($00, 01, 10, 11$) in a real noisy quantum processing unit (QPU).

### Target Audience & Use Cases

* **Students & Educators:** Ideal for classroom demonstrations to demystify principles like quantum superposition, phase shifts, and constructive/destructive interference patterns.
* **Quantum Curious Developers:** Serves as an easy sandbox to prototype small-scale algorithms and understand gate behaviors before writing production-level Qiskit or Cirq code.
* **Researchers:** A quick, lightweight tool to verify small circuit geometries and quickly visualize probability distributions without setting up heavy local development notebooks.

---

## How It Works

The application leverages Python's advanced scientific libraries to model quantum mechanics right in your browser:

1. **Circuit Definition:** User inputs are translated into a quantum circuit representation.
2. **Statevector Computation:** The app calculates the exact statevector using matrix multiplication for the applied gates:
   $$\lvert \psi \rangle = U_n \dots U_2 U_1 \lvert 0 \rangle$$
3. **Measurement Visualization:** Simulates measurement collapses to output classic bit probabilities, rendered via dynamic charting tools.

---

## Supported Quantum Gates

The simulator currently supports the following operations:
- **Single-Qubit Gates:** Pauli-X (NOT), Pauli-Y, Pauli-Z, Hadamard (H), Phase (S, T).
- **Multi-Qubit Gates:** Controlled-NOT (CNOT / CX), CZ, Swap.
- **Measurement:** Z-basis measurement tracking.

---

## Directory Structure

```text
streamlit-quantum-app/
├── .streamlit/           # Streamlit configuration files
├── src/                  # Core application logic
│   ├── circuits.py       # Quantum circuit generation functions
│   └── visualization.py  # Bloch sphere and charting utilities
├── app.py                # Main Streamlit application entry point
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
