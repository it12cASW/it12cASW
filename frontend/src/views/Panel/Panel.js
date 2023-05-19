import React from "react";
import Main from "../Main/Main";
import CrearIssue from "../CrearIssue/CrearIssue";

export default function Panel({ idUsuario, handleUsuario }) {
  
  const [crearIssue, setCrearIssue] = React.useState(false);

  return (
    <div>
      <Main idUsuario={ idUsuario }
        handleUsuario={ handleUsuario }
      />
    </div>
  )
}

