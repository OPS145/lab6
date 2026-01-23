#!/usr/bin/env python3

import subprocess

def for1test():

    # Run the bash script
    result = subprocess.Popen(['bash', 'for-1.bash'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Get the output
    output = result.stdout.read()

    # Check the output
    assert "5" in output
    assert "4" in output
    assert "3" in output
    assert "2" in output
    assert "1" in output
    assert "blast-off!" in output

    # Close the process
    result.stdin.close()
    result.stdout.close()
    result.stderr.close()

for1test()