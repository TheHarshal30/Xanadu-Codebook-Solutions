def extract_qubit_state(input_state):
    """Extract the state of the third qubit from the combined state after teleportation.
    
    Args:
        input_state (array[complex]): A 3-qubit state of the form 
            (1/2)(|00> + |01> + |10> + |11>) (a|0> + b|1>)
            obtained from the teleportation protocol.
            
    Returns:
        array[complex]: The state vector np.array([a, b]) of the third qubit.
    """

    ##################
    # YOUR CODE HERE #
    ##################
    

    # DETERMINE THE STATE OF THE THIRD QUBIT

    return np.array([2*input_state[0], 2*input_state[1]])
    

# Here is the teleportation routine for you
dev = qml.device("default.qubit", wires=3)

#################
# YOUR CODE HERE #
##################

# OPTIONALLY UPDATE THIS STATE PREPARATION ROUTINE
def state_preparation():
    qml.Hadamard(wires=0)
    qml.Rot(0.1, 0.2, 0.3, wires=0)


@qml.qnode(dev)
def teleportation():
    state_preparation()
    entangle_qubits()
    rotate_and_controls()    
    return qml.state()

# Print the extracted state after teleportation
full_state = teleportation()
print(extract_qubit_state(full_state))
