import os

## 可能不需要这个function，或者改这个function，load分解之后的存储的地方
def get_valid_directory():
    while True:
        # directory_path = "/song-connector/快乐1demo"
        input("Please enter the path to the directory containing the audio files: ")
        if os.path.exists(directory_path) and os.path.isdir(directory_path):
            return directory_path
        else:
            print("Invalid directory. Please enter a valid path.")
