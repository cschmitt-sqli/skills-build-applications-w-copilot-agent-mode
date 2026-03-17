import React, { useEffect, useState } from 'react';

const Activities = () => {
  const [activities, setActivities] = useState([]);
  const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/activities/`;

  useEffect(() => {
    console.log('Fetching activities from:', apiUrl);
    fetch(apiUrl)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setActivities(results);
        console.log('Fetched activities:', results);
      })
      .catch(err => console.error('Error fetching activities:', err));
  }, [apiUrl]);

  return (
    <div className="container mt-4">
      <h2 className="mb-4">Activities</h2>
      <div className="card">
        <div className="card-body">
          <table className="table table-striped table-hover">
            <thead>
              <tr>
                <th>Username</th>
                <th>Type</th>
                <th>Duration (min)</th>
                <th>Calories (kcal)</th>
                <th>Action</th>
              </tr>
            </thead>
            <tbody>
              {activities.map((activity, idx) => (
                <tr key={idx}>
                  <td>{activity.username}</td>
                  <td>{activity.type}</td>
                  <td>{activity.duration}</td>
                  <td>{activity.calories}</td>
                  <td>
                    <button className="btn btn-primary btn-sm" onClick={() => alert(JSON.stringify(activity, null, 2))}>Details</button>
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

export default Activities;
