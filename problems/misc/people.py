# Name     |   Favorite Color  |  Birthday
# Theo     |   Green           |  October 10, 2000
# Sherwin  |   Blue            |  May 3, 2003
# Daniel   |   Orange          |  December 2, 2003
# Sunny    |   Orange          |  January 4, 1999
# Aubrianna|   Green           |  August 5, 1999


# 1-1) How would you represent this data?

from datetime import datetime
from dateutil import relativedelta


class Person:
    def __init__(self, name, color, birthday):
        self.name = name
        self.color = color
        self.birthday = birthday


class People:
    def __init__(self, people):
        self.people = people
        self.nameHashmap = {}
        self.colorHashmap = {}
        self.birthdayHashmap = {}
        self.ageHashmap = {}
        self.daysFromTodayHashmap = {}

        self.populateHashmaps()

    def populateHashmaps(self):
        for person in self.people:
            if person.name not in self.nameHashmap.keys():
                self.nameHashmap[person.name] = list()
            self.nameHashmap[person.name].append(person)

            if person.color not in self.colorHashmap.keys():
                self.colorHashmap[person.color] = list()
            self.colorHashmap[person.color].append(person)

            if person.birthday not in self.birthdayHashmap.keys():
                self.birthdayHashmap[person.birthday] = list()
            self.birthdayHashmap[person.birthday].append(person)

            age = self.calculateAge(person)
            if age not in self.ageHashmap.keys():
                self.ageHashmap[age] = list()
            self.ageHashmap[age].append(person)

            days = self.calculateDiffDays(person)
            if days not in self.daysFromTodayHashmap.keys():
                self.daysFromTodayHashmap[days] = list()
            self.daysFromTodayHashmap[days].append(person)

        print(self.daysFromTodayHashmap)

    def calculateAge(self, person):
        timeNow = datetime.now()

        personDate = datetime.strptime(person.birthday, "%B %d, %Y")
        difference = relativedelta.relativedelta(timeNow, personDate)
        return difference.years

    def calculateDiffDays(self, person):
        timeNow = datetime.now()

        personDate = datetime.strptime(person.birthday, "%B %d, %Y")
        return (timeNow - personDate).days

    def findByColor(self, color):
        if color in self.colorHashmap.keys():
            return self.colorHashmap[color]

    def findByAge(self, age):
        if age in self.ageHashmap.keys():
            return self.ageHashmap[age]

    def getSortedByDate(self):
        sortedByDate = list()
        if self.daysFromTodayHashmap:
            sortedKeys = sorted(self.daysFromTodayHashmap.keys())
            for key in sortedKeys:
                sortedByDate.extend(self.daysFromTodayHashmap[key])
        return sortedByDate


def toPrint(name, color, birthday):
    person = Person(name, color, birthday)
    print("Name: ", person.name)
    print("Favorite Color: ", person.color)
    print("Birthday: ", person.birthday)


people = list()


def addToList(name, color, birthday):
    person = Person(name, color, birthday)
    people.append(person)


addToList("Theo", "Green", "October 10, 2000")
addToList("Sherwin", "Blue", "May 3, 2003")
addToList("Daniel", "Orange", "December 2, 2003")

peopleObject = People(people)


# 1-2) write a function that accepts a color and returns the people
# that have that as their favorite color
def getPeopleByFavoriteColor(color):
    listOfPeople = peopleObject.findByColor(color)

    if listOfPeople:
        for person in listOfPeople:
            toPrint(person.name, person.color, person.birthday)


getPeopleByFavoriteColor("Green")
getPeopleByFavoriteColor("Blue")


# 1-3) write a function that accepts an age and returns the people that are that age
def getPeopleByAge(age):
    agePeople = peopleObject.findByAge(age)

    if agePeople:
        for person in agePeople:
            toPrint(person.name, person.color, person.birthday)
    else:
        print("No people of that age")


print("18:")
getPeopleByAge(18)
print("16:")
getPeopleByAge(16)


# 1-4) write a function that returns the people, but sorted by birthday
def getPeopleListSortedByBirthday():
    daysPeople = peopleObject.getSortedByDate()

    if daysPeople:
        for person in daysPeople:
            toPrint(person.name, person.color, person.birthday)


getPeopleListSortedByBirthday()
