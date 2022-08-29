dev = qml.device("default.qubit", wires=1)

@qml.qnode(dev)
def convert_to_rz_rx():
    ##################
    # YOUR CODE HERE #
    ##################

    # IMPLEMENT THE CIRCUIT IN THE PICTURE USING ONLY RZ AND RX
    qml.RZ(np.pi/2, wires=0)
    qml.RX(np.pi/2, wires=0)
    qml.RZ(np.pi/2, wires=0)
    qml.RZ(np.pi/2,wires=0)
    qml.RZ(-np.pi/4, wires=0)
    qml.RX(np.pi, wires=0)
    qml.RZ(np.pi,wires=0)


    return qml.state()
