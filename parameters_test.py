#!/usr/bin/env python3

import subprocess

def test_parameters():

    # Run the bash script
    result = subprocess.Popen(['bash', 'parameters.bash', '1', '2', '3', '4', '5', '6', '7', '8'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Get the output
    output = result.stdout.read()

    # Check the output
    assert "$2: 2" in output
    assert "$3: 3" in output
    assert "$#: 8" in output
    assert "$*: 1 2 3 4 5 6 7 8" in output
    assert "$#: 6" in output
    assert "$*: 3 4 5 6 7 8" in output


    # Close the process
    result.stdin.close()
    result.stdout.close()
    result.stderr.close()

test_parameters()