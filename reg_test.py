import re
import csv
import pandas as pd

with open("../data/linortek.txt") as file:
    lines = file.readlines()  # 

reg = r"\w([A-Za-z\s]+)" # this is regualar express for the school
line_list = []
school_list = []

for line in lines:
    line_list.append(line.strip())
    school = re.search(reg, line)
    
    if school:
        school_list.append(school.group())
    else:
        pass
school_list = school_list[1::]  # remove the 1st line

school_list = pd.DataFrame(school_list)
school_list = school_list.values
print(school_list)


#school_list.to_csv("../data/School_list.csv")
    