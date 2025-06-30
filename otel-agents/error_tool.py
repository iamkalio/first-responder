# this is only for test purpose, going further it should read from your database or S3 bucket, or anywhere you store you files 
import json
from typing import Dict, List, Optional

def read_and_check_for_error(file_path: str) -> Optional[Dict[str, Dict[str, str]]]:
    """
    Reads a file, checks for the first line containing "ERROR", and returns the error
    along with 10 lines of context before and after the error line.

    Args:
        file_path (str): The absolute path to the file to be checked.

    Returns:
        Optional[Dict[str, Dict[str, str]]]: A dictionary containing the error and its context,
        or None if no error is found. The dictionary format is:
        {"this is the error from the otel file: <error_line>": {
            "before": "<10 lines before error>",
            "after": "<10 lines after error>"
            }
        }
    """
    try:
        with open(file_path, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        return {"error": {"message": f"File not found at {file_path}"}}
    except Exception as e:
        return {"error": {"message": str(e)}}

    for i, line in enumerate(lines):
        if "ERROR" in line:
            error_line = line.strip()
            start = max(0, i - 10)
            end = min(len(lines), i + 11)
            
            before_lines = "".join(lines[start:i])
            after_lines = "".join(lines[i+1:end])

            error_context = {
                "this is the error from the otel file: " + error_line: {
                    "before": before_lines,
                    "after": after_lines
                }
            }
            return error_context
    return None