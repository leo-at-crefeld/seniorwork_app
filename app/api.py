"""Senior Work App API"""
import flask as fl
import json

app = fl.Flask(__name__, template_folder='jinja_templates/')

with open('user-data/student_trackers.json') as f:
	student_profiles = json.load(f)

@app.route('/student/<student_name>/tracker/')
def student_tracker(student_name):
	try:
		student = student_profiles[student_name]
		template_context = dict(student=student, student_name=student_name)
		return fl.render_template('tracker_template.html', **template_context)
	except KeyError:
		fl.abort(404, f'Student {student_name} not found')

if __name__ == "__main__":
	app.run(debug=True)
