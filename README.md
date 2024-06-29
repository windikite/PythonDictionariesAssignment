My 9th assignment! Although I was able to pull a lot of ideas from my to-do list application, this still had some unique problems that made it much harder. My main problems revolved around using the dictionary structure to store, retrieve and update data more than one layer deep, and corelate between keys and values.

An example of this from the ticketing system is as follows:
    1. Prompt user with list of values from dictionary
    2. Determine what key corresponds to it and store it for reference later
    3. Use the key to access the value, such as updating it

In js I would probably have stored the data in an array or something, allowing me to easily work by index and/or find. However, even using objects with keyvalue pairs to store info it'd be a simple enough matter to temporarily convert it to an array with Object.entries and loop through it at a minimum. Dictionaries does have dictionary.items() but I couldn't find a good solution for working with them like how I wanted. I definitely want to come back to this at some point, because I feel like I'm missing something and should be able to get the items in a dictionary, present the values to the user, and grab the corresponding key that goes with it afterward. Then pass a function the dictionary, the key and a new value and update the value of that key on the dictionary without issue. 