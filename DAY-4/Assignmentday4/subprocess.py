import subprocess


def run_shell_command(command_args):
  """Executes a system command safely and returns its stdout.

  Raises a CalledProcessError if the command fails.
  """
  try:
    # Pass command as a list of strings and set check=True to catch errors
    result = subprocess.run(
        command_args, capture_output=True, text=True, check=True
    )
    return result.stdout.strip()
  except subprocess.CalledProcessError as e:
    print(f"Command failed with exit code {e.returncode}")
    print(f"Error output: {e.stderr.strip()}")
    return None


# Program execution (passing arguments as a list)
output = run_shell_command(["echo", "Hello from the system shell"])

if output is not None:
  print("Command Output:", output)