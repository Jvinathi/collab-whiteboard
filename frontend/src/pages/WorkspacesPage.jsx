import { useAuth } from '../context/AuthContext';

export default function WorkspacesPage() {
  const { user, logout } = useAuth();

  return (
    <div style={{ maxWidth: 600, margin: '80px auto' }}>
      <h2>Welcome, {user?.username}</h2>
      <p>Workspaces will go here (next step).</p>
      <button onClick={logout}>Log out</button>
    </div>
  );
}