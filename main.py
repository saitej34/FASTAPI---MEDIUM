from fastapi import FastAPI

app = FastAPI()


dataset =[{"id":1,"name":"saiteja","marks":125},{"id":2,"name":"raj","marks":135},{"id":3,"name":"mani","marks":97}]


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/getAll")
def getData():
    return dataset


@app.get("/get/{item_id}")
def get_item(item_id: int):
    for i in dataset:
        if i["id"] == item_id:
            return i
    return {"status": "Record Not Found"}



@app.post('/add')
def addData(item: dict):
    dataset.append(item)
    return dataset


@app.delete('/delete/{id}')
def deleteData(id : int):
    for i in range(len(dataset)):
        if(dataset[i]["id"]==id):
            dataset.remove(i)
            return dataset
    return {"status":"Id Not found"}


@app.put('/edit/{id}')
def editData(item : dict):
    for i in dataset:
        if(i["id"]==id):
            i=item 
            return dataset 
    return {"status" : "Id not found"}



           
    
    
