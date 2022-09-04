def entangle_qubits():
    ##################
    # YOUR CODE HERE #
    ##################
    qml.Hadamard(wires=1)
    qml.CNOT(wires=[1,2])

    # ENTANGLE THE SECOND QUBIT (WIRES=1) AND THE THIRD QUBIT
    
