from flask import Blueprint , request,jsonify
from models import db , Task



api = Blueprint('api',__name__)

@api.route('/tasks',methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([task.to_dict() for task in tasks]),200

@api.route('/task/<int:id>',methods =['GET'])
def get_task(id):
    task = Task.query.get_or_404(id)
    return jsonify(task.to_dict()),200


@api.route('/tasks',methods=['POST'])
def create_taks():
    data = request.get_json()

    new_task = Task(title=data['title'],description=data.get('description',''))
    db.session.add(new_task)
    db.session.commit()
    return jsonify(new_task.to_dict()),201

@api.route('/tasks/<int:id>',methods=['PUT'])

def update_task(id):
    task = Task.query.get_or_404(id)
    data = request.get_json()
    task.title = data.get('title',task.title)
    task.description = data.get('description', task.description)
    task.completed = data.get('completed',task.completed)
    db.session.commit()
    return jsonify(task.to_dict()),200
@api.route('/tasks/<int:id>' ,methods=['DELETE'])

def delete_task(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({"message" :"Task deleted"})


