#!/usr/bin/env bash
#!/usr/bin/expect

if [[ $1 -eq  1 ]]
then
	git fetch origin
	echo fetch success
	git pull origin master
	echo pull success
elif [[ $1 -eq 2 ]]
then
	git add .
	echo Enter message
	read varname
	git commit -m $varname
	git push origin master
	echo push success

else
	echo Enter 1 for fetching updates from repository and 2 to push to repository
fi


