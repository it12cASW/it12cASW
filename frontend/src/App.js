
import React, { useEffect } from 'react';
import { Routes, Route } from 'react-router-dom';

// Componentes pantallas
import CrearIssue from './views/CrearIssue/CrearIssue';
import Main from './views/Main/Main';
import ShowIssue from './views/ShowIssue/ShowIssue';

// token: acbbf2e3ca3929ccac31c8ccc572a2b783aa876f


function App() {

  const [idUsuario, setIdUsuario] = React.useState(null);

  function handleUsuario(id) {

    setIdUsuario(id.target.value);
  }

  useEffect(() => {
    setIdUsuario(0);
  }, []);


  return (
    <Routes>
      {/* <Route path="/" element={
        <Panel idUsuario={ idUsuario } 
          handleUsuario={ handleUsuario } 
        />} />   */}

      <Route path="/" element={ 
        <Main idUsuario={ idUsuario } 
          handleUsuario={ handleUsuario }
      /> } />

      <Route path="/crearIssue" element={
        <CrearIssue idUsuario={ idUsuario } 
          handleUsuario={ handleUsuario }
      />} />  

      <Route path="/:id" element={ 
        <ShowIssue
      /> } />

    </Routes>
  );
}

export default App;
