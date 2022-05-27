 su username -- Change from current user to [username]

id -un --- Print the effective user

groups --- Print group of current user

chown username filename -- Change owner of [filename] to [username]

touch filename --- Creates an empty with name [filename]

chmod 744 filename --- adds execute permission to the owner of the file 

chmod 754 filename --- adds execute permission to the owner and the group owner, and read permission to other users, to the a file with name with [filename]


chmod a+x filename  --- adds execution permission to the owner, the group owner and the other users, to the file


chmod 007 -- owner, group no permission, others all permission


chmod 753 -- owner all permission, group read,execute permission other users write execute permission

chmod --reference=file-take-from file-taking --- set the permission of a file to another

chmod -R ogu+X dir --- Recursively add execute permission for owner, group, other users to [dir] and subdirectories

mkdir -m permission directory --- create a directory with that specify permission


chgrp groupname filename ---change the file group to the specify group

chown -hR owner:group dir -- set all the files and directories and subdirectories owner and group to the specify owner and group


chown -h owner:group filename -- set the file owner and group to the specify owner and group


chown --from=old-owner new-owner file -- change a specify owner of a file to new specify new owner

telnet towel.blinkenlights.nl -- play stars war in terminal
