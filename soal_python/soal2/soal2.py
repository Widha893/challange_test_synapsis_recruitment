from flask import Flask, request, jsonify

app = Flask(__name__)


def convertGrade(nilai):

    if not isinstance(nilai, int):
        return "Invalid"

    if nilai < 0 or nilai > 100:
        return "Invalid"

    if nilai >= 80:
        return "A"
    elif nilai >= 65:
        return "B"
    elif nilai >= 50:
        return "C"
    elif nilai >= 35:
        return "D"
    else:
        return "E"


def determineStatus(grade):

    if grade in ["A", "B", "C"]:
        return "lulus"
    else:
        return "tidak lulus"


@app.route("/api/<candidate_name>", methods=["POST"])
def gradeApi(candidate_name):

    data = request.get_json()

    if not data or "nilai" not in data:
        grade = "Invalid"
    else:
        try:
            nilai = int(data["nilai"])
            grade = convertGrade(nilai)
        except Exception:
            grade = "Invalid"

    status = determineStatus(grade)

    response = {
        "nama": candidate_name,
        "nilai_abjad": grade,
        "status": status
    }

    return jsonify(response)


if __name__ == "__main__":

    app.run(port=8080)
