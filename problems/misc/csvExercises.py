"""
Write an exercise loader class.  Exercises are stored in a CSV as id, name, glycemic index.
Load the data as part of the object initialization and provide a sensible interface to query
the data.

Example CSV file:
id,name,glycemic_index
2,running,34
5,crunch,20
6,"exercise,”,40

Notes
Code does not have to compile
Feel free to use google
Use whatever language and editor you would like
id and name are unique
"""
import _csv


class Exercise:
    def __init__(self, id, name, glycemic_index):
        self.id = id
        self.name = name
        self.glycemic_index = glycemic_index


class Exercises:
    def __init__(self, listOfExercises):
        self.listOfExercises = listOfExercises
        self.idExerciseMap = {}
        self.nameExerciseMap = {}
        self.glycExerciseMap = {}
        self.populateHashmaps()

    def populateHashmaps(self):
        for exercise in self.listOfExercises:
            self.idExerciseMap[exercise.id] = exercise
            self.nameExerciseMap[exercise.name] = exercise
            if exercise.glycemic_index not in self.glycExerciseMap.keys():
                self.glycExerciseMap[exercise.glycemic_index] = list()
            self.glycExerciseMap[exercise.glycemic_index].append(exercise)

    def findById(self, id):
        if id in self.idExerciseMap.keys():
            return self.idExerciseMap[id]

    def findByName(self, name):
        if name in self.nameExerciseMap.keys():
            return self.nameExerciseMap[name]

    def findByGlycIndex(self, index):
        if index in self.glycExerciseMap:
            return self.glycExerciseMap[index]


def loader(csv_file):
    with open(csv_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            exercise = Exercise(row['id'], row['name'], row['glycemic_index'])

            print(row['first_name'], row['last_name'])
