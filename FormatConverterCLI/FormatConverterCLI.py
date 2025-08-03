import threading
from Operations import *

class FormatConverterCLI:
    def __init__(self):
        self.operations = Operations()

    def mainMenu(self):
        while True:
            # Main menu
            print("==========================================================")
            print("=                    Format Converter                    =")
            print("==========================================================\n")
            print("Please select the type of conversion you want to run:")
            print("1) Video")
            print("2) Audio")
            print("3) Image")
            print("4) Document")
            print("0) Exit")
            userChoice = input("\nChoose: ")

            match userChoice:
                case '1':
                    self.VideoConverterMenu()

                case '2':
                    print("Audio conversion - Coming soon!")
                    input("Press Enter to continue...")
               
                case '3':
                    print("Image conversion - Coming soon!")
                    input("Press Enter to continue...")

                case '4':
                    print("Document conversion - Coming soon!")
                    input("Press Enter to continue...")

                case '0':
                    print("Goodbye!")
                    return

                case _:  # Use _ instead of default for Python 3.10+
                    print(f"Invalid choice: {userChoice}")
                    print("Please select a correct choice from the menu\n")
                    input("Press Enter to continue...")
        
    def VideoConverterMenu(self):
        while True:
            # Menu
            print("==========================================================")
            print("=                    Video Converter                     =")
            print("==========================================================\n")
            print("Please select the conversion format:")
            print("1) to MP4")
            print("2) to MKV")
            print("3) to AVI")
            print("4) to WebM")
            print("0) Back")
            userChoice = input("\nChoose: ")

            match userChoice:
                case '1':
                    self.convertToFormat("mp4")
                    break

                case '2':
                    self.convertToFormat("mkv")
                    break
                
                case '3':
                    self.convertToFormat("avi")
                    break
                
                case '4':
                    self.convertToFormat("webm")
                    break

                case '0':
                    return

                case _:
                    print(f"Invalid choice: {userChoice}")
                    print("Please select a correct choice from the menu\n")
                    input("Press Enter to continue...")

    def convertToFormat(self, targetFormat):
        # Select input video file
        print(f"\nConverting to {targetFormat.upper()} format")
        print("Step 1: Select the video file to convert")
        
        inputFile = self.operations.selectVideoFile()
        if not inputFile:
            print("No file selected. Returning to menu.")
            input("Press Enter to continue...")
            return

        # Select output location
        print("Step 2: Select the output folder")
        outputFolder = self.operations.outputFileLocation()
        if not outputFolder:
            print("No output folder selected. Returning to menu.")
            input("Press Enter to continue...")
            return

        # Generate output file path
        outputFile = self.operations.generateOutputPath(inputFile, outputFolder, targetFormat)
        
        # Confirm conversion
        print(f"\nInput file: {inputFile}")
        print(f"Output file: {outputFile}")
        confirm = input("Do you want to proceed with the conversion? (y/n): ").lower()
        
        if confirm == 'y' or confirm == 'yes':
            print("\nStarting conversion...")
            success = self.operations.conversion(inputFile, outputFile)
            
            if success:
                print("Conversion completed successfully!")
            else:
                print("Conversion failed. Please check the error messages above.")
        else:
            print("Conversion cancelled.")
        
        input("Press Enter to continue...")

def main():
    FCCLI = FormatConverterCLI()
    FCCLI.mainMenu()

if __name__ == "__main__":
    main()