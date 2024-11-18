# Knitting Machine Simulation Tool

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-yellow)

## Overview
This project is a simulation tool designed for the textile industry to automate product selection for knitting machines. It ensures efficient production by eliminating manual calculations and providing optimized recommendations for the next tasks. The tool reduces machine downtime and enhances productivity.


---

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Table-of-Contents](#table-of-contents)
- [Requirements](#requirements)
- [File Descriptions](#file-descriptions)
- [Setup and Execution](#setup-and-execution)
  - [Installation](#installation)
  - [Quick Start](#quick-start)
- [Customization](#customization)
  - [Adjusting Threshold](#adjusting-threshold)
  - [Redefining Hardness of Tasks](#redefining-hardness-of-tasks)
- [License](#license)
- [Contributing](#contributing)
- [Contact](#contact)

---

## Features
- **Order Analysis**: Categorizes tasks into primary and non-primary types to streamline machine operations.
- **Machine Load Balancing**: Ensures balanced workloads by analyzing current machine usage.
- **Threshold Conditions**: Prevents frequent product changes by enforcing minimum operation times.
- **Grouping and Averages**: Groups tasks by product type and calculates average times for better scheduling insights.


---

### Requirements
- Python 3.8+
- Libraries: `pandas`, `openpyxl

## File Descriptions 
- **`simulate.py`**: Core logic for determining the next products to be processed and analyzing workloads.
- **`SimulationFunctions.py`**: Contains helper functions for analyzing orders and machine workloads, including threshold checks and task categorization.
- **`main.py`**: Entry point script that loads data, executes simulations, and displays results.

---

## Setup and Execution

### Requirements
- Python 3.8+
- Libraries:
  - `pandas`
  - `openpyxl`

---

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Ahmet-Yesevi/KnitSimLab
   cd knitting-machine-simulation
2. Install dependencies:
    ```bash
    pip install -r requirements.txt

---

## Quick Start
1. Prepare your data files:

Order List: An Excel file  **`simulation.xlsx`** containing the product specifications such as order ID, part type, size, and color.
Machine List: An Excel file **`machines.xlsx`** with details about the current state of each machine.

2. Update file paths in main.py to point to your data files.
3. Run the tool:
    ```bash
    python main.py
4. The output will include:
- Recommendations for the next tasks.
- Workload distribution across machines.

---

## Customization
### Adjusting Threshold

- Modify the Threshold variable in SimulationFunctions.py to set the minimum operation time before switching tasks:
    ```python
    Threshold = 8 * 60  # Default: 8 hours in minutes
## Redefining Hardness of Tasks:
- Update the Primary and NonPrimary lists in SimulationFunctions.py to adjust task hardness:
    ```python
    Primary = ["Front", "Back", "Sleeve"] # Easily Started by operators/workers
    NonPrimary = ["Collar", "Hood", "Band"] # Cannot be started by operators easily need an expertise
---
## License
This project is licensed under the MIT License. See the LICENSE file for details.
---

## Contributing
Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
3. Commit your changes and submit a pull request.

---
## Contact
For questions or suggestions, feel free to contact:

- Name: Ahmet Yesevi Nurcan
- Email: yesevinurcan@gmail.com
- GitHub: Ahmet-Yesevi



 
