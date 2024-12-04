# TarjanPlanner

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python Version](https://img.shields.io/badge/python-3.9%2B-blue.svg)
![Pytest](https://img.shields.io/badge/pytest-8.3.4-brightgreen.svg)

TarjanPlanner is a Python-based application designed to optimize multi-destination routes for an individual named Tarjan, seeking to visit all his relatives efficiently. By leveraging various transportation modes—bus, train, bicycle, and walking—the program calculates the most optimal path based on user-selected criteria: minimizing time, minimizing cost, or balancing both.

## Table of Contents

- [Features](#features)
- [Demo](#demo)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Features

- **Multi-Modal Transportation**: Supports bus, train, bicycle, and walking modes, each with customizable speed, cost, and transfer times.
- **Flexible Optimization Criteria**: Users can choose to optimize for time, cost, or a balanced combination of both.
- **Graphical Visualization**: Generates visual maps of the computed routes for better understanding and planning.
- **Performance Logging**: Measures and logs execution times of key functions to aid in performance analysis.
- **Comprehensive Testing**: Includes unit tests using pytest to ensure the correctness and reliability of the program.

## Installation

Follow these steps to set up TarjanPlanner on your local machine.

### Prerequisites

- **Python 3.9 or higher**: Ensure Python is installed on your system. Download it from [Python's official website](https://www.python.org/downloads/).

### Clone the Repository

```bash
git clone https://github.com/andersblberg/Final_Assignment_Problemsolvingwscripting.git
cd TarjanPlanner
```

### Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
```

Activate the virtual environment:

- **Windows:**

  ```bash
  venv\Scripts\activate
  ```

- **macOS/Linux:**

  ```bash
  source venv/bin/activate
  ```

### Install Dependencies

Install the required Python packages using `pip`:

```bash
pip install -r requirements.txt
```

## Usage

TarjanPlanner is a command-line application that guides Tarjan, a korean man, through optimizing your route to visit all your relatives. Follow the steps below to use the program.

### Running the Program

Navigate to the project directory and execute the `main.py` script:

```bash
python main.py
```

### User Input

Upon running the program, you will be prompted to select your optimization criteria:

```
Optimize by (time/cost/both):
```

Enter your choice:

- **time**: Optimize the route to minimize total travel time.
- **cost**: Optimize the route to minimize total travel cost.
- **both**: Optimize the route to balance between time and cost.

### Example Interaction

```
Optimize by (time/cost/both): both

Optimal route details:
Tarjan's Home -> Relative_5: Distance = 5.80 km, Mode = Bus, Time = 15.83 minutes, Cost = ₩63.29
... (other route details) ...

Total distance: 57.63 km
Total time: 147.33 minutes
Total cost: ₩583.27

Total execution time: 1.1602 seconds.
```

### Visualization

After computing the optimal route, the program will display a graphical representation of the route on a map. This visualization helps in understanding the path and the modes of transportation used for each segment.

## Project Structure

The project is organized into several modules, each responsible for a specific aspect of the application's functionality.

```
TarjanPlanner/

├── main.py          
├── planner/
│   ├── __init__.py  
│   ├── data.py     
│   ├── optimizer.py 
│   ├── graph.py
│   ├── visualizer.py
│   ├── timer.py   
├── requirements.txt
├── README.md
├── execution_time.log
└── tests/
    ├── __init__.py
    └── test_planner.py 
```

- **`main.py`**: The entry point of the program. It orchestrates the execution flow by calling functions from other modules, handles user input, and initiates the visualization of results.
- **`data.py`**: Contains the data structures representing the relatives' information, including their names and geographical coordinates.
- **`graph.py`**: Responsible for constructing the graph representation of the problem using the NetworkX library. It defines the nodes and edges based on the relatives' locations.
- **`optimizer.py`**: Implements the core optimization algorithms. It calculates edge weights based on transportation modes and finds the optimal route according to the selected criteria.
- **`visualizer.py`**: Handles the graphical representation of the route using Matplotlib, providing a visual aid to understand the computed path.
- **`timer.py`**: Provides a decorator function to measure and log the execution time of functions, aiding in performance analysis.
- **`test_planner.py`**: Contains unit tests written with pytest to verify the correctness of the modules and functions.
- **`requirements.txt`**: Lists all the Python dependencies required to run the project.
- **`execution_time.log`**: Logs the execution times of key functions for performance analysis.

## Testing

Ensuring the correctness and reliability of the program is paramount. TarjanPlanner includes a comprehensive suite of unit tests using the pytest framework.

### Running Tests

To execute the test suite, run the following command in the project directory:

```bash
pytest test_planner.py
```

### Test Coverage

To assess the extent of code covered by the tests, use the `coverage` package:

1. **Install Coverage** (if not already installed):

   ```bash
   pip install coverage
   ```

2. **Run Tests with Coverage**:

   ```bash
   coverage run -m pytest test_planner.py
   coverage report -m
   ```

### Sample Test Results

```
============================================= test session starts =============================================
platform win32 -- Python 3.9.13, pytest-8.3.4, pluggy-1.5.0
collected 8 items

test_planner.py ........                                                                                 [100%]

============================================== 8 passed in 0.60s ===============================================
```


## Contributing

Contributions are welcome! To contribute to TarjanPlanner, follow these steps:

1. **Fork the Repository**: Click the "Fork" button at the top-right corner of the repository page.
2. **Clone Your Fork**:

    ```bash
    git clone https://github.com/yourusername/TarjanPlanner.git
    cd TarjanPlanner
    ```

3. **Create a New Branch**:

    ```bash
    git checkout -b feature/YourFeatureName
    ```

4. **Make Changes**: Implement your feature or fix bugs.
5. **Commit Your Changes**:

    ```bash
    git commit -m "Add feature: YourFeatureName"
    ```

6. **Push to Your Fork**:

    ```bash
    git push origin feature/YourFeatureName
    ```

7. **Open a Pull Request**: Navigate to the original repository and create a pull request detailing your changes.

### Guidelines

- Follow the existing code style and conventions.
- Write clear and concise commit messages.
- Ensure that all tests pass before submitting a pull request.
- Include documentation for new features or changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
