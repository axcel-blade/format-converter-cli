import threading
from Operations import *

class FormatConverterCLI:
    operations = Operations()

    def mainMenu(self):
        while True:
            # Main menu
            print("==========================================================")
            print("=                    Format Converter                    =")
            print("==========================================================\n")
            print("Please select the type of convertion you want to run:")
            print("1) Video")
            print("2) Audio")
            print("3) Image")
            print("4) Document")
            print("0) Exit")
            userChoice = input("\nChoose: ")

            match userChoice:
                case '1':
                    self.VideoConverterMenu()
                    break

                case '2':
                    print(self.__str__(userChoice))
                    break
               
                case '3':
                    print(self.__str__(userChoice))
                    break

                case '4':
                    print(self.__str__(userChoice))
                    break

                case '0':
                    print(self.__str__(userChoice))
                    break

                case default:
                    print(self.__str__(userChoice))
                    print("\nPlease select corrent choice from the menu\n")
        
    def VideoConverterMenu(self):
        while True:
            # Menu
            print("==========================================================")
            print("=                    Video Converter                     =")
            print("==========================================================\n")
            print("Please select the type of convertion you want to convert:")
            print("1) to MP4")
            print("2) to MKV")
            print("3) to AVI")
            print("4) to WebM")
            print("0) Back")
            userChoice = input("\nChoose: ")

            selectFile = self.operations.selectFile()
            #selectOutputLocation = self.operations.outputFileLocation() + "\Output.mp4"

            match userChoice:
                case '1':
                    self.operations.Convertion(selectFile, "Output.mp4")
                    break

                case '2':
                    break


    def __str__(self,userChoice):
        return "User chose: " + userChoice

def main():
    FCCLI = FormatConverterCLI()
    FCCLI.mainMenu()

if __name__ == "__main__":
    main()