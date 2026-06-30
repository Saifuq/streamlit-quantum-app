# Streamlit Quantum App

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://app-quantum-app-rb4iw7spj9rql3f8gbgpt7.streamlit.app/)

An interactive web application built with Streamlit to visualize, simulate, and experiment with quantum computing concepts in real-time.

## Features

- **Quantum Circuit Builder:** Interactively design quantum circuits using standard logic gates (H, X, Y, Z, CNOT, etc.).
- **Real-Time Simulation:** Simulate quantum states and visualize measurement probability distributions instantly.
- **Statevector & Bloch Sphere Visualization:** Intuitive graphical representations of quantum states on the Bloch sphere.
- **Educational Tool:** Designed to make quantum mechanics and computing concepts approachable for beginners and researchers alike.

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
