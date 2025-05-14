"""
Function Extraction Laboratory

This script demonstrates how to extract functions from source code.
It identifies function definitions, extracts them with their comments,
and maintains proper indentation.
"""

import os
import sys
from pathlib import Path
import re
from typing import List, Dict, Optional, Tuple
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from dotenv import load_dotenv
from wca_backend import call_wca_api, stream_response

# Load environment variables
load_dotenv()

console = Console()

def extract_code_blocks(markdown: str) -> Dict[str, List[Tuple[str, str]]]:
    """
    Extract code blocks and their file names from markdown content.
    
    Args:
        markdown (str): Markdown content with code blocks
        
    Returns:
        Dict[str, List[Tuple[str, str]]]: Dictionary of language -> list of (filename, code) tuples
    """
    # Pattern to match filename and code blocks with language specification
    pattern = r'File: ([^\n]+)\n```(\w+)\n(.*?)```'
    blocks = {}
    
    # Find all code blocks
    matches = re.finditer(pattern, markdown, re.DOTALL)
    for match in matches:
        filename = match.group(1).strip()
        language = match.group(2)
        code = match.group(3).strip()
        
        # Group blocks by language
        if language not in blocks:
            blocks[language] = []
        blocks[language].append((filename, code))
    
    return blocks

def display_analysis(analysis: Dict) -> None:
    """
    Display function analysis results in a formatted table.
    
    Args:
        analysis (Dict): Analysis results
    """
    table = Table(title="Function Analysis Results")
    table.add_column("Metric", style="cyan")
    table.add_column("Value", style="green")
    
    table.add_row("Total Functions", str(analysis["total_functions"]))
    table.add_row("Average Length", f"{analysis['avg_length']:.1f} lines")
    table.add_row("Max Length", f"{analysis['max_length']} lines")
    table.add_row("Min Length", f"{analysis['min_length']} lines")
    table.add_row("With Comments", f"{analysis['with_comments']} functions")
    
    console.print(table)

def generate_code_examples() -> str:
    """
    Generate code examples using WCA API.
    
    Returns:
        str: Markdown content with code examples
    """
    prompt = """Please provide multiple examples of Java code that demonstrate different programming concepts. 
    Include examples of:
    1. Singapore Holiday Calendar
    2. Prime number generation
    
    For each example:
    1. First specify the file name that would be appropriate for the code (e.g., 'File: BinaryTree.java')
    2. Then provide the code in a markdown code block with language specification
    3. Ensure the file name follows proper naming conventions for the language
    
    Format each example as:
    File: ExampleName.java
    ```java
    // code here
    ```
    
    Return only the code examples in this format."""
    
    response = call_wca_api(prompt)
    if hasattr(response, 'iter_lines'):
        markdown = stream_response(response, action="Generating code examples")
    else:
        markdown = response
        
    return markdown

def main():
    """Main function to demonstrate function extraction."""
    console.print(Panel.fit("Function Extraction Laboratory", title="Welcome"))
    
    # Generate code examples
    console.print("\n[bold]Generating code examples using WCA API...[/bold]")
    markdown = generate_code_examples()
    
    # Extract code blocks by language
    console.print("\n[bold]Extracting code blocks from markdown...[/bold]")
    code_blocks = extract_code_blocks(markdown)
    
    # Process each language's code blocks
    for language, blocks in code_blocks.items():
        console.print(f"\n[bold cyan]Found {len(blocks)} {language} code blocks:[/bold cyan]")
        
        # Create language-specific output directory
        output_dir = Path(f"output/{language}/extract")
        output_dir.mkdir(parents=True, exist_ok=True)
        
        # Save original markdown
        with open(output_dir / "examples.md", "w") as f:
            f.write(markdown)
        
        # Process each code block
        for i, (filename, code) in enumerate(blocks, 1):
            # Print code block with border and filename
            console.print(f"\n[bold yellow]Code Block {i} - File: {filename}[/bold yellow]")
            console.print("[bold blue]" + "="*60 + "[/bold blue]")
            console.print(code)
            console.print("[bold blue]" + "="*60 + "[/bold blue]")
            
            # Save code block using the provided filename
            block_dir = output_dir / f"block_{i}"
            block_dir.mkdir(exist_ok=True)
            
            # Save original code block with its intended filename
            with open(block_dir / filename, "w") as f:
                f.write(code)
    
    console.print(f"\n[green]Results saved to the 'output/extract' directory[/green]")

if __name__ == "__main__":
    main() 