# Print Absolute Path - File System
# The program must accept a string S representing a file system as the input. The program must print the absolute path to each file in the given file system. If there is no file, then the program must print -1 as the output. The string S contains the names of the directories, sub-directories and files, where \n and \t are used to indicate the difference between the directories and sub-directories.

# Boundary Condition(s):
# 8 <= Length of S <= 1000

# Input Format:
# The first line contains S.

# Output Format:
# The line(s), each contains the absolute path to the file or the first line contains -1.

# Example Input/Output 1:
# Input:
# MyDir\n\tPhotos\n\t\tmyphoto.jpeg\n\t\tMiniProject\n\tDocuments\n\t\tIDProof\n\t\t\tMyAadhaar.pdf

# Output:
# MyDir\Photos\myphoto.jpeg
# MyDir\Documents\IDProof\MyAadhaar.pdf

# Explanation:
# The given file system is
# MyDir
# -> Photos
# -> -> myphoto.jpeg
# -> -> MiniProject
# -> Documents
# -> -> IDProof
# -> -> -> MyAadhaar.pdf

# Example Input/Output 2:
# Input:
# Hector\n\tAndroid\n\tJava\n\t\tNetBeans\n\t\tEclipse\n\tCodeBlocks\n\t\tSampleProject\n\tGeany

# Output:
# -1

# Explanation:
# The given file system is
# Hector
# -> Android
# -> Java
# -> -> NetBeans
# -> -> Eclipse
# -> CodeBlocks
# -> -> SampleProject
# -> Geany







