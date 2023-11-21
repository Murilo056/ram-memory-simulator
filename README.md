# RAM Memory Simulator

This project is a simple RAM Memory Simulator implemented in Python. It allows the manipulation of data at different memory addresses, simulating basic storage (ST) and read (LD) operations.

## Features

- **Storage (ST): Stores data at a specific memory address.
- **Read (LD): Loads data from a specific memory address.

## Setup

1. **Clone the Repository::**
   ```bash
   git clone https://github.com/Murilo056/ram-memory-simulator.git
   cd ram-memory-simulator

2. **Follow the Instructions::

  Enter the number of memory addresses.
  Enter the size of the memory cell in bits.

2.1 **Supported Commands::

  ST <address> <data>: Stores data at the specified address.
  LD <address>: Loads data from the specified address.

3. ** Usage Example:
  Enter a command (ST <address> <data> or LD <address>): ST 0001 42
  Storing 42 at address 1

  Enter a command (ST <address> <data> or LD <address>): LD 0001
  Reading 42 from address 1


4. **End the Simulator:
   Type "stop" to end the simulator.
