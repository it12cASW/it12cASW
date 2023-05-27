import React, { useState } from 'react';
import {obtenerIssuesFiltrados} from '../../Controllers/issueCtrl';

function FormularioFiltros({ sharedIssues, setSharedIssues }) {
  const [filtrosSeleccionados, setFiltrosSeleccionados] = useState([]);
  const [estadosSeleccionados, setEstadosSeleccionados] = useState([]);
  const [usuarioAsignado, setUsuarioAsignado] = useState('');
  const [prioridadSeleccionada, setPrioridadSeleccionada] = useState('');
  const [usuarioCreador, setUsuarioCreador] = useState('');

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
    if (estadosSeleccionados.includes(estado)) {
      setEstadosSeleccionados(estadosSeleccionados.filter((e) => e !== estado));
    } else {
      setEstadosSeleccionados([...estadosSeleccionados, estado]);
    }
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
    const issuesFiltradas = await obtenerIssuesFiltrados(filtrosSeleccionados, estadosSeleccionados, usuarioAsignado, prioridadSeleccionada, usuarioCreador);
    await setSharedIssues(issuesFiltradas);
  };
  React.useEffect(() => {
    console.log(sharedIssues);
  }, [sharedIssues]);
  
  return (
    <div>
        <form id="filtres" onSubmit={handleFiltroSubmit}>
        <label style={{ fontWeight: 'bold' }} htmlFor="filtro">
            Filtrar issues por:
        </label>
        <div className="filtro-options">
            <div>
            <input
                type="checkbox"
                id="status"
                name="filtro"
                value="status"
                checked={filtrosSeleccionados.includes('status')}
                onChange={handleFiltroChange}
            />
            <label htmlFor="status">Estado</label>
            {filtrosSeleccionados.includes('status') && (
                <div>
                <select
                    id="status-select"
                    name="status"
                    value={estadosSeleccionados}
                    onChange={handleEstadoChange}
                    multiple
                >
                    {/* Renderizar las opciones dinámicamente en React */}
                </select>
                </div>
            )}
            </div>
            <div>
            <input
                type="checkbox"
                id="assignee"
                name="filtro"
                value="assignee"
                checked={filtrosSeleccionados.includes('assignee')}
                onChange={handleFiltroChange}
            />
            <label htmlFor="assignee">Asignado a</label>
            {filtrosSeleccionados.includes('assignee') && (
                <div>
                <input
                    type="text"
                    id="assignee-select"
                    name="asignados"
                    value={usuarioAsignado}
                    onChange={handleUsuarioAsignadoChange}
                />
                </div>
            )}
            </div>
            <div>
            <input
                type="checkbox"
                id="priority"
                name="filtro"
                value="priority"
                checked={filtrosSeleccionados.includes('priority')}
                onChange={handleFiltroChange}
            />
            <label htmlFor="priority">Prioridad</label>
            {filtrosSeleccionados.includes('priority') && (
                <div>
                <select
                    id="priority-select"
                    name="prioridades"
                    value={prioridadSeleccionada}
                    onChange={handlePrioridadChange}
                >
                    {/* Renderizar las opciones dinámicamente en React */}
                </select>
                </div>
            )}
            </div>
            <div>
            <input
                type="checkbox"
                id="created_by"
                name="filtro"
                value="created_by"
                checked={filtrosSeleccionados.includes('created_by')}
                onChange={handleFiltroChange}
            />
            <label htmlFor="created_by">Creador</label>
            {filtrosSeleccionados.includes('created_by') && (
                <div>
                <input
                    type="text"
                    id="created_by-select"
                    name="creado_por"
                    value={usuarioCreador}
                    onChange={handleUsuarioCreadorChange}
                />
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
