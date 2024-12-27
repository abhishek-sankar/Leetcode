# Bash to get all file names
# python3 -c "import os; print(sorted(os.listdir('.'), key=lambda x: int(x.split('.')[0]) if x.split('.')[0].isdigit() else float('inf')))"

# Python to set it to main md
# for f in fil:
#     # - [36.validSudoku.py](36.validSudoku.py)
#     print(f"- [{f}]({f})")

# python3 names.py >> names.md

import os

# Get all .py files in the current directory
py_files = [f for f in os.listdir(".") if f.endswith(".py")]

# Sort files by the numeric part of the filename
sorted_files = sorted(
    py_files,
    key=lambda x: int(x.split(".")[0]) if x.split(".")[0].isdigit() else float("inf"),
)

# Process each file
for py_file in sorted_files:
    # Read the contents of the .py file
    with open(py_file, "r") as f:
        content = f.read()

    # Create the corresponding markdown file path
    md_file_path = f"../docs/Leetcode/{py_file.replace('.py', '.md')}"

    # Write the content to the markdown file with the specified format
    with open(md_file_path, "w") as f:
        f.write("```python\n")
        f.write(content)
        f.write("\n```\n")
