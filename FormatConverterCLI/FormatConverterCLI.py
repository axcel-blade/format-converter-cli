class FormatConverterCLI:
    def mainMenu(self):
        isWrongChoice = True

        while(isWrongChoice):
            # Menu
            print("==================================")
            print("=        Format Converter        =")
            print("==================================\n")
            print("Please select the type of convertion you want to run:")
            print("1) Video")
            print("2) Audio")
            print("3) Image")
            print("4) Document")
            print("0) Exit")
            userChoice = input("\nChoose: ")

            match userChoice:
                case '1':
                    print(self.__str__(userChoice))
                    isWrongChoice = False

                case '2':
                    print(self.__str__(userChoice))
                    isWrongChoice = False
               
                case '3':
                    print(self.__str__(userChoice))
                    isWrongChoice = False

                case '4':
                    print(self.__str__(userChoice))
                    isWrongChoice = False

                case '0':
                    print(self.__str__(userChoice))
                    isWrongChoice = False

                case default:
                    print(self.__str__(userChoice))
                    print("\nPlease select corrent choice from the menu\n")

    def __str__(self,userChoice):
        return "User chose: " + userChoice

def main():
    FCCLI = FormatConverterCLI()
    FCCLI.mainMenu()

if __name__ == "__main__":
    main()