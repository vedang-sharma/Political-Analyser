import numpy as np

f = open('C:/Users/jayes/Desktop/collegeProject/mainefesto/health.txt', 'r+')
temp = [line for line in f.readlines()]
health = np.array(temp)
f.close()
print(health)

# f = open('C:/Users/jayes/Desktop/collegeProject/mainefesto/education.txt', 'r+')
# temp = [line for line in f.readlines()]
# education = np.array(temp)
# f.close()

# f = open('C:/Users/jayes/Desktop/collegeProject/mainefesto/infrastruture.txt', 'r+')
# temp = [line for line in f.readlines()]
# infrastruture = np.array(temp)
# f.close()

# f = open('C:/Users/jayes/Desktop/collegeProject/mainefesto/economy.txt', 'r+')
# temp = [line for line in f.readlines()]
# economy = np.array(temp)
# f.close()

# f = open('C:/Users/jayes/Desktop/collegeProject/mainefesto/agriculture.txt', 'r+')
# temp = [line for line in f.readlines()]
# agriculture = np.array(temp)
# f.close()

# years = [1999,2004,2009,2014,2019]

# # congress
# for year in years:
#     with open('C:/Users/jayes/Desktop/collegeProject/mainefesto/extracted/C'+str(year)+'.xml', 'r', encoding = 'utf-8', errors = 'ignore') as file_obj:
#         for sentence in file_obj:
#             pass            

# # BJP
# for year in years:
#     with open('C:/Users/jayes/Desktop/collegeProject/mainefesto/extracted/BJP'+str(year)+'.xml', 'r', encoding = 'utf-8', errors = 'ignore') as file_obj:
#         for sentence in file_obj:
#             pass