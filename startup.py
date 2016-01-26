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