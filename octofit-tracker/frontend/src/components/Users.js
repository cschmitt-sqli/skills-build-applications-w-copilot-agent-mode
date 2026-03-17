import React, { useEffect, useState } from 'react';

const Users = () => {
  const [users, setUsers] = useState([]);
  const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/users/`;

  useEffect(() => {
    console.log('Fetching users from:', apiUrl);
    fetch(apiUrl)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setUsers(results);
        console.log('Fetched users:', results);
      })
      .catch(err => console.error('Error fetching users:', err));
  }, [apiUrl]);

  return (
    <div className="container mt-4">
      <h2 className="mb-4">Users</h2>
      <div className="card">
        <div className="card-body">
          <table className="table table-striped table-hover">
            <thead>
              <tr>
                <th>Username</th>
                <th>Email</th>
                <th>Team</th>
                <th>Action</th>
              </tr>
            </thead>
            <tbody>
              {users.map((user, idx) => (
                <tr key={idx}>
                  <td>{user.username}</td>
                  <td>{user.email}</td>
                  <td>{user.team_name}</td>
                  <td>
                    <button className="btn btn-primary btn-sm" onClick={() => alert(JSON.stringify(user, null, 2))}>Details</button>
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

export default Users;
