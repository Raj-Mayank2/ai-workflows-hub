import { useState } from "react";
import "./App.css";

function App() {
  const [file, setFile] = useState(null);
  const [jd, setJd] = useState("");
  const [results, setResults] = useState([]);

  const uploadResume = async () => {
    if (!file) return alert("Select file");

    const formData = new FormData();
    formData.append("file", file);

    await fetch("http://127.0.0.1:8000/resume/upload", {
      method: "POST",
      body: formData
    });

    alert("Resume Uploaded");
  };

  const rankCandidates = async () => {
    const res = await fetch(
      `http://127.0.0.1:8000/resume/rank?job_description=${encodeURIComponent(jd)}`,
      { method: "POST" }
    );

    const data = await res.json();
    setResults(data);
  };

  const exportCSV = () => {
    window.open(
      `http://127.0.0.1:8000/resume/export?job_description=${encodeURIComponent(jd)}`
    );
  };

  return (
    <div className="container">

      <header className="header">
        <h1>Smart Resume Screening System</h1>
        
      </header>

      <div className="card">
        <h3>Upload Resume</h3>
        <input type="file" onChange={e => setFile(e.target.files[0])} />
        <button onClick={uploadResume}>Upload</button>
      </div>

      <div className="card">
        <h3>Job Description</h3>
        <textarea
          rows="5"
          placeholder="Paste Job Description..."
          value={jd}
          onChange={e => setJd(e.target.value)}
        />
        <div className="btn-group">
          <button onClick={rankCandidates}>Rank Candidates</button>
          <button className="secondary" onClick={exportCSV}>Export CSV</button>
        </div>
      </div>

      <div className="card">
        <h3>Ranked Candidates</h3>
        <table>
          <thead>
            <tr>
              <th>Name</th>
              <th>Email</th>
              <th>Score</th>
              <th>Status</th>
            </tr>
          </thead>
          <tbody>
            {results.map(r => (
              <tr key={r.resume_id}>
                <td>{r.name}</td>
                <td>{r.email}</td>
                <td>{r.final_score}</td>
                <td>{r.status}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

    </div>
  );
}

export default App;
