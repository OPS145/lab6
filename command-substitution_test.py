#!/usr/bin/env python3

import subprocess

def test_command_substitution():

    # Run the bash script
    result = subprocess.Popen(['bash', 'command-substitution.bash'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Get the output
    output = result.stdout.read()

    # Check the output
    assert "MY ACCOUNT INFORMATION" in output
    assert "Username:" in output
    assert "Current Directory:" in output
    
    # Close the process
    result.stdin.close()
    result.stdout.close()
    result.stderr.close()

test_command_substitution()
