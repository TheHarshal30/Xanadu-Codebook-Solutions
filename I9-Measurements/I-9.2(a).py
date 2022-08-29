##################
# YOUR CODE HERE #
##################
dev = qml.device("default.qubit", wires=1)



# WRITE A QUANTUM FUNCTION THAT PREPARES (1/2)|0> + i(sqrt(3)/2)|1>
def prepare_psi():
    state = np.array([1/2, 1j*(np.sqrt(3)/2)])
    qml.MottonenStatePreparation(state_vector = state, wires=0)

# WRITE A QUANTUM FUNCTION THAT SENDS BOTH |0> TO |y_+> and |1> TO |y_->
def y_basis_rotation():
    qml.Hadamard(wires=0)
    qml.S(wires=0)
