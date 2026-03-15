text = input("Enter a text: ")

words = text.split()

frequency = {}

for word in words:
    if word in frequency:
        frequency[word] = frequency[word] + 1
    else:
        frequency[word] = 1


word_list = []

for word in frequency:
    word_list.append((word, frequency[word]))


word_list.sort(reverse=True)

top5 = word_list[:5]


total_words = len(words)

top5_count = 0

for word, count in top5:
    top5_count = top5_count + count

print("Top 5 tu pho bien:")

for word, count in top5:
    print(word, ":", count)


print("tong so tu la:", total_words)

percentage = (top5_count / total_words) * 100

print(" phan tram 5 tu sd nhieu nhat:", percentage, "%")