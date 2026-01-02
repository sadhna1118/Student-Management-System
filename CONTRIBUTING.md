# Contributing to Student Management System

First off, thank you for considering contributing to the Student Management System! It's people like you that make this project better for everyone.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Coding Guidelines](#coding-guidelines)
- [Commit Messages](#commit-messages)
- [Pull Request Process](#pull-request-process)
- [Reporting Bugs](#reporting-bugs)
- [Suggesting Enhancements](#suggesting-enhancements)

## Code of Conduct

This project and everyone participating in it is governed by our [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the existing issues to avoid duplicates. When you create a bug report, include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps to reproduce the problem**
- **Provide specific examples**
- **Describe the behavior you observed and what you expected**
- **Include screenshots if applicable**
- **Include your environment details** (OS, Python version, etc.)

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion:

- **Use a clear and descriptive title**
- **Provide a detailed description of the suggested enhancement**
- **Explain why this enhancement would be useful**
- **List any similar features in other applications**

### Your First Code Contribution

Unsure where to begin? Look for issues labeled:

- `good first issue` - Simple issues for beginners
- `help wanted` - Issues that need assistance
- `documentation` - Documentation improvements

## Development Setup

1. **Fork the repository** and clone your fork:
   ```bash
   git clone https://github.com/your-username/Student-Management-System.git
   cd "Student Management System"
   ```

2. **Add the upstream repository**:
   ```bash
   git remote add upstream https://github.com/original-owner/Student-Management-System.git
   ```

3. **Create a virtual environment**:
   ```bash
   python -m venv venv
   # Windows
   .\venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate
   ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up the database**:
   ```bash
   python scripts/init_db.py
   ```

6. **Create a new branch** for your feature:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## Coding Guidelines

### Python Style Guide

We follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guidelines:

- Use 4 spaces for indentation (not tabs)
- Maximum line length of 100 characters
- Use descriptive variable names
- Add docstrings to all functions and classes
- Keep functions small and focused

### Code Formatting

We use **Black** for code formatting:

```bash
# Format all Python files
black app/ tests/ scripts/
```

### Linting

We use **flake8** for linting:

```bash
# Run linter
flake8 app/ tests/ scripts/
```

### Type Hints

Use type hints where appropriate to improve code readability:

```python
def create_student(name: str, age: int) -> Student:
    """Create a new student."""
    pass
```

### Testing

All new features and bug fixes must include tests:

```bash
# Run tests
pytest

# Run tests with coverage
pytest --cov=app tests/
```

Test coverage should not decrease. Aim for at least 80% coverage.

### Documentation

- Update the README.md if you change functionality
- Update API_DOCUMENTATION.md for API changes
- Add docstrings to new functions and classes
- Update CHANGELOG.md following [Keep a Changelog](https://keepachangelog.com/) format

## Commit Messages

Write clear and meaningful commit messages:

### Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

### Examples

```
feat(auth): add password reset functionality

Implement password reset via email with secure tokens.
Tokens expire after 1 hour.

Closes #123
```

```
fix(students): correct student ID generation

Fixed issue where student IDs were not unique when
created in rapid succession.

Fixes #456
```

## Pull Request Process

1. **Update Documentation**: Ensure all relevant documentation is updated
2. **Add Tests**: Include tests for new features
3. **Run Tests**: Ensure all tests pass
4. **Format Code**: Run Black and flake8
5. **Update CHANGELOG**: Add your changes to CHANGELOG.md
6. **Create Pull Request**:
   - Use a clear title and description
   - Reference any related issues
   - Include screenshots for UI changes
   - List any breaking changes

### Pull Request Template

When creating a PR, include:

- **Description**: What does this PR do?
- **Motivation**: Why is this change needed?
- **Testing**: How was this tested?
- **Screenshots**: If applicable
- **Breaking Changes**: Any breaking changes?
- **Checklist**:
  - [ ] Code follows style guidelines
  - [ ] Tests added/updated
  - [ ] Documentation updated
  - [ ] CHANGELOG updated
  - [ ] All tests pass

### Review Process

- At least one maintainer must approve the PR
- All CI checks must pass
- Code must meet quality standards
- Documentation must be complete

## Project Structure

Understanding the project structure will help you contribute:

```
app/
├── config/          # Configuration files
├── models/          # Database models
├── repositories/    # Data access layer
├── services/        # Business logic layer
├── routes/          # API endpoints
└── utils/           # Utility functions

scripts/             # Database and setup scripts
tests/               # Test suite
frontend/            # Frontend files (HTML/CSS/JS)
```

### Design Patterns

We use the following patterns:

- **Repository Pattern**: For data access
- **Service Layer**: For business logic
- **Dependency Injection**: For testability
- **Factory Pattern**: For app creation

## Questions?

Feel free to:

- Open an issue for questions
- Join our community discussions
- Contact the maintainers

## Recognition

Contributors will be recognized in:

- README.md contributors section
- Release notes
- GitHub contributors page

Thank you for contributing! 🎉