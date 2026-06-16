from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Task(BaseModel):
    id: int = 0
    title: str = ""
    isDone: bool = False
# the variables are required by default but we can set them to optional by giving them a default value, in this case we set them to empty string or false or 0 , it depends :)

#same as flask , for the root exept we use get as GET request not . route
@app.get("/")
def main():
    return "HOME"

tasks = []


# so here when we send the item we want to send it in json format and it will be converted to a Task object using pydantic, not in a query parameter or form data, but in the body of the request as json
#this is a route for tasks , to create the task , using POST
@app.post("/tasks")
def create_task(task: Task): # this will convert the json to a task object using pydantic
    # add the task to the list 
    tasks.append(task)
    # so it will return the whole tasks
    return tasks

# sending the post to the /tasks?task="eating" , while using the parameter to define the task

@app.get("/tasks")
def get_tasks(limit: int = 10): # this will limit the number of tasks to 10 by default
    return tasks[0:limit] # this wll return the first 10 tasks in the list by default

#this will get the task by its id (it place in the list)
@app.get("/tasks/{task_id}")
def get_task(task_id: int) -> Task: # this will convert the task_id to an int and return a Task object
    # we will check if the task is in the list or not
    if task_id >= len(tasks): 
        raise HTTPException(status_code=404, detail="Task not found")
    task = tasks[task_id] #serching the list by the index
    return task 