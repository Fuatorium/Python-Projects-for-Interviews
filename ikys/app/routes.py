from flask import Blueprint, request, jsonify, render_template
from . import db
from .models import Employee, Candidate
from datetime import datetime

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/employees', methods=['GET', 'POST'])
def employees():
    if request.method == 'POST':
        data = request.get_json()
        new_employee = Employee(
            name=data['name'],
            position=data['position'],
            salary=data['salary'],
            performance_score=data.get('performance_score')
        )
        db.session.add(new_employee)
        db.session.commit()
        return jsonify({'message': 'Employee added successfully!'}), 201
    else:
        if request.headers.get('Accept') == 'application/json':
            employees = Employee.query.all()
            return jsonify([e.serialize() for e in employees])
        else:
            return render_template('employees.html')

@bp.route('/employees/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def employee_detail(id):
    employee = Employee.query.get_or_404(id)
    if request.method == 'GET':
        return jsonify(employee.serialize())
    elif request.method == 'PUT':
        data = request.get_json()
        employee.name = data['name']
        employee.position = data['position']
        employee.salary = data['salary']
        employee.performance_score = data.get('performance_score')
        db.session.commit()
        return jsonify({'message': 'Employee updated successfully!'})
    elif request.method == 'DELETE':
        db.session.delete(employee)
        db.session.commit()
        return jsonify({'message': 'Employee deleted successfully!'})

@bp.route('/candidates', methods=['GET', 'POST'])
def candidates():
    if request.method == 'POST':
        data = request.get_json()
        interview_date = data.get('interview_date')
        if interview_date:
            interview_date = datetime.strptime(interview_date, '%Y-%m-%d')

        new_candidate = Candidate(
            name=data['name'],
            position_applied=data['position_applied'],
            interview_date=interview_date
        )
        db.session.add(new_candidate)
        db.session.commit()
        return jsonify({'message': 'Candidate added successfully!'}), 201
    else:
        if request.headers.get('Accept') == 'application/json':
            candidates = Candidate.query.all()
            return jsonify([c.serialize() for c in candidates])
        else:
            return render_template('candidates.html')

@bp.route('/candidates/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def candidate_detail(id):
    candidate = Candidate.query.get_or_404(id)
    if request.method == 'GET':
        return jsonify(candidate.serialize())
    elif request.method == 'PUT':
        data = request.get_json()
        interview_date = data.get('interview_date')
        if interview_date:
            interview_date = datetime.strptime(interview_date, '%Y-%m-%d')

        candidate.name = data['name']
        candidate.position_applied = data['position_applied']
        candidate.interview_date = interview_date
        db.session.commit()
        return jsonify({'message': 'Candidate updated successfully!'})
    elif request.method == 'DELETE':
        db.session.delete(candidate)
        db.session.commit()
        return jsonify({'message': 'Candidate deleted successfully!'})
