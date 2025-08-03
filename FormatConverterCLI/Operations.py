from tkinter import filedialog
import ffmpeg
import os

class Operations():
    # Select the file that need to convert
    def selectFile(self):
        filePath = filedialog.askopenfilename(
            title="Select a file",
            filetypes=[("All files", "*.*")]
        )

        print("Selected file:", filePath)
        return filePath

    # Select the folder where should the converter format output should save 
    def outputFileLocation(self):
        folderPath = filedialog.askdirectory(
        title="Select a folder"
        )

        print("Selected folder:", folderPath)
        return folderPath

    # Converting current file type to selected file type
    def Convertion(self, inputFile, outputFile):
        try:
            print(f"Start converting {self.fileBaseName(inputFile)} to {self.fileBaseName(outputFile)}")
            ffmpeg.input(inputFile).output(outputFile, codec='copy').run()
            print(f"Conversion completed: {outputFile}")

        except ffmpeg.Error as e:
            print("Error occurred during conversion:", e)
    
    # Getting the file name and the file extension
    def fileBaseName(self, filePath):
        baseName = os.path.basename(filePath)
        #fileName, fileExtension = os.path.splitext(baseName)

        #return fileName, fileExtension
        return baseName