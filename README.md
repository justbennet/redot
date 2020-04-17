# ARC-TS redot script

This repository is for a python script to back up the configuration files in a users
home directory that might become corrupted and replace them with copies from the
skeleton directories that are used to create new accounts.

The general plan is to create a dated backup directory, move the existing files or
directories there, then copy or create the system standard versions.  The one
exception to this is the ssh key pair, if it exists, but the `authorized_keys` file
would be put back to initial state.
