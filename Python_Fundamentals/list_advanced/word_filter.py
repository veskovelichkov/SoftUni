random_words = input().split(" ")
even_length_words = [word for word in random_words if len(word) % 2 == 0]
print("\n".join(even_length_words))
