# error handling and JSON
## catching exceptions
when dealing with exceptions there are 4 main words.    
try: #something that might cause an exception   
except: #do this if there was an exception  
else: do this if there were no exceptions   
finally: do this no matter what happens 
    raise #type of error and can specify the message
    raise KeyError("message error")

bare except will accept everything, try to capture certain types of errors. 

except KeyError as error_message: # to get hold of the error information    

using pass in except just skips this code.  

If you want to loop a exception handling put it into a function.

## JSON data
JavaScriptOrientated... 
json.dump() write -> json.dump(what you want to dump, where in file)    
json.load() read    
json.update() update    
by adding indent= you can format your data. 

with open("data.json", mode='r') as f:  
    data = json.load(f)#reading old data     
    data.update(new_data)  #updating old data with new data 
with open("data.json", mode='w') as f:  
    json.dump(data, f, indent=4) # saving updated data