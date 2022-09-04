def rotate_and_controls():
    ##################
    # YOUR CODE HERE #
    ##################

    # PERFORM THE BASIS ROTATION

    # PERFORM THE CONTROLLED OPERATIONS
    qml.CNOT(wires=[0,1])
    qml.Hadamard(wires=0)
    qml.CNOT(wires=[1,2])
    qml.CZ(wires=[0,2])

