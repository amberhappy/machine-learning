import pickle

a_dict = {'da':111,2:[23,1,4],'23':{1:2,'d':'sad'}}

file = open('6_example.pickle','wb')
pickle.dump(a_dict,file)
file.close()

with open('6_example.pickle','rb') as file:
    a_dict1 = pickle.load(file)
    print(a_dict1)