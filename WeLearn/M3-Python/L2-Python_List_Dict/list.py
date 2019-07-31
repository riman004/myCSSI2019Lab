# students = ["Alice", "Javi", "Damien"]
# students.append("Delilah")
# print(students)
#
# students = ["Alice", "Javi", "Damien"]
# students.insert(1, "Zoe")
# print(students)
#
# students = ["Alice", "Javi", "Damien", "Javi"]
# students.remove("Javi")
# print(students)
#
# # my_list.insert(index, element)
#
# smith_siblings = ["Emily", "Monique", "Giovanni", "George", "Marisa", "Claire", "June"]
# for name in smith_siblings:
#     print(name + " Smith")

# smith_siblings = ["Emily", "Monique", "Giovanni", "Brianna", "Javi"]
# for index in range(len(smith_siblings)):
#     smith_siblings[index] = smith_siblings[index] + " Smith"
# print(smith_siblings)
# print index
#
# names = ["Rickon", "Bran", "Arya", "Sansa", "Jon", "Robb"]
# for i in range(len(names)):
#     if names[i] == "Jon":
#         names[i] += " Snow"
#     else:
#         names[i] += " Stark"
# print(names)

# artists = ["Tyler the Creator", "Frank Ocean", "Troye Sivan", "Kehlani", "Pouya", "Tame Impala"]
#
# demoted_artist = str(raw_input("What artist do you want to eliminate from the top 5?"))
#
# if demoted_artist in artists:
#     artists.remove(demoted_artist)
#     print("Top 5 heroes:", artists)
# else:
#     print("Hero not found")

names = ["Rickon", "Bran", "Arya", "Sansa", "Jon", "Robb"]
names[::-1]
names[4:2:-1]
print(names[:2])
print(names[4:2:-1])
