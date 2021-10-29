import os


def isBinod(filename):
    with open(filename, "r") as f:
        fileContent = f.read()

    # Detect all forms if Binod like bInOd
    if "binod" in fileContent.lower():
        return True

    else:
        return False


if __name__ == "__main__":
    #Listing the contents of this folder
    dir_contents = os.listdir()

    nBinod = 0
    # for each text file, run isBinod for them

    for item in dir_contents:
        if item.endswith('txt'):
            print(f"Detecting Binod in {item}")
            flag = isBinod(item)
            if(flag):
                print(f"**********Binod founf in {item}")
                nBinod += 1
            else:
                print(f"Binod not found in {item}")

        print("***********Binod Detector Summary**********")
        print(f"{nBinod} files found with Binod hidden in them")