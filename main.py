import typer
from rich import print
from rich.console import Console
from rich.table import Table
import utils.operators as operators  # <- clearer alias

app = typer.Typer()
console = Console()
@app.command()
def version():
    print("xyrculator version [bold red]pre:[green]0.1")
#multiplication sub command
@app.command()
def multiply(a: int, b: int):
    table = Table("operation", "answer")
    table.add_row(f"{str(a)} × {str(b)}", str(operators.multiply(a,b)))
    console.print(table)

#division sub command
@app.command()
def divide(a: int, b:int):
    table = Table("operation", "answer")
    table.add_row(f"{str(a)}÷{str(b)}", str(operators.divide(a,b)))
    console.print(table)

#
@app.command()
def to_numbers(value: str):
    """
    Tried to use operators.to_numbers if available; otherwise attempt a best-effort parse.
    Prints a table of parsed numeric values.
    """
    nums = None
    if hasattr(operators, "to_numbers"):
        try:
            nums = operators.to_numbers(value)
        except Exception as e:
            nums = None
    if nums is None:
        # best-effort parsing: split on commas or whitespace
        parts = [p for p in (v.strip() for v in value.replace(",", " ").split()) if p]
        parsed = []
        for p in parts:
            try:
                if "." in p:
                    parsed.append(float(p))
                else:
                    parsed.append(int(p))
            except Exception:
                # couldn't parse, keep raw
                parsed.append(p)
        nums = parsed

    table = Table("input", "parsed")
    table.add_row(value, str(nums))
    console.print(table)

@app.command()
def add(a: float, b: float):
    """Add two numbers using operators.add if present, otherwise fallback to local add."""
    if hasattr(operators, "add"):
        result = operators.add(a, b)
    else:
        result = a + b
    table = Table("operation", "answer")
    table.add_row(f"{a} + {b}", str(result))
    console.print(table)

@app.command()
def subtract(a: float, b: float):
    """Subtract two numbers using operators.subtract if present, otherwise fallback."""
    if hasattr(operators, "subtract"):
        result = operators.subtract(a, b)
    else:
        result = a - b
    table = Table("operation", "answer")
    table.add_row(f"{a} - {b}", str(result))
    console.print(table)

@app.command()
def call(op_name: str, args: str = typer.Argument("", help="space/comma separated args")):
    """
    Call any function from utils.operators by name.
    Example: call add "1 2"  or call multiply "3,4"
    """
    if not hasattr(operators, op_name):
        print(f"[red]operators has no function named[/red] [bold]{op_name}[/bold]")
        raise typer.Exit(code=1)

    # parse args
    parts = [p for p in (v for v in args.replace(",", " ").split()) if p]
    parsed = []
    for p in parts:
        try:
            parsed.append(int(p) if p.isdigit() else float(p))
        except Exception:
            parsed.append(p)

    func = getattr(operators, op_name)
    try:
        result = func(*parsed)
    except TypeError:
        # try passing the whole string if signature differs
        result = func(args)

    table = Table("operation", "answer")
    table.add_row(f"{op_name}({', '.join(map(str, parsed))})", str(result))
    console.print(table)

if __name__ == "__main__":
    app()
