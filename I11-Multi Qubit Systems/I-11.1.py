dev = qml.device('default.qubit', wires=3)

@qml.qnode(dev)
def make_basis_state(basis_id):
    """Produce the 3-qubit basis state corresponding to |basis_id>.
    
    Note that the system starts in |000>.

    Args:
        basis_id (int): An integer value identifying the basis state to construct.
        
    Returns:
        array[complex]: The computational basis state |basis_id>.
    """

    ##################
    # YOUR CODE HERE #
    ##################
    s = "{0:03b}".format(basis_id)
    if s[0] == "1":
        qml.PauliX(wires=0)
    if s[1] == "1":
        qml.PauliX(wires=1)
    if s[2] == "1":
        qml.PauliX(wires=2)

    # CREATE THE BASIS STATE
    
    return qml.state()


basis_id = 3
print(f"Output state = {make_basis_state(basis_id)}")
