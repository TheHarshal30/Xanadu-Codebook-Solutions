# An array to store your results
shot_results = []

# Different numbers of shots
shot_values = [100, 1000, 10000, 100000, 1000000]

for shots in shot_values: 
    ##################
    # YOUR CODE HERE #
    ##################
    
    # CREATE A DEVICE, CREATE A QNODE, AND RUN IT
    dev = qml.device('default.qubit', wires=1)

    @qml.qnode(dev)
    def circuit():
        qml.RX(np.pi/4,wires=0)
        qml.Hadamard(wires=0)
        qml.PauliZ(wires=0)
        
        return qml.expval(qml.PauliY(wires=0))

    # STORE RESULT IN SHOT_RESULTS ARRAY
    shot_results.append(circuit())
    
    

print(qml.math.unwrap(shot_results))
