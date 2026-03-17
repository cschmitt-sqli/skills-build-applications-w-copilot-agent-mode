import React, { useEffect, useState } from 'react';

const Workouts = () => {
  const [workouts, setWorkouts] = useState([]);
  const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/workouts/`;

  useEffect(() => {
    console.log('Fetching workouts from:', apiUrl);
    fetch(apiUrl)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setWorkouts(results);
        console.log('Fetched workouts:', results);
      })
      .catch(err => console.error('Error fetching workouts:', err));
  }, [apiUrl]);

  return (
    <div className="container mt-4">
      <h2 className="mb-4">Workouts</h2>
      <div className="card">
        <div className="card-body">
          <table className="table table-striped table-hover">
            <thead>
              <tr>
                <th>Name</th>
                <th>Description</th>
                <th>Team</th>
                <th>Action</th>
              </tr>
            </thead>
            <tbody>
              {workouts.map((workout, idx) => (
                <tr key={idx}>
                  <td>{workout.name}</td>
                  <td>{workout.description}</td>
                  <td>{workout.suggested_for_team_name}</td>
                  <td>
                    <button className="btn btn-primary btn-sm" onClick={() => alert(JSON.stringify(workout, null, 2))}>Details</button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};

export default Workouts;
