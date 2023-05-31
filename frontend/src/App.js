import React, { useEffect } from 'react';
import { Routes, Route, useParams } from 'react-router-dom';

// Componentes pantallas
import CrearIssue from './views/CrearIssue/CrearIssue';
import Main from './views/Main/Main';
import ShowIssue from './views/ShowIssue/ShowIssue';
import BulkInsert from './views/BulkInsert/BulkInsert';
import Profile from './views/Profile/Profile';
import { getIdUsuario } from './vars';

function App() {
  const [idUsuario, setIdUsuario] = React.useState(null);

  function handleUsuario(id) {
    setIdUsuario(getIdUsuario());
  }

  useEffect(() => {
    setIdUsuario(getIdUsuario());
  }, []);

  const { id } = useParams(); // Obtener el parámetro de ruta ":id"

  return (
    <Routes>
      <Route
        path={`${process.env.PUBLIC_URL}/`}
        element={<Main idUsuario={idUsuario} handleUsuario={handleUsuario} />}
      />

      <Route
        path={`${process.env.PUBLIC_URL}/crearIssue`}
        element={<CrearIssue idUsuario={idUsuario} handleUsuario={handleUsuario} />}
      />

      <Route
        path={`${process.env.PUBLIC_URL}/bulkInsert`}
        element={<BulkInsert idUsuario={idUsuario} handleUsuario={handleUsuario} />}
      />

      <Route
        path={`${process.env.PUBLIC_URL}/profile`}
        element={<Profile idUsuario={idUsuario} handleUsuario={handleUsuario} />}
      />

      <Route
        path={`${process.env.PUBLIC_URL}/:id`}
        element={<ShowIssue id={id} />}
      />
    </Routes>
  );
}

export default App;
