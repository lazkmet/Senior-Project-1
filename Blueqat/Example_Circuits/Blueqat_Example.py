from blueqat import Circuit

#Create a quantum circuit using 2 qubits
circuit = Circuit(2)

#Apply gates in the following order:
#Hadamard gate to qubit 0
#NOT gate to qubit 1
#Hadamard gate to qubit 1
#Conditional-NOT gate to qubit 1, with qubit 0 as the control
#Hadamard gate to qubit 1
#Measure the value of both qubits
circuit.h[0].x[1].h[1].cx[0, 1].h[1].m[:]

#Simulate this circuit 1000 times and print the results
print(circuit.run(shots=1000))

#Display a drawing of the circuit
circuit.run(backend="draw")