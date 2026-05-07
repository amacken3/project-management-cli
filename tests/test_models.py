from models.task import Task
    
def test_task_stores_attributes():
    task = Task("Finish README", "Write setup instructions", "2026-05-08")
    
    assert task.title == "Finish README"
    assert task.description == "Write setup instructions"
    assert task.due_date == "2026-05-08"

def test_task_starts_incomplete():
    task = Task("Finish README", "Write setup instructions", "2026-05-08")

    assert task.completed == False

def test_task_can_be_marked_complete():
    task = Task("Finish README", "Write setup instructions", "2026-05-08")

    task.mark_complete()

    assert task.completed == True