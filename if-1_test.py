#!/usr/bin/env python3

import subprocess

def if1test():

    # Run the bash script
    result = subprocess.Popen(['bash', 'if-1.bash'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Get the output
    output = result.stdout.read()

    # Check the output
    assert "num1 is less than num2" in output

    # Close the process
    result.stdin.close()
    result.stdout.close()
    result.stderr.close()

if1test()