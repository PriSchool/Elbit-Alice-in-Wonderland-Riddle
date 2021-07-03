def constConverterFunc(values, multiConstInput):
    for i in range(17):
        values[i] = (values[i] * multiConstInput)
    return values

def PrintAnswer(defangedText, decimalValuesList):
    global multiConst
    changedValues = constConverterFunc(decimalValuesList, multiConst)
    print(changedValues)
    print("+====================+")
    for i in range(6):
        print(defangedText[changedValues[i]], end = '')
    print("//", end = '')
    for i in range(6, 11):
        print(defangedText[changedValues[i]], end = '')
    print("/", end = '')
    for i in range(11, 17):
        print(defangedText[changedValues[i]], end = '')
    print("\n")

def converter(inputNumber, base):
    #split number in figures
    figures = [int(i,base) for i in str(inputNumber)]
    #invert oder of figures (lowest count first)
    figures = figures[::-1]
    result = 0
    #loop over all figures
    for i in range(len(figures)):
        #add the contirbution of the i-th figure
        result += figures[i]*base**i
    return result

origValues = [36, 17, 17, 44, 12, 0x3A, 0x3D, 0x09, 0x26A, 18, 0x1B, 58, 0x19C, 58, 13, 31, 18]

inputText = "CHAPTER I. Down the Rabbit-Hole Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, ‘and what is the use of a book,’ thought Alice ‘without pictures or conversations?’ So she was considering in her own mind (as well as she could, for the hot day made her feel very sleepy and stupid), whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her. There was nothing so VERY remarkable in that; nor did Alice think it so VERY much out of the way to hear the Rabbit say to itself, ‘Oh dear! Oh dear! I shall be late!’ (when she thought it over afterwards, it occurred to her that she ought to have wondered at this, but at the time it all seemed quite natural); but when the Rabbit actually TOOK A WATCH OUT OF ITS WAISTCOAT-POCKET, and looked at it, and then hurried on, Alice started to her feet, for it flashed across her mind that she had never before seen a rabbit with either a waistcoat-pocket, or a watch to take out of it, and burning with curiosity, she ran across the field after it, and fortunately was just in time to see it pop down a large rabbit-hole under the hedge. In another moment down went Alice after it, never once considering how in the world she was to get out again."
defangedText = inputText.replace(" ", "")
multiConst = 2

decimalValuesList15 = [51, 22, 22, 64, 17, 55, 58, 9, 550, 23, 26, 83, 372, 83, 18, 46, 23] #base 15

PrintAnswer(defangedText, decimalValuesList15)