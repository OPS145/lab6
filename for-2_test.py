#!/usr/bin/env python3

import subprocess

def for2test():

    # Run the bash script
    result = subprocess.Popen(['bash', 'for-2.bash', '10', '9', '8', '7', '6', '5', '4', '3', '2', '1'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Get the output
    output = result.stdout.read()

    # Check the output
    assert "10" in output
    assert "9" in output
    assert "8" in output
    assert "7" in output
    assert "6" in output
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

for2test()