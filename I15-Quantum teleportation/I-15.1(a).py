def state_preparation():
    ##################
    # YOUR CODE HERE #
    ##################

    # OPTIONALLY UPDATE THIS STATE PREPARATION ROUTINE

    qml.Hadamard(wires=0)
    qml.Rot(0.1, 0.2, 0.3, wires=0)
