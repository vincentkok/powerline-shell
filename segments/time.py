
def add_time_segment():
    powerline.append(' $(date +"%T") ', Color.USERNAME_FG, Color.USERNAME_BG, powerline.separator_thin, Color.SEPARATOR_FG)

add_time_segment()