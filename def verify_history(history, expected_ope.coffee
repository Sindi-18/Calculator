def verify_history(history, expected_operations):
    """
    Verifies that the history contains the correct number of operations
    and that each operation result is accurate.

    Parameters:
    - history: list of tuples in the form (operation: str, operands: list, result: float)
    - expected_operations: dict with operation names as keys and expected counts as values

    Returns:
    - dict with verification status and any errors found
    """
    from math import isclose

    actual_counts = {}
    errors = []

    for entry in history:
        operation, operands, result = entry
        actual_counts[operation] = actual_counts.get(operation, 0) + 1

        # Recalculate expected result
        try:
            if operation == 'add':
                expected = sum(operands)
            elif operation == 'subtract':
                expected = operands[0] - operands[1]
            elif operation == 'multiply':
                expected = operands[0] * operands[1]
            elif operation == 'divide':
                expected = operands[0] / operands[1]
            elif operation == 'modulus':
                expected = operands[0] % operands[1]
            else:
                errors.append(f"Unknown operation: {operation}")
                continue

            if not isclose(result, expected, rel_tol=1e-9):
                errors.append(f"Incorrect result for {operation} with {operands}: got {result}, expected {expected}")
        except Exception as e:
            errors.append(f"Error verifying {operation} with {operands}: {e}")

    # Compare counts
    for op, expected_count in expected_operations.items():
        actual = actual_counts.get(op, 0)
        if actual != expected_count:
            errors.append(f"Operation count mismatch for {op}: expected {expected_count}, got {actual}")

    return {
        "status": "passed" if not errors else "failed",
        "errors": errors
    }
