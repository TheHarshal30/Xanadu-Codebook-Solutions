dev = qml.device("default.qubit", wires=3)

##################
# YOUR CODE HERE #
##################

# OPTIONALLY UPDATE THIS STATE PREPARATION ROUTINE
def state_preparation():
    qml.Hadamard(wires=0)
    qml.Rot(0.1, 0.2, 0.3, wires=0)


@qml.qnode(dev)
def teleportation():
    ##################
    # YOUR CODE HERE #
    ##################

    # USE YOUR QUANTUM FUNCTIONS TO IMPLEMENT QUANTUM TELEPORTATION
    state_preparation()
    entangle_qubits()
    rotate_and_controls()

    # RETURN THE STATE
    return qml.state()


print(teleportation())
