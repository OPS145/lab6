#!/usr/bin/env python3

import subprocess

def test_parameters():

    # Run the bash script
    result = subprocess.Popen(['bash', 'dog-years.bash'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Provide the input
    result.stdin.write("7\n")
    result.stdin.flush()

    # Get the output
    output = result.stdout.read()

    # Check the output
    assert "Your age in dog-years is: 49" in output

    # Close the process
    result.stdin.close()
    result.stdout.close()
    result.stderr.close()

test_parameters()