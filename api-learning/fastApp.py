from fastapi import FastAPI, HTTPException
# we run it through uvicorn
app = FastAPI()

#same as flask , for the root exept we use get as GET request not . route
@app.get("/")
def main():
    return "HOME"

tasks = []

#this is a route for tasks , to create the task , using POST
@app.post("/tasks")
def create_task(task):
    # add the task to the list 
    tasks.append(task)
    # so it will return the whole tasks
    return tasks

# sending the post to the /tasks?task="eating" , while using the parameter to define the task

#this will get the task by its id (it place in the list)
@app.get("/tasks/{task_id}")
def get_task(task_id: int): # this will convert the id to int or we could convert it manually (task_id = int(task_id))
    # we will check if the task is in the list or not
    if task_id > len(tasks): 
        raise HTTPException(status_code=404, detail="Task not found")
    task = tasks[task_id] #serching the list by the index
    return task