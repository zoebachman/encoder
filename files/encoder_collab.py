def encode(string):

    result = []

    prevLetter = ''
    firsttimethough = True


    sameCt = 1

    for char in string :


        if (char == prevLetter):
            sameCt = sameCt + 1



        elif (char != prevLetter):

            if firsttimethough == False:
                result += str(sameCt)
                result += prevLetter
                # print sameCt
                # print prevLetter
                sameCt = 1

            firsttimethough = False



        prevLetter = char
    result += str(sameCt)
    result += prevLetter

    return ''.join(result)
    # print sameCt
    # print prevLetter

if __name__ == "__main__":
    print encode("EEEEEEvvvvvEEEE")
    # print (encode)
