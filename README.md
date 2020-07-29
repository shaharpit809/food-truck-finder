# food-truck-finder

This is a command line project which is used to find all the Food Trucks that are open in San Francisco when the code is executed.

You can read more about my thought process for building a fully featured web application from [here](https://github.com/shaharpit809/food-truck-finder/blob/master/writeup.md)

## Prerequisites

- Check if `Python 3.x` version is installed or not
	- Check the version using `python --version`
	- If version 2.x is installed or you don't have python, you can download it from [here](https://www.python.org/downloads/)
- Check if `pip` is installed or not using `pip -V` on the command prompt
	- If not, you can install it from [here](https://pip.pypa.io/en/stable/installing/)
- Once pip is installed, install the libraries that are used in the code
	- Install datetime library using `pip install Datetime`
	- You can read more about it [here](https://pypi.org/project/DateTime/)
	- Install requests library using `pip install requests`
	- You can read more about it [here](https://pypi.org/project/requests/)
	
## Tips for better performance

- Socrata's API has a limit for every user which restricts it from being misused. If a user calls the API a large number of times, rate limitation is applied to the user sending those requests, to reduce throttling.
- Work other for this is to use an application token. An application token helps in attributing each request to a particular application and developer, granting each their own pool of API requests.
- Register yourself to get a token and get better performance from [here](https://dev.socrata.com/docs/app-tokens.html)
- Token will be used as a header that fetching the required data.
- Add the token variable into the `.bashrc` file on your shell.
- Create/Edit your .bashrc file by :
	- Going to the home directory by `cd ~`
	- Creating/Editing the file by `vi .bashrc`
	- Adding a new environment variable by `export APP_TOKEN=(your access key from the website)`
	- Reloading the file by `source .bashrc`
- Following the above steps will help you in getting a much better performance as opposed to the one where the token wasn't being used.

## Executing the program

- Clone the repository by `git clone food-truck-finder`
- Going into the directory by `cd food-truck-finder`
- Finally executing the program by `python show_open_food_trucks.py`
- Options available while executing,
	- Type `p` to get the previous 10 food trucks
	- Type `n` to get the next 10 food trucks
	- Type `q` to quit
	
## Possible improvements and assumptions
- Network improvements
	- There are multiple HTTP calls with a different offset, this increases the resource consumption and can reduce the performance.
	- If we are sure that the data size is not substantial, we can fetch all the records together and store them in a variable and only display the 10 required food trucks.
	- Single HTTP call gets all available food trucks at that time of execution.
	- If the user wishes to check the food trucks at a different time and doesn't exit the code, the user might see food trucks that were closed but stored in a local variable.
	- To prevent this issue, I went ahead with the implementation of multiple calls to the API to get the user the most accurate data.
	
- Caching improvements
	- Data can be stored in a dictionary, which `offset` and `time` as the key and food trucks as the value.
	- If the user wishes to check out the food trucks that were already checked before in a short span, we can directly fetch it from the dictionary and give it to the user.
	- This would also help in reducing the network calls.

	