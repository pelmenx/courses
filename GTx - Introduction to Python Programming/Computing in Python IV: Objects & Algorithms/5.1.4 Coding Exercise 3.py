# Previously, you wrote a class called ExerciseSession that
# had three attributes: an exercise name, an intensity, and a
# duration.
#
# Add a new method to that class called calories_burned.
# calories_burned should have no parameters (besides self, as
# every method in a class has). It should return an integer
# representing the number of calories burned according to the
# following formula:
#
# - If the intensity is "Low", 4 calories are burned per
#   minute.
# - If the intensity is "Moderate", 8 calories are burned
#   per minute.
# - If the intensity is "High", 12 calories are burned per
#   minute.
#
# You may copy your class from the previous exercise and just
# add to it.


# Add your code here!
class ExerciseSession():
    # init
    def __init__(self, exercise_init, intensity_init, duration_init):
        self.exercise = exercise_init
        self.intensity = intensity_init
        self.duration = duration_init

    # getter
    def get_exercise(self):
        return self.exercise

    def get_intensity(self):
        return self.intensity

    def get_duration(self):
        return self.duration

    # setter
    def set_exercise(self, new_exercise):
        self.exercise = new_exercise

    def set_intensity(self, new_intensity):
        self.intensity = new_intensity

    def set_duration(self, new_duration):
        self.duration = new_duration

    def calories_burned(self):
        if self.intensity == "Low":
            return self.duration * 4
        elif self.intensity == "Moderate":
            return self.duration * 8
        elif self.intensity == "High":
            return self.duration * 12


# If your code is implemented correctly, the lines below
# will run error-free. They will result in the following
# output to the console:
# 240
# 360
new_exercise = ExerciseSession("Running", "Low", 60)
print(new_exercise.calories_burned())
new_exercise.set_exercise("Swimming")
new_exercise.set_intensity("High")
new_exercise.set_duration(30)
print(new_exercise.calories_burned())
