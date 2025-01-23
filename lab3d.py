#!/usr/bin/env python3

# Author ID: rchin11

import subprocess

def free_space():
    try:
        # Execute the command as a new process
        result = subprocess.check_output(
            "df -h | grep '/$' | awk '{print $4}'",
            shell=True,
            text=True
        )
        # Return the result as a stripped UTF-8 string
        return result.strip()
    except subprocess.CalledProcessError as e:
        return f"Error: {e}"

# Example usage
if __name__ == "__main__":
    print(free_space())
