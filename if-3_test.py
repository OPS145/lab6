#!/usr/bin/env python3

import subprocess

def if3testlt():

    # Run the bash script
    result = subprocess.Popen(['bash', 'if-3.bash'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Provide the input
    result.stdin.write('2\n')
    result.stdin.write('3\n')
    result.stdin.flush()

    # Get the output
    output = result.stdout.read()

    # Check the output
    assert "first number" in output
    assert "second number" in output

    # Close the process
    result.stdin.close()
    result.stdout.close()
    result.stderr.close()


if3testlt()