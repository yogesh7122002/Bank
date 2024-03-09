file = open('story.txt','r')
story = file.read()
file.close()

print(story)

start_of_word = -1
target_start="<"
target_end=">"
# print(story)

words =set()
for i,char in enumerate(story):
    if char == target_start:
        start_of_word = i

    if char == target_end and start_of_word!=-1: 
        word = story[start_of_word:i+1]
        words.add(word)
        start_of_word=-1

# print(words)
answers={}
for word in words:
    answer = input("Enter the Word For" +word+"  :")
    answers[word]= answer
    
# print(answers)
# answers = {}
# for word in words:
#     answer = input("Enter the word for " + word + "  :")
#     answers[word] = answer

for word in words:
    story  = story.replace(word,answers[word])


print(story)

