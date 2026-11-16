from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulated data
class Event:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def to_dict(self):
        return {"id": self.id, "title": self.title}

# In-memory "database"
events = [
    Event(1, "Tech Meetup"),
    Event(2, "Python Workshop")
]
@app.route("/events/<int:event_id>", methods=["GET"])
def get_event(event_id):
    event = next((e for e in events if e.id == event_id), None)

    if not event:
        return jsonify({'error': 'Not found'}), 404

    return jsonify(event.to_dict()), 200
# TODO: Task 1 - Define the Problem
# Create a new event from JSON input
@app.route("/events", methods=["POST"])
def create_event():
    # TODO: Task 2 - Design and Develop the Code

    data = request.get_json()
    new_id = len(events) + 1
    # TODO: Task 3 - Implement the Loop and Process Each Element
    new_event = Event(id=new_id,title=data['title'])
    events.append(new_event)


    # TODO: Task 4 - Return and Handle Results
    return jsonify(new_event.to_dict()),201

# TODO: Task 1 - Define the Problem
# Update the title of an existing event
@app.route("/events/<int:event_id>", methods=["PATCH"])
def update_event(event_id):
    # TODO: Task 2 - Design and Develop the Code
    data = request.get_json()

    event = next((e for e in events if e.id == event_id),None)
    # TODO: Task 3 - Implement the Loop and Process Each Element
    if not event:
        return jsonify({'error':'Not Found'}),404
    if 'title' in data:
         event.title = data['title']

    # TODO: Task 4 - Return and Handle Results
    return jsonify(event.to_dict())

# TODO: Task 1 - Define the Problem
# Remove an event from the list
@app.route("/events/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):
    # TODO: Task 2 - Design and Develop the Code
    global events
    # TODO: Task 3 - Implement the Loop and Process Each Element
    event = next((e for e in events if e.id == event_id),None)

    if not event:
        return ('Not found'),404
    events.remove(event)
    return ('Event deleted',204)

    # TODO: Task 4 - Return and Handle Results
    

if __name__ == "__main__":
    app.run(debug=True)
