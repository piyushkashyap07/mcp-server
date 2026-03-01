from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Demo", json_response=True)

@mcp.tool()
def add(numbers: list[float]) -> float:
    """Add any number of values"""
    return sum(numbers)


@mcp.tool()
def subtract(numbers: list[float]) -> float:
    """Subtract a sequence of numbers from the first number"""
    if not numbers:
        return 0.0
    return numbers[0] - sum(numbers[1:])


@mcp.tool()
def multiply(numbers: list[float]) -> float:
    """Multiply any number of values"""
    from functools import reduce
    import operator
    if not numbers:
        return 1.0
    return float(reduce(operator.mul, numbers, 1.0))


@mcp.tool()
def divide(numbers: list[float]) -> float:
    """Divide a sequence of numbers sequentially from the first number"""
    if not numbers:
        raise ValueError("No numbers provided")
    if len(numbers) == 1:
        return numbers[0]
    result = numbers[0]
    for num in numbers[1:]:
        if num == 0:
            raise ValueError("Division by zero")
        result /= num
    return result


# Run with streamable HTTP transport
if __name__ == "__main__":
    mcp.run(transport="streamable-http")