from fastapi import FastAPI
from model import Course
import json
import uvicorn

app = FastAPI()

FILE_NAME = "courses.json"


def load_courses():
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data


def save_courses(data):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


@app.get("/")
async def home():
    return {"message": "Course Record API Server"}


@app.get("/courses")
async def get_courses():
    courses = load_courses()
    return courses


@app.post("/courses")
async def add_course(course: Course):
    courses = load_courses()

    new_course = {
        "course_name": course.course_name,
        "year": course.year,
        "semester": course.semester,
        "grade": course.grade
    }

    courses.append(new_course)
    save_courses(courses)

    return {
        "message": "Course added successfully",
        "course": new_course
    }


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)