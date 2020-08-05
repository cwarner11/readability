def main():

    #gets input of text
    text = input("Text: ")

    string = len(text)
    letters = 0
    words = 0
    sentences = 0

    #loops text
    for i in range(string):
        if text[i].isalpha():
            letters += 1

        #checks if character is a letter
        if i == 0 and text[0].isalpha() or text[i] == " " and i != string -1 and text[i +1] != " ":
            words += 1

        if text[i] == '?' or text[i] == '!' or text[i] == '.':
            sentences += 1

    #gets average letter per 100 words
    L = (float(letters) / float(words)) * 100

    #gets average sentences per 100 words
    S = (float(sentences) / float(words)) * 100

    #uses  Coleman-Liau index to compute grade level number
    grade = round( 0.0588 * L - 0.296 * S - 15.8 )

    #below grade 1
    if grade < 1:
        print("Before Grade 1")

    #at or above senior undergrad student
    elif grade >= 16:
        print("Grade 16+")

    else :
        print(f"Grade: {grade}")

main()
