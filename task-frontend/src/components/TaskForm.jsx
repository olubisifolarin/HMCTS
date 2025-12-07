import React, { useState } from 'react';

function TaskForm() {
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [status, setStatus] = useState('pending');
  const [dueDate, setDueDate] = useState('');
  const [createdTask, setCreatedTask] = useState(null);
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null);
    const response = await fetch('http://localhost:8000/api/tasks/', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({title, description, status, due_date: dueDate})
    });

    const data = await response.json();

    if (response.ok) {
      setCreatedTask(data);
      setTitle('');
      setDescription('');
      setStatus('pending');
      setDueDate('');
    } else {
      setError(data);
    }
  };

  return (
    <div>
      <h2>Create Task</h2>
      <form onSubmit={handleSubmit}>
        <input type="text" placeholder="Title" value={title} onChange={e=>setTitle(e.target.value)} required />
        <input type="text" placeholder="Description" value={description} onChange={e=>setDescription(e.target.value)} />
        <select value={status} onChange={e=>setStatus(e.target.value)}>
          <option value="pending">Pending</option>
          <option value="in_progress">In Progress</option>
          <option value="completed">Completed</option>
        </select>
        <input type="datetime-local" value={dueDate} onChange={e=>setDueDate(e.target.value)} required />
        <button type="submit">Create Task</button>
      </form>
      {createdTask && (
        <div>
          <h3>Task Created Successfully!</h3>
          <pre>{JSON.stringify(createdTask, null, 2)}</pre>
        </div>
      )}
      {error && <div style={{color:'red'}}>{JSON.stringify(error)}</div>}
    </div>
  );
}

export default TaskForm;
