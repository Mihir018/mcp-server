from mcp.server.fastmcp import FastMCP

mcp = FastMCP("calculator")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers together."""
    return a * b

@mcp.tool()
def divide(numerator: float, denominator: float) -> str:
    """Divide two numbers.
    
    Args:
        numerator: The dividend
        denominator: The divisor
    
    Returns:
        The quotient or an error message
    """
    try:
        if denominator == 0:
            return "Error: Cannot divide by zero"
        result = numerator / denominator
        return f"Result: {result}"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    mcp.run()