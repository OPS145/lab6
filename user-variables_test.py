#!/usr/bin/env python3

import subprocess

def test_user_variables():
    
    # Run the bash script
    result = subprocess.Popen(['bash', 'user-variables.bash'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Provide the input
    result.stdin.write("Jason\n")
    result.stdin.flush()

    result.stdin.write("43\n")
    result.stdin.flush()

    # Get the output
    output = result.stdout.read()

    # Check the output
    assert "Hello" or "hello" in output
    assert "Jason" in output
    assert "43" in output

    # Close the process
    result.stdin.close()
    result.stdout.close()
    result.stderr.close()

test_user_variables()