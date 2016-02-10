"""
Problem:

Your start-up is building a basic prototype where users can save URLs to your service with the idea that they can retrieve them later (perhaps when they have time to read them).  You've been put in charge with writing the server-side implementation of this service..

For the purposes of this exercise, let's make the following assumptions:
- You will just be responsible for writing functions that take input, take the appropriate action, and return if necessary (e.g. and not handle HTTP requests, etc)
- Your prototype stack does not contain a database (you're a start-up, remember?).  You will need to store all data in memory (e.g. datastructures).  
- You can implement this in the language of your choice.  Your code is not required to compile or run.  
- Solutions to all 3 problems should live in the same file.  Make sure your implementation to past problems are updated as you work on future problems.  For example, if you need something to happen in saveUrl() from problem #1 for problem #2 or #3, please update it!

Problem #1: Build Create, Read and Delete operations for this service.

- Build a "Create" function called saveUrl() which takes in as input a userToken (String) and URL (String) and returns a boolean value of whether or not the URL was successfully saved.  If the URL has been saved for the user previously, this function should not save it and return false.
- Build a "Read" function called getUrlsForUser() takes in a userToken and returns an array or list of all the URLs that user has saved, if any.
- The "Delete" function called removeUrl() which takes in a userToken (String) and URL (String) and returns a boolean value of whether or not it was successfully deleted.  If the URL to be deleted has never been saved, the function should return false.

Problem #2: B2B

Your service is a hit.  Tons of users are saving URLs and life is good.  Le'ts imagine you're approached by website publishers (CNN, ESPN, etc) that want to find out which users have currently saved 1 or more of *their* URLs to your service.  Let's build a function called b2bUsers() which takes in a domain name String (e.g. "espn.com") and returns a list or array of user tokens.

Assumptions:
 - Imagine we have a magical function (let's call it getDomain()) that when given a String input of a URL, will return the domain name).  For example, getDomain("http://www.espn.com/story1") will return "espn.com"
 - Ignore any complexities around subdomains. 
 - Only use currently saved data.  If a user had saved a URL, but removed it, it does not count.

Problem #3: Power Users

Next, you want to know who your power users are so you can talk to them and learn their impressions of the product.  Let's build a function called powerUsers() that takes in no input and will return an array or list of the 5 user tokens that have stored the most URLs.  

"""


# Problem 1

"""def saveUrl(userToken, URL):
    global users
    if userToken in users:
        if URL in users[userToken]:
            return False
        else:
            users[userToken].append(URL)
            return True
    else:
        users[userToken] = [URL]
        return True

def Read(userToken):
    global users
    return users[userToken]

def removeUrl(userToken, URL):
    global users
    if userToken in users:
        if URL in users[userToken]:
            users[userToken].remove(URL)
            return True
        else:
            return False
    else:
        return False

users = {}"""


# for problem 1 I created a dictionary, with the URLS inside of lists. In reality
# a set might make more sense than a list, since you don't want duplicates, but
# the question wanted me to check for duplicates in code, so I used a list.


#Problem 2

"""class Entry:
    def __init__(self, userToken, URL):
        self.userToken = userToken
        self.URL = URL

def saveUrl(userToken, URL):
    global users
    if userToken in users:
        if any(user.URL == URL for user in users[userToken]):
            return False
        else:
            users[userToken].append(Entry(userToken, URL))
            return True
    else:
        users[userToken] = [Entry(userToken, URL)]
        return True

def Read(userToken):
    global users
    return [user.URL for user in users[userToken]]

def removeUrl(userToken, URL):
    global users
    if userToken in users:
        for entry in users[userToken]:
            if entry.url == URL:
                users[UserToken].remove(entry)
                return True
        else:
            return False
    else:
        return False


def b2bUsers(URL):
    global users
    userList = [entry.userToken for entry in [x for sublist in users.values() for x in sublist] if entry.URL == URL]
    if userList:
        return userList
    else:
        return False

users = {}

"""

#I chose to alter this by adding an object containing both the URL string and the User, rather
#than purely the URL. I thought this would make it more efficient to search through. I'm sure
#there are more efficient ways to create a data structure but I'm going with 45 minute time
#constraints.
#Also, I didn't put in the getDomain() function, as it makes my code untestable. But it could
#be wrapped around the entry.URL on line 86.


"""

Problem #3: Power Users

Next, you want to know who your power users are so you can talk to them and learn their impressions of the product.  Let's build a function called powerUsers() that takes in no input and will return an array or list of the 5 user tokens that have stored the most URLs.  """

"""class Entry:
    def __init__(self, userToken, URL):
        self.userToken = userToken
        self.URL = URL

def saveUrl(userToken, URL):
    global users
    if userToken in users:
        if any(user.URL == URL for user in users[userToken]):
            return False
        else:
            users[userToken].append(Entry(userToken, URL))
            return True
    else:
        users[userToken] = [Entry(userToken, URL)]
        return True

def Read(userToken):
    global users
    return [user.URL for user in users[userToken]]

def removeUrl(userToken, URL):
    global users
    if userToken in users:
        for entry in users[userToken]:
            if entry.url == URL:
                users[UserToken].remove(entry)
                return True
        else:
            return False
    else:
        return False


def b2bUsers(URL):
    global users
    userList = [entry.userToken for entry in [x for sublist in users.values() for x in sublist] if entry.URL == URL]
    if userList:
        return userList
    else:
        return False



def powerUsers():
    global users
    if len(users) >= 5:
        return [entry[0] for entry in sorted([[user, len(users[user])] for user in users], key = lambda x: x[1], reverse=True)[0:5]]
    else:
        return False

users = {}"""

"""saveUrl("Andrew", "espn.com")
saveUrl("Andrew", "cnn.com")
saveUrl("Andrew", "fox.com")
saveUrl("Andrew", "firefly.com")
saveUrl("Andrew", "amazon.com")
saveUrl("Andrew", "google.com")

saveUrl("Billy", "espn.com")
saveUrl("Billy", "cnn.com")
saveUrl("Billy", "fox.com")
saveUrl("Billy", "firefly.com")
saveUrl("Billy", "amazon.com")
saveUrl("Billy", "google.com")
saveUrl("Billy", "yahoo.com")

saveUrl("Charles", "firefly.com")
saveUrl("Charles", "amazon.com")
saveUrl("Charles", "google.com")
saveUrl("Charles", "yahoo.com")

saveUrl("James", "espn.com")
saveUrl("James", "cnn.com")
saveUrl("James", "fox.com")

saveUrl("Mark", "espn.com")
saveUrl("Mark", "cnn.com")

saveUrl("Fred", "espn.com")

print powerUsers()"""

#I left some test values in for the final version of the program.
#Line 147 is a bit ugly but I think it's pretty efficient
#Essentially I create a list, containing an array of 2 values, the users
#and their number of URLS. Then it sorts the list by the number of URLS
#and returns another list only containing the names, in order. It cuts off
#so it's only the first 5.
#it wasn't explicitly stated but I returned False with under 5 users.
