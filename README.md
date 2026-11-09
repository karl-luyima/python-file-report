# Python File Report

## Project Description
This project is a Python command-line application that scans a specified directory and generates a report containing information about files.

The script uses Python's `os` and `argparse` modules to traverse directories, retrieve file information, and allow users to customize their reports through command-line arguments.

## Features
- Accepts a directory path as a command-line argument.
- Traverses directories and their subdirectories.
- Retrieves file paths and file sizes.
- Limits reports to a maximum number of files (20 by default).
- Filters files based on a specified minimum size in megabytes.
- Sorts files by size, from largest to smallest.
- Supports combining multiple reporting options.

## Technologies Used
- Python 3
- os module
- argparse module

## How to Run

1. Clone the repository:

   ```bash
   git clone YOUR_GITHUB_REPOSITORY_URL
   ```

2. Navigate into the project directory:

   ```bash
   cd python-file-report
   ```

3. Run the script and provide a directory path:

   ```bash
   python file_report.py "C:\Users\YourName\Desktop"
   ```

## Command-Line Options

| Option | Description |
|---|---|
| `--limit 10` | Displays a maximum of 10 files. |
| `--min-size-mb 5` | Displays files larger than 5 MB. |

Both options can be combined:

```bash
python file_report.py "C:\Users\YourName\Desktop" --limit 10 --min-size-mb 5
```

## Project Structure

```text
python-file-report/
├── README.md
└── file_report.py
```

## What I Learned
Through this project, I practised:
- Python scripting and command-line arguments.
- Directory traversal using `os.walk()`.
- Retrieving file paths and sizes.
- Filtering and sorting data.
- Handling file access errors.
- Using GitHub to manage and document a Python project.

## Author
Created as part of my Python and data engineering learning journey.