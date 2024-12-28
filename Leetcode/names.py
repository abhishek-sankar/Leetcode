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

        # Check if each file has a listing in readme.md
        readme_path = "../Leetcode/readme.md"
        with open(readme_path, "r") as readme_file:
            readme_content = readme_file.read()

        # Extract the file name without the extension
        file_name_without_ext = py_file.replace(".py", "")

        # Extract the numeric part and the descriptive part of the file name
        if file_name_without_ext not in ["names", "readme"]:
            numeric_part, descriptive_part = file_name_without_ext.split(".", 1)
        else:
            numeric_part, descriptive_part = None, None
        # Format the descriptive part to have spaces and capitalize each word
        formatted_description = (
            "".join(
                [" " + char if char.isupper() else char for char in descriptive_part]
            )
            .strip()
            .title()
        )

        # Create the expected line in the readme
        expected_line = f"- [{numeric_part}. {formatted_description}](../docs/Leetcode/{file_name_without_ext}.md)"

        # If the expected line is not in the readme, append it
        if expected_line not in readme_content:
            with open(readme_path, "a") as readme_file:
                readme_file.write(f"{expected_line}\n")
