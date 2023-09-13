from flask import jsonify

class Routes:
    def __init__(self, app, repository):
        self.app = app
        self.repository = repository

        @self.app.route('/v1/student/<int:student_id>', methods=['GET'])
        def get_student_id(student_id):
            try:
                result = self.repository.get_student_by_id(student_id)
                return jsonify(result), 200
            except Exception as e:
                print(e)