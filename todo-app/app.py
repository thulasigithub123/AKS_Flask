from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory "database" (use a proper database for production)
tasks = []

@app.route("/")
def index():
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add_task():
    task = request.form.get("task")
    if task:
        tasks.append({"id": len(tasks) + 1, "task": task})
    return redirect(url_for("index"))

@app.route("/update/<int:task_id>", methods=["POST"])
def update_task(task_id):
    new_task = request.form.get("task")
    for task in tasks:
        if task["id"] == task_id:
            task["task"] = new_task
            break
    return redirect(url_for("index"))

@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
