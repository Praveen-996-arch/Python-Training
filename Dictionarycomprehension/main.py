# import random
# names = ["Manu", "Praveen", "Isha", "Eleanor", "Sam", "Sophie"]
# student_scores= {name:random.randint(1,100) for name in names}
# print(student_scores)
# passsed_students = {name : student_score for name, student_score in student_scores.items() if student_score >=60}
# print(passsed_students)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word:len(word)for word in sentence.split()}
print(result)