import sys

if len(sys.argv) < 3:
    print("You need to enter the information in that order: python scriptName.py fileName.txt number_of_common_words")
    sys.exit(1)

file_name = sys.argv[1]
n = int(sys.argv[2])

with open(file_name, "r") as file:
    line = file.readline().strip()

word_list = line.split()

def count_elements_in_taples(list):
    dict = {}
    for element in list:
        if element not in dict:
            dict[element] = 1
        else:
            dict[element] += 1
    return dict
            
count_word = count_elements_in_taples(word_list)

#n = int(input("Enter the number of common words that you want to see:"))

sorted_list = sorted(count_word.items(), key = lambda x: x[1], reverse=True)

if n > len(sorted_list):
    print(f"There are only {len(sorted_list)} words in your file:")

    #הוספתי את זה כדי למנוע העמסת יתר על המחשב
    #בלי זה עם מגדירים את המשתנה למספר גדול מאוד בקנה מידה של מיליונים המחשב נכלא סתם בלולאה למשך הרבה זמן
    n = len(sorted_list)

for i in range(n):
    for taple in sorted_list:
        print(f"{i+1}- word \"{taple[0]}\" {taple[1]} times")
        if len(sorted_list) != 0:
            sorted_list.pop(0)
        break










#עשיתי את הדרך הזאת ואז קלטתי שביקשתם דרך ספציפית
#for i in range(n):
    #max_value = max(count_word.values())
    #for key, value in count_word.items():
        #if value == max_value:
            #print(f"{i+1}- word {key} {value} times")
            #count_word.pop(key)
            #break

