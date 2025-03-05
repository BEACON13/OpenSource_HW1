# Python Project Template

A comprehensive Python project template with component-based architecture, testing frameworks, and CI/CD integration.

## Overview

This repository serves as a Python project template, providing a structured foundation for developing Python applications. It includes:

- **Component-based Architecture**: Modular design with Calculator, Logger, and Notifier components
- **Continuous Integration & Testing**: Automated tests with CircleCI
- **Static Analysis & Code Formatting**: Uses Ruff and Mypy
- **Comprehensive Testing Framework**: Includes unit, integration, and end-to-end tests
- **Dependency Management**: Uses UV for modern Python package management

## Project Structure

```
src/
  calculator/           # Calculator component
  logger/              # Logger component
  notifier/           # Notifier component
tests/
  integration_tests/  # Integration tests
  end_to_end_tests/  # End-to-end tests
docs/                # Documentation
```

## Installation

This project uses [uv](https://github.com/astral-sh/uv) for dependency management.

1. Install uv:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. Create a new virtual environment and install dependencies:
```bash
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv pip install -e .
```

## Usage

### Calculator

```python
from src.calculator import add, subtract, multiply

result = add(5, 3)  # Returns 8
```

### Logger

```python
from src.logger import create_logger, log_message

logger = create_logger("myapp.log")
log_message("Hello, World!", logger)
```

### Notifier

```python
from src.notifier import notify

notify("Important message!")
```

## Testing

### Running Tests

Run all tests:
```bash
pytest
```

Run component unit tests:
```bash
# Run calculator unit tests
pytest src/calculator/tests/

# Run logger unit tests
pytest src/logger/tests/

# Run notifier unit tests
pytest src/notifier/tests/
```

Run a specific test file:
```bash
# Run a specific unit test file
pytest src/calculator/tests/test_calculator.py

# Run a specific integration test file
pytest tests/integration_tests/test_integration_calculator_logger.py

# Run a specific end-to-end test file
pytest tests/end_to_end_tests/test_end_to_end.py
```

Run tests by type:
```bash
# Run all integration tests
pytest tests/integration_tests/

# Run all end-to-end tests
pytest tests/end_to_end_tests/
```

### Test Organization

This project follows a structured approach to testing:

1. **Unit Tests**: Located within each component's directory (`src/<component>/tests/`), these tests verify the functionality of individual components in isolation.

2. **Integration Tests**: Located in the top-level `tests/integration_tests/` directory, these tests verify the interactions between components.

3. **End-to-End Tests**: Located in the top-level `tests/end_to_end_tests/` directory, these tests verify complete workflows across the entire system.

## Development

1. Clone the repository
2. Create a virtual environment with uv
3. Install development dependencies
4. Run tests to ensure everything is working

## Static Analysis

Run Ruff for linting:
```bash
ruff check .
```

Run Mypy for type checking:
```bash
mypy src/
```

## CI/CD

This project uses CircleCI for continuous integration and deployment. The CI pipeline:

1. Runs static analysis (Ruff & Mypy)
2. Executes unit tests
3. Executes integration tests
4. Executes end-to-end tests
5. Generates code coverage reports

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests
5. Submit a pull request

## License

This project is licensed under the Apache License 2.0 - see the LICENSE file for details.

## Documentation

For more detailed information about the components, see [components.md](docs/components.md).

