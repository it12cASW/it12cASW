import React, { useState } from 'react';
import { obtenerIssuesFiltrados } from '../Controllers/issueCtrl';
import { getUsuariosCtrl } from '../Controllers/usuariosCtrl';
import { styles } from '../views/Main/style';
import { FaCircle } from "react-icons/fa";

function FormularioFiltros({ sharedIssues, setSharedIssues, sharedUrl, setSharedUrl }) {
  const [filtrosSeleccionados, setFiltrosSeleccionados] = useState([]);
  const [estadosSeleccionados, setEstadosSeleccionados] = useState('');
  const [usuarioAsignado, setUsuarioAsignado] = useState('');
  const [prioridadSeleccionada, setPrioridadSeleccionada] = useState('');
  const [usuarioCreador, setUsuarioCreador] = useState('');
  const [users, setUsers] = useState([]);

  const handleFiltroChange = (event) => {
    const filtro = event.target.value;
    if (filtrosSeleccionados.includes(filtro)) {
      setFiltrosSeleccionados(filtrosSeleccionados.filter((f) => f !== filtro));
    } else {
      setFiltrosSeleccionados([...filtrosSeleccionados, filtro]);
    }
  };

  const handleEstadoChange = (event) => {
    const estado = event.target.value;
    setEstadosSeleccionados(estado);
  };

  const handleUsuarioAsignadoChange = (event) => {
    setUsuarioAsignado(event.target.value);
  };

  const handlePrioridadChange = (event) => {
    setPrioridadSeleccionada(event.target.value);
  };

  const handleUsuarioCreadorChange = (event) => {
    setUsuarioCreador(event.target.value);
  };

  const handleFiltroSubmit = async (event) => {
    event.preventDefault();
    const issuesFiltradas = await obtenerIssuesFiltrados(
      filtrosSeleccionados,
      estadosSeleccionados,
      usuarioAsignado,
      prioridadSeleccionada,
      usuarioCreador
    );
    await setSharedIssues(issuesFiltradas[0]);
    await setSharedUrl(issuesFiltradas[1]);
  };

  React.useEffect(() => {
    console.log(sharedIssues);
  }, [sharedIssues]);

  React.useEffect(() => {
    const fetchData = async () => {
      const aux_users = await getUsuariosCtrl();
      await setUsers(aux_users);
    };
  
    fetchData();
  }, []);
  

  return (
    <div style={styles.formContainer}>
      <form id="filtres" onSubmit={handleFiltroSubmit}>
        <label style={{ fontWeight: 'bold' }} htmlFor="filtro">
          Filtrar issues por:
        </label>
        <div className="filtro-options" style={styles.filterOptions}>
          <div style={styles.filtersContainer}>
            <div className="checkbox-style" style={styles.checkboxContainer}>
              <input
                type="checkbox"
                id="status"
                name="filtro"
                value="status"
                checked={filtrosSeleccionados.includes('status')}
                onChange={handleFiltroChange}
              />
              <label htmlFor="status">Estado</label>
            </div>
            {filtrosSeleccionados.includes('status') && (
              <div>
                <div>
                  <input
                    type="radio"
                    id="new"
                    name="estados"
                    value="new"
                    checked={estadosSeleccionados === 'new'}
                    onChange={handleEstadoChange}
                  />
                  <label htmlFor="new">
                    <FaCircle style={{ color: 'violet', marginRight: '5px' }} /> New
                  </label>
                </div>
                <div>
                  <input
                    type="radio"
                    id="progress"
                    name="estados"
                    value="progress"
                    checked={estadosSeleccionados === 'progress'}
                    onChange={handleEstadoChange}
                  />
                  <label htmlFor="progress">
                    <FaCircle style={{ color: 'blue', marginRight: '5px' }} /> Progress
                  </label>
                </div>
                <div>
                  <input
                    type="radio"
                    id="test"
                    name="estados"
                    value="test"
                    checked={estadosSeleccionados === 'test'}
                    onChange={handleEstadoChange}
                  />
                  <label htmlFor="test" >
                    <FaCircle style={{ color: 'yellow', marginRight: '5px' }} /> Test
                  </label>
                </div>
                <div>
                  <input
                    type="radio"
                    id="closed"
                    name="estados"
                    value="closed"
                    checked={estadosSeleccionados === 'closed'}
                    onChange={handleEstadoChange}
                  />
                  <label htmlFor="closed" >
                    <FaCircle style={{ color: 'green', marginRight: '5px' }} /> Closed
                  </label>
                </div>
                <div>
                  <input
                    type="radio"
                    id="info"
                    name="estados"
                    value="info"
                    checked={estadosSeleccionados === 'info'}
                    onChange={handleEstadoChange}
                  />
                  <label htmlFor="info" >
                    <FaCircle style={{ color: 'red', marginRight: '5px' }} /> Info
                  </label>
                </div>
                <div>
                  <input
                    type="radio"
                    id="rejected"
                    name="estados"
                    value="rejected"
                    checked={estadosSeleccionados === 'rejected'}
                    onChange={handleEstadoChange}
                  />
                  <label htmlFor="rejected" >
                    <FaCircle style={{ color: 'gray', marginRight: '5px' }} /> Rejected
                  </label>
                </div>
                <div>
                  <input
                    type="radio"
                    id="posponed"
                    name="estados"
                    value="posponed"
                    checked={estadosSeleccionados === 'posponed'}
                    onChange={handleEstadoChange}
                  />
                  <label htmlFor="posponed" >
                    <FaCircle style={{ color: 'blue', marginRight: '5px' }} /> Posponed
                  </label>
                </div>
              </div>
            )}
          </div>
          <div style={styles.filtersContainer}>
            <div className="checkbox-style" style={styles.checkboxContainer}>
              <input
                type="checkbox"
                id="assignee"
                name="filtro"
                value="assignee"
                checked={filtrosSeleccionados.includes('assignee')}
                onChange={handleFiltroChange}
              />
              <label htmlFor="assignee">Asignado a</label>
            </div>
            {filtrosSeleccionados.includes('assignee') && (
              <div>
                {users.map((user) => (
                  <div key={user.id}>
                    <input
                      type="radio"
                      id={`assignee-${user.id}`}
                      name="asignados"
                      value={user.username}
                      checked={usuarioAsignado === user.username}
                      onChange={handleUsuarioAsignadoChange}
                    />
                    <label htmlFor={`assignee-${user.id}`}>{user.username}</label>
                  </div>
                ))}
              </div>
            )}
          </div>
          <div style={styles.filtersContainer}>
            <div className="checkbox-style" style={styles.checkboxContainer}>
              <input
                type="checkbox"
                id="priority"
                name="filtro"
                value="priority"
                checked={filtrosSeleccionados.includes('priority')}
                onChange={handleFiltroChange}
              />
              <label htmlFor="priority">Prioridad</label>
            </div>
            {filtrosSeleccionados.includes('priority') && (
              <div style={styles.radioContainer}>
                <div>
                  <input
                    type="radio"
                    id="high"
                    name="prioridades"
                    value="high"
                    checked={prioridadSeleccionada === 'high'}
                    onChange={handlePrioridadChange}
                  />
                  <label htmlFor="high" >
                    <FaCircle style={{ color: 'red', marginRight: '5px' }} /> High
                  </label>
                </div>
                <div>
                  <input
                    type="radio"
                    id="normal"
                    name="prioridades"
                    value="normal"
                    checked={prioridadSeleccionada === 'normal'}
                    onChange={handlePrioridadChange}
                  />
                  <label htmlFor="normal" >
                    <FaCircle style={{ color: 'orange', marginRight: '5px' }} /> Normal
                  </label>
                </div>
                <div>
                  <input
                    type="radio"
                    id="low"
                    name="prioridades"
                    value="low"
                    checked={prioridadSeleccionada === 'low'}
                    onChange={handlePrioridadChange}
                  />
                  <label htmlFor="low" >
                    <FaCircle style={{ color: 'green', marginRight: '5px' }} /> Low
                  </label>
                </div>
              </div>
            )}
          </div>
          <div style={styles.filtersContainer}>
            <div className="checkbox-style" style={styles.checkboxContainer}>
              <input
                type="checkbox"
                id="created_by"
                name="filtro"
                value="created_by"
                checked={filtrosSeleccionados.includes('created_by')}
                onChange={handleFiltroChange}
              />
              <label htmlFor="created_by">Creador</label>
            </div>
            {filtrosSeleccionados.includes('created_by') && (
              <div>
                {users.map((user) => (
                  <div key={user.id}>
                    <input
                      type="radio"
                      id={`created_by-${user.id}`}
                      name="creado_por"
                      value={user.username}
                      checked={usuarioCreador === user.username}
                      onChange={handleUsuarioCreadorChange}
                    />
                    <label htmlFor={`created_by-${user.id}`}>{user.username}</label>
                  </div>
                ))}
              </div>
            )}
          </div>
        </div>
        <input id="botonFiltro" type="submit" value="Filtrar" />
      </form>
    </div>
  );
}

export default FormularioFiltros;
