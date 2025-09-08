from flask import Flask, render_template, request 

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        try:
            heart_rate = int(request.form.get("heart_rate", 0))
            bp_systolic = int(request.form.get("bp_systolic", 0))
            bp_diastolic = int(request.form.get("bp_diastolic", 0))
            breathing_rate = int(request.form.get("breathing_rate", 0))
            oxygen_level = int(request.form.get("oxygen_level", 0))

            result += f"<p>❤️ <strong>Heart Rate:</strong> {heart_rate} bpm</p>"
            result += f"<p>🩸 <strong>Blood Pressure:</strong> {bp_systolic}/{bp_diastolic} mmHg</p>"
            result += f"<p>🌬️ <strong>Breathing Rate:</strong> {breathing_rate} breaths/min</p>"
            result += f"<p>🧪 <strong>Oxygen Level:</strong> {oxygen_level}%</p>"

            warnings = []
            if oxygen_level < 95:
                warnings.append("⚠️ Low oxygen level!")
            if heart_rate < 60 or heart_rate > 100:
                warnings.append("⚠️ Heart rate out of range!")
            if bp_systolic > 140 or bp_diastolic > 90:
                warnings.append("⚠️ High blood pressure!")
            if breathing_rate < 12 or breathing_rate > 20:
                warnings.append("⚠️ Breathing rate out of range!")

            if warnings:
                result += "<h4>Warnings:</h4><ul>" + "".join(f"<li>{w}</li>" for w in warnings) + "</ul>"
            else:
                result += "<p>✅ All readings look normal.</p>"

        except ValueError:
            result = "<p>❌ Please enter valid numbers!</p>"

    return render_template("index.html", result=result)

import os
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)



