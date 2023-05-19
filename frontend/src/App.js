
import React from 'react';
import { Routes, Route } from 'react-router-dom';

// Componentes pantallas
import Panel from './views/Panel/Panel';
import CrearIssue from './views/CrearIssue/CrearIssue';
import Main from './views/Main/Main';


function App() {

  const [idUsuario, setIdUsuario] = React.useState(null);

  function handleUsuario(id) {
    console.log("ID: " + id);
    setIdUsuario(id);
  }


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

    </Routes>
  );
}

export default App;
