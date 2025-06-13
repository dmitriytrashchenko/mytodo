import React, { useEffect, useState } from "react";
import axios from "axios";

const TaskPage = () => {
  const [tasks, setTasks] = useState([]);
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [tags, setTags] = useState("");
  const [priority, setPriority] = useState("M");
  const [deadline, setDeadline] = useState("");
  const token = localStorage.getItem("token");

  useEffect(() => {
    if (!token) return;
    axios.get("http://127.0.0.1:8000/api/tasks/", {
      headers: { Authorization: `Bearer ${token}` }
    })
    .then(res => setTasks(res.data))
    .catch(() => alert("Ошибка загрузки задач"));
  }, [token]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await axios.post("http://127.0.0.1:8000/api/tasks/", {
        title, description, tags, priority, deadline, completed: false, order: tasks.length + 1
      }, {
        headers: { Authorization: `Bearer ${token}` }
      });
      setTasks([...tasks, res.data]);
      setTitle(""); setDescription(""); setTags(""); setPriority("M"); setDeadline("");
    } catch {
      alert("Ошибка при добавлении задачи");
    }
  };

  return (
    <div style={{ maxWidth: 600, margin: "50px auto" }}>
      <h1>Задачи</h1>
      {tasks.length === 0 ? <p>Задач пока нет.</p> : (
        <ul>
          {tasks.map(task => (
            <li key={task.id}>
              <b>{task.title}</b> — приоритет: {task.priority}, дедлайн: {new Date(task.deadline).toLocaleString()}
            </li>
          ))}
        </ul>
      )}

      <h2>Добавить новую задачу</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <input 
            type="text" placeholder="Название задачи" required 
            value={title} onChange={e => setTitle(e.target.value)} 
          />
        </div>
        <div>
          <textarea 
            placeholder="Описание задачи" 
            value={description} onChange={e => setDescription(e.target.value)} 
          />
        </div>
        <div>
          <input 
            type="text" placeholder="Теги через запятую" 
            value={tags} onChange={e => setTags(e.target.value)} 
          />
        </div>
        <div>
          <select value={priority} onChange={e => setPriority(e.target.value)}>
            <option value="L">Низкий</option>
            <option value="M">Средний</option>
            <option value="H">Высокий</option>
          </select>
        </div>
        <div>
          <input 
            type="datetime-local" 
            value={deadline} onChange={e => setDeadline(e.target.value)} 
          />
        </div>
        <button type="submit">Добавить задачу</button>
      </form>
    </div>
  );
};

export default TaskPage;
