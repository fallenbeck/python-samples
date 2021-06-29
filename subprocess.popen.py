#!/usr/bin/env python3

# Commands to be executed
cmds = [ "id", "sudo -k", "sudo id" ]

import subprocess

for cmd in cmds:
    print(f"[{cmd}] Starting execution")

    proc = subprocess.Popen(
            cmd,
            shell = True,
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE,
            stdin = subprocess.PIPE,
            )

    try:
        pid = proc.pid
        print(f"[{cmd}] Process ID: {pid}")

        #print(f"[{cmd}] stdout: {proc.stdout.read().decode()}")
        #print(f"[{cmd}] stderr: {proc.stderr.read().decode()}")

        stdout, stderr = proc.communicate()
    except subprocess.TimeoutExpired:
        proc.kill()
        stdout, stderr = proc.communicate()

    print(f"[{cmd}] stdout: {stdout.decode()}")
    print(f"[{cmd}] stderr: {stderr.decode()}")

    proc.wait()

    returncode = proc.returncode
    print(f"[{cmd}] Return code: {returncode}")

print("Finished.")
