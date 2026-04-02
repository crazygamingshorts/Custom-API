from fastapi import FastAPI, HTTPException
import json

app = FastAPI()

# load knowledge
def load_knowledge():
    with open("knowledge.json", "r") as f:
        return json.load(f)

# save knowledge
def save_knowledge(data):
    with open("knowledge.json", "w") as f:
        json.dump(data, f, indent=2)

# ask প্রশ্ন
@app.get("/")
def home():
    return {"message": "CrazyBot API Running"}

@app.get("/ask")
def ask(q: str):
    knowledge = load_knowledge()
    q = q.lower()

    if q in knowledge:
        return {"answer": knowledge[q]}
    else:
        return {"answer": "I don't know yet"}

# new knowledge add
@app.post("/add")
def add(q: str, ans: str):
    knowledge = load_knowledge()
    knowledge[q.lower()] = ans
    save_knowledge(knowledge)

    return {"message": "Knowledge added successfully"}
