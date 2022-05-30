


echo "Hello, World" -- Prints hello world on a new line.

echo "\"(Ôo)'"  -- Prints "(Ôo)'

cat /etc/passwd -- display the content of the file /etc/passwd


cat /etc/passwd /etc/hosts -- concatenate and display the contents of /etc/passwd /etc/hosts files


tail /etc/passwd --- prints the last 10 line ofbthe file /etc/passwd


head /etc/passwd --- Display the first 10 lines of /etc/passwd


head -n 3 iacta | tail -n 1 --- prints the third of the file iacta


echo "Best School" > \\\*\\\\"'\"Best School\"\\\'"\\\\\*\$\\\?\\*\\\*\\\*\\\*\\\*\:\) -- create a file with this long and content Best School

ls -la > 8-cwd-state --- writes into the file ls-cwd-content the result of the command ls -la. If the file ls-cwd-content already exists, it should be overwritten. If the file ls-cwd-content does not exist, create it.


tail -n 1 >> iacta  -- duplicates the last line of the file iacta

find . -type f -name "*.js" -delete --- deletes all the regular files (not the directories) with a .js extension that are present in the current directory and all its subfolders.


