# iterator
# iterate over X

numbers = [1, 2, 3, 4, 5]

# num becomes each thing within numbers 1 by 1

# for num in numbers:
#    if num == 3:
#        print("My fave")
#    else:
#        print(f"the number is {num}")
# print("the loop has ended")

# #the loop has ended when its no longer indented


# nested_list = [[1, 2, 3], [4, 5], [6]]
# for sub_list in nested_list:
#     print(sub_list)
#     for sub_list in sub_list:
#         print(sub_list)

# book = {
#     "name": "The Iliad",
#     "author": "Homer",
#     "rating": 7


# # .items is a tuple that gives you everything (key and value), just printing gives you the key
# #
# # for something in book.values():
# #     print(something)
#
# # can also use k or v instead of key and value
# for key, value in book.items():
#     print(f"The {key} is {value}")


# a list of dictionaries
# library = [
#     {
#         "name": "The Iliad",
#         "author": "Homer",
#         "rating": 7
#     },
#     {
#         "title": "The foundations of Maths",
#         "author": "Ian Stewart",
#         "rating": 8.5,
#         "synopsis": "Lots of maths"
#
#     },
#     {
#         "title": "The Very Hungry caterpillar",
#         "author": "Eric Carle",
#         "rating": 10,
#         "synopsis": "caterpillar eats lots"
#     }
# ]


# play around with iterating with the list
# then iterate through each dictionary
# do something


# for book in library:
#     print(book)
#
# for book in library:
#     for key, value in book.items():
#         print(f"{key} is {value}")
#         print("")


# iterate through library
# if the book has a synopsis, print the title and synopsis

# for book in library:
#     if "synopsis" in book.keys():
#         print(f"{book['title']}: {book['synopsis']}")

# loops are very slow,cut down on them as much as possible in future

# with range can set start and end
# for i in range(5,10):
#     print(i)