# ARC-TS redot script

This repository is for a python script to back up the configuration files in a users
home directory that might become corrupted and replace them with copies from the
skeleton directories that are used to create new accounts.

The general plan is to create a dated backup directory, move the existing files or
directories there, then copy or create the system standard versions.  The one
exception to this is the ssh key pair, if it exists, but the `authorized_keys` file
would be put back to initial state.


Summary of redot.py script - 

Overall

	▪	What is the user interaction?
	▪	How will the script handle errors?



Why redot is needed

	▪	Reset needed due to software issues
	▪	User changes their .bashrc file which breaks their home directory
	▪	User accidentally deletes required files (‘dot’ files for instance)



What is needed in script

	▪	Move files and directories during user creation into backup
	▪	Gather files and directories that are created during new user creation and put them in place (?)
	▪	Gives an overview of what it did in english and in bash and puts it into backup directory
	▪	Check to see if ssh keys exist in the .ssh directory and replace after backup
	▪	Reads files from “files” file and checks if they exist - prints y or n. Same for directories. 
	▪	Mkdir and presmission 700
	▪	Get current date and time and use that in the name of the backup directory.
	▪	Create backup dir - username_backup_day_time
	▪	Move existing files into backup directory. 
