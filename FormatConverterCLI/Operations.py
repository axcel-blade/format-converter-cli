from tkinter import filedialog
import ffmpeg
import os

class Operations():
    # Select the video file that needs to convert
    def selectVideoFile(self):
        filePath = filedialog.askopenfilename(
            title="Select a video file",
            filetypes=[
                ("Video files", "*.mp4 *.avi *.mkv *.mov *.wmv *.flv *.webm *.m4v *.3gp"),
                ("MP4 files", "*.mp4"),
                ("AVI files", "*.avi"),
                ("MKV files", "*.mkv"),
                ("All files", "*.*")
            ]
        )

        if filePath:
            print("Selected file:", filePath)
        return filePath

    # Select the folder where the converted file should be saved 
    def outputFileLocation(self):
        folderPath = filedialog.askdirectory(
            title="Select output folder"
        )

        if folderPath:
            print("Selected folder:", folderPath)
        return folderPath

    # Converting current file type to selected file type
    def conversion(self, inputFile, outputFile):
        try:
            print(f"Start converting {self.fileBaseName(inputFile)} to {os.path.basename(outputFile)}")
            
            # Use appropriate codec for MP4 conversion
            (
                ffmpeg
                .input(inputFile)
                .output(outputFile, vcodec='libx264', acodec='aac')
                .overwrite_output()  # Overwrite output file if it exists
                .run(quiet=True)
            )
            
            print(f"Conversion completed: {outputFile}")
            return True

        except ffmpeg.Error as e:
            print("Error occurred during conversion:")
            print(f"stdout: {e.stdout.decode() if e.stdout else 'None'}")
            print(f"stderr: {e.stderr.decode() if e.stderr else 'None'}")
            return False
        except Exception as e:
            print(f"Unexpected error: {e}")
            return False
    
    # Getting the file name and the file extension
    def fileBaseName(self, filePath):
        baseName = os.path.basename(filePath)
        return baseName
    
    # Generate output file path with proper naming
    def generateOutputPath(self, inputFile, outputFolder, targetExtension):
        # Get the base name without extension
        baseName = os.path.splitext(os.path.basename(inputFile))[0]
        # Create output filename with target extension
        outputFileName = f"{baseName}.{targetExtension}"
        # Combine with output folder
        outputPath = os.path.join(outputFolder, outputFileName)
        return outputPath