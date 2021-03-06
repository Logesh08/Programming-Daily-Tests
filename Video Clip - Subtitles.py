# Video Clip - Subtitles
# There are N subtitles in a video. A boy wants to know the subtitles present in a video clip that starts from X to Y. The format of the time is MM:SS. The maximum length of the video is always less than 1 hour.
# The program must accept the N subtitles and the values of X, Y as the input. Each subtitle has a start time, the content and the number of seconds it lasts T. For each second in the video clip, the program must print the time (MM:SS) followed by the content of the subtitle as the output. If two or more subtitles are present in a second, then the program must print those subtitles separated by the pipe symbol (|) in the order of their occurrence. If there is no subtitle in the video clip, the program must print -1 as the output.
# Note: The N subtitles are always given in chronological order.

# Boundary Condition(s):
# 1 <= N <= 50
# 1 <= Length of each subtitle content <= 50
# 1 <= T <= 10

# Input Format:
# The first line contains N.
# The next N lines, each contains the start time, the content and the number of seconds it lasts separated by a space.
# The N+2nd line contains X and Y separated by a space.

# Output Format:
# The lines, each contains the time (MM:SS) followed by the content of the subtitle(s) or the first line contains -1 based on the given conditions.

# Example Input/Output 1:
# Input:
# 9
# 00:04 This is Matt. 2
# 00:07 Hi! I am Matt. 2
# 00:10 This is Gavin. 2
# 00:13 Hello. My name is Gavin. 3
# 00:18 What's your job? 3
# 00:24 I'm a jazz musician 5
# 00:28 Really? What do you play? 4
# 00:35 The drums. 2
# 00:45 Oh nice! 2
# 00:10 00:35

# Output:
# 00:10 This is Gavin.
# 00:11 This is Gavin.
# 00:12
# 00:13 Hello. My name is Gavin.
# 00:14 Hello. My name is Gavin.
# 00:15 Hello. My name is Gavin.
# 00:16
# 00:17
# 00:18 What's your job?
# 00:19 What's your job?
# 00:20 What's your job?
# 00:21
# 00:22
# 00:23
# 00:24 I'm a jazz musician
# 00:25 I'm a jazz musician
# 00:26 I'm a jazz musician
# 00:27 I'm a jazz musician
# 00:28 I'm a jazz musician | Really? What do you play?
# 00:29 Really? What do you play?
# 00:30 Really? What do you play?
# 00:31 Really? What do you play?
# 00:32
# 00:33
# 00:34
# 00:35 The drums.

# Explanation:
# Here X = 00:10 and Y = 00:35, so the video clip starts at 00:10 and ends at 00:35.
# The subtitles in the video clip are printed as the output.

# Example Input/Output 2:
# Input:
# 9
# 00:04 This is Matt. 2
# 00:07 Hi! I am Matt. 2
# 00:10 This is Gavin. 2
# 00:13 Hello. My name is Gavin. 3
# 00:18 What's your job? 3
# 00:24 I'm a jazz musician 5
# 00:28 Really? What do you play? 4
# 00:35 The drums. 2
# 00:45 Oh nice! 2
# 00:37 00:44

# Output:
# -1