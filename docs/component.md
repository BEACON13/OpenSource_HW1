# Component Definition

In this project, a component refers to a modular unit with specific functionality and responsibilities, which can be independently developed, tested, and deployed, while also being integrated with other components to build a complete application.

## Component Characteristics

1. **Modularity**: Each component is an independent module with clearly defined boundaries.
2. **Single Responsibility**: Each component focuses on completing a specific task.
3. **Testability**: Components are designed to facilitate unit testing, integration testing, and end-to-end testing.
4. **Reusability**: Components can be reused in different contexts.
5. **Interface Definition**: Components interact with other components through clearly defined APIs.

## Project Components

This project contains the following three core components:

### 1. Calculator

**Responsibility**: Perform basic arithmetic operations.

**Functionality**:
- Addition (add)
- Subtraction (subtract)
- Multiplication (multiply)

**API**:
- `add(a, b)`: Returns a + b
- `subtract(a, b)`: Returns a - b
- `multiply(a, b)`: Returns a * b

### 2. Logger

**Responsibility**: Record operations performed by the calculator.

**Functionality**:
- Create log files
- Record calculation operations and their results
- Record error messages

**API**:
- `create_logger(log_file)`: Create a logger instance
- `log_calculation(operation, a, b, result)`: Record a calculation operation
- `log_error(message)`: Record an error message

### 3. Notifier

**Responsibility**: Send notifications when calculation results exceed a specified threshold.

**Functionality**:
- Check if results exceed the threshold
- Send notifications

**API**:
- `create_notifier(threshold)`: Create a notifier instance
- `send_alert(value)`: Check if the value exceeds the threshold and send a notification

## Component Interaction

These three components can work together:

1. Calculator performs calculation operations
2. Logger records calculation operations and results
3. Notifier sends notifications when results exceed the threshold

Interactions between components occur through clearly defined APIs, which allows components to be independently developed and tested, while also being integrated into a complete system.

## Directory Structure

Each component is organized in its own subdirectory within the `src` folder:

```
src/
├── calculator/
│   ├── __init__.py
│   ├── api.py
│   ├── calculator.py
│   ├── pyproject.toml
│   └── tests/
│       ├── __init__.py
│       └── test_calculator.py
├── logger/
│   ├── __init__.py
│   ├── api.py
│   ├── logger.py
│   ├── pyproject.toml
│   └── tests/
│       ├── __init__.py
│       └── test_logger.py
└── notifier/
    ├── __init__.py
    ├── api.py
    ├── notifier.py
    ├── pyproject.toml
    └── tests/
        ├── __init__.py
        └── test_notifier.py
```

Integration tests and end-to-end tests are located in the top-level `tests` directory:

```
tests/
├── integration_tests/
│   ├── __init__.py
│   ├── test_integration_calculator_logger.py
│   └── test_integration_logger_notifier.py
└── end_to_end_tests/
    ├── __init__.py
    └── test_end_to_end.py
```

### Testing Organization

This project follows a structured approach to testing:

1. **Unit Tests**: Located within each component's directory (`src/<component>/tests/`), these tests verify the functionality of individual components in isolation.

2. **Integration Tests**: Located in the top-level `tests/integration_tests/` directory, these tests verify the interactions between components.

3. **End-to-End Tests**: Located in the top-level `tests/end_to_end_tests/` directory, these tests verify complete workflows across the entire system.

This structure ensures that each component is self-contained with its own implementation, API, and unit tests, while integration and end-to-end tests verify the interactions between components. 