from flask import Flask, render_template, request, redirect, url_for

skills_app = Flask(__name__)
my_skills = [("Html", 80), ("CSS", 75), ("Python", 95), ("MySQL", 45), ("Flask", 60)]

@skills_app.route("/", methods=["GET", "POST"])
def skills():
    global my_skills
    if request.method == "POST":
        if 'delete' in request.form:
            skill_to_delete = request.form.get("delete")
            my_skills = [skill for skill in my_skills if skill[0] != skill_to_delete]
        else:
            skill_name = request.form.get("skill_name")
            skill_progress = request.form.get("skill_progress")
            if skill_name and skill_progress:
                my_skills.append((skill_name, int(skill_progress)))
        return redirect(url_for("skills"))
    
    return render_template("skills.html",
                            title="My Skills",
                            css_file="css/skills.css",
                            page_head="Skills App",
                            description="Add Your Skills Here",
                            skills=my_skills)

if __name__ == "__main__":
    skills_app.run(debug=True, port=5000)
    