dev = qml.device("default.qubit", wires=1)

##################
# YOUR CODE HERE #
##################

# OPTIONALLY REPLACE THIS STATE PREPARATION ROUTINE WITH
# THE ONE FROM THE PREVIOUS EXERCISE

def state_preparation():
    qml.Hadamard(wires=0)
    qml.Rot(0.1, 0.2, 0.3, wires=0)


@qml.qnode(dev)
def state_prep_only():
    state_preparation()
    return qml.state()

print(state_prep_only())
