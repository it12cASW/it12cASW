import { useEffect } from "react"
import React from "react"
import { useRef } from "react"

// Funciones
import { getAllUsers, getIdUsuario } from "../vars";
import { editarIssueCtrl } from "../Controllers/issueCtrl";
import { setAsociadoCtrl } from "../Controllers/issueCtrl";
import { deleteAsociadoCtrl } from "../Controllers/issueCtrl";
import { deleteAsignadoCtrl } from "../Controllers/issueCtrl";  
import { setAsignadoCtrl } from "../Controllers/issueCtrl";  
import { deleteDeadlineCtrl } from "../Controllers/issueCtrl";
import { setDeadlineCtrl } from "../Controllers/issueCtrl";

// Componentes
import SwitchSelector from "react-switch-selector";
import Switch from 'react-switch';


export default function InfoIssue({ issue, setIssue }) {
    
    // Variables
    const [usuarios, setUsuarios] = React.useState(null);

    // Editar issue
    const [asunto, setAsunto] = React.useState(issue.asunto);
    const [descripcion, setDescripcion] = React.useState(issue.descripcion);
    const [vigilant, setVigilant] = React.useState(null);
    const [reason_blocked, setReasonBlocked] = React.useState(issue.reason_blocked);
    const [prioridad, setPrioridad] = React.useState(issue.prioridad);
    const [estado, setEstado] = React.useState(issue.estado);

    const [blocked, setBlocked] = React.useState(false);

    const asunto_ref = useRef(null)
    const descripcion_ref = useRef(null)
    const asociat_ref = useRef(null)
    const asignado_ref = useRef(null)
    const bloqued_ref = useRef(null)
    const reason_bloqued_ref = useRef(null)
    const deadline_ref = useRef(null)
    const prioridad_ref = useRef(null)
    const estado_ref = useRef(null)


    ////////// FUNCIONES HANDLE //////////
    function handleAsunto(e) {
        setAsunto(e.target.value);
    }

    function handleDescripcion(e) {
        setDescripcion(e.target.value);
    }

    async function handleAsociado(e) {
        var deleted = await deleteAsociadoCtrl(issue.id);
        var res = await setAsociadoCtrl(issue.id, e.target.value);
        if(res) {
            setIssue();
        }
    }

    async function handleAsignado(e) {

        var deleted = await deleteAsignadoCtrl(issue.id);
        var res = await setAsignadoCtrl(issue.id, e.target.value);

        if(res) {
            setIssue();
        }
    }

    function lock() {
        setBlocked(true);
    }   

    function unlock() {
        setBlocked(false);
    }

    async function handleDeadline(e) {
        
        var deleted = await deleteDeadlineCtrl(issue.id);
        var res = await setDeadlineCtrl(issue.id, e.target.value);

        setIssue();
    }

    function handlePrioridad(e) {
        setPrioridad(e.target.value);
    }

    function handleEstado(e) {
        setEstado(e.target.value);
    }
    ////////// FUNCIONES HANDLE //////////

    async function editarIssueAPI() {
        // Leo los valores de 
        var asunto_aux = asunto_ref.current.value;
        var descripcion_aux = descripcion_ref.current.value;
    
        var asociat_aux = null;
        if(issue.associat) asociat_aux = issue.associat.id;
        else {
            if(asociat_ref.current.value == "Ninguno") asociat_aux = null;
            else asociat_aux = asociat_ref.current.value;
        }

        var asignado_aux = null;
        if(issue.asignada) asignado_aux = issue.asignada.id;
        else {
            if(asignado_ref.current.value == "Ninguno") asignado_aux = null;
            else asignado_aux = asignado_ref.current.value;
        }

        var blocked_aux = blocked;

        var reason_blocked_aux = null;
        console.log("reason_blocked_ref.current.value: " + reason_bloqued_ref.current.value)
        if(reason_bloqued_ref.current.value) reason_blocked_aux = reason_bloqued_ref.current.value;
        else reason_blocked_aux = issue.reason_blocked;

        var deadline_aux = null;
        if(deadline_ref.current.value) deadline_aux = deadline_ref.current.value;
        else deadline_aux = issue.deadline;

        var prioridad_aux = prioridad_ref.current.value;
        var estado_aux = estado_ref.current.value;

        var data = {
            "id_user": getIdUsuario(),
            "asunto": asunto_aux,
            "descripcion": descripcion_aux,
            "asociado": asociat_aux,
            "asignado": asignado_aux,
            "blocked": blocked_aux,
            "reason_blocked": reason_blocked_aux,
            "deadline": deadline_aux,
            "prioridad": prioridad_aux,
            "status":   estado_aux,  
        };

        var res = await editarIssueCtrl(issue.id ,data);
        setIssue();
    }

    useEffect(() => {   

        async function getUsuariosAPI() {
            var usuarios_aux = await getAllUsers();
            setUsuarios(usuarios_aux);
        }

        getUsuariosAPI();
        if(issue.blocked) setBlocked(issue.blocked);
        console.log("Vuelvo a cargar con: " + issue.deadline);

    }, [issue])

    return (
        <div style={ styles.contenedor }>
            <div style={ styles.targeta }>
                <p>Asunto:</p>
                <input onChange={ handleAsunto } style={ styles.input } type="text" placeholder={issue.asunto} defaultValue={ issue.asunto } ref={ asunto_ref } />
            </div>
            <div style={ styles.targeta }>
                <p>Descripción:</p>
                <input onChange={ handleDescripcion } style={ styles.inputArea } type="textarea" multiple={true} placeholder={issue.descripcion} defaultValue={ issue.descripcion } ref={ descripcion_ref } />
            </div>
            <div style={ styles.targetaCreador }>
                <p>Creador: {issue.creador.username}</p>
            </div>

            {/* ASOCIADO --> Por defecto el 'none', sino pongo el que venia */}
            <div style={ styles.targeta }>
                {issue.associat && <p>Asociado: { issue.associat.username }</p>}
                {!issue.associat && <p>Asociado: Ninguno</p>}
                <select style={styles.select} ref={ asociat_ref } defaultValue={ issue.associat } onChange={handleAsociado}>
                    <option value={null}>Ninguno</option>
                    {usuarios && usuarios.map((usuario) => (
                        <option value={usuario.id} >{usuario.username}</option>
                    ))}
                </select>
            </div>

            {/* ASIGNADO --> Por defecto el 'none', sino pongo el que venia */}
            <div style={ styles.targeta }>
                {issue.asignada && <p>Asignado: {issue.asignada.username}</p>}
                {!issue.asignada && <p>Asignado: Ninguno</p>}
                <select style={ styles.select } ref={ asignado_ref } defaultValue={ issue.asignado } onChange={ handleAsignado } >
                    <option value={null} >Ninguno</option>
                    {usuarios && usuarios.map((usuario) => (
                        <option value={usuario.id}>{usuario.username}</option>
                    ))}
                </select>
            </div>
            {/* Recorre los usuarios */}
            <div>
                {usuarios && usuarios.map((usuario) => (
                    <div>
                        
                    </div>
                ))}
            </div>
            {/* BLOQUEO */}
            <div style={ styles.targeta }>
                <div style={{ display:"flex", flexDirection:"row", alignContent:"center", alignContent:"center" }}>
                    {!blocked && <button onClick={ lock } style={ styles.bloqueado }>Bloquear</button>}
                    {blocked && <button onClick={ unlock } style={ styles.desbloqueado }>Desbloquear</button>}
                    <p>Bloqueada</p>
                </div>
            
                <input type="text" ref={ reason_bloqued_ref } onChange={setReasonBlocked} style={ styles.input } defaultValue={ issue.reason_blocked } placeholder={ issue.reason_blocked } />
            </div>
            {/* DEADLINE */}
            <div style={ styles.targeta }>
                <p>Deadline: { issue.deadline }</p>
                <input ref={ deadline_ref } onChange={handleDeadline} type="date" defaultValue={ issue.deadline } />
            </div>
            {/* PRIORIDAD */}
            <div style={ styles.targeta }>
                { issue.prioridad && <p>Prioridad: { issue.prioridad }</p> }
                {!issue.prioridad && <p>Prioridad: Ninguna</p> }
                <select ref={ prioridad_ref } onChange={handlePrioridad}>
                    <option value="low">Low</option>
                    <option value="normal" defaultValue>Normal</option>
                    <option value="high">High</option>
                </select>
            </div>
            {/* ESTADO */}
            <div style={ styles.targeta }>
                {issue.status && <p>Estado: { issue.status }</p>}
                {!issue.status && <p>Estado: Ninguno</p>}
                <select ref={ estado_ref } onChange={ handleEstado } name="estado" id="estado" style={ styles.select }>
                    <option value="new" defaultValue>New</option>
                    <option value="progress">In progress</option>
                    <option value="test">Ready for test</option>
                    <option value="closed">Closed</option>
                    <option value="info">Needs Info</option>
                    <option value="rejected">Rejected</option>
                    <option value="postponed">Postponed</option>
                </select>
            </div>
            <div>
                <button onClick={ editarIssueAPI }>Editar</button>
            </div>
        </div>
    )
}

const styles = {
    contenedor: {
        display: 'flex',
        flexDirection: 'column',
        width: '100%',
        alignItems: 'center',
    },
    targeta: {
        display: 'flex',
        flexDirection: 'column',
        padding: '5px',
        backgroundColor: '#DBDBDB',
        width: '80%',
        borderRadius: '5px',
        margin: '5px',
    },
    targetaCreador: {
        display: 'flex',
        flexDirection: 'column',
        backgroundColor: '#DBDBDB',
        width: '80%',
        borderRadius: '5px',
        padding: '5px',
    },
    input: {
        padding: '5px',
        borderRadius: '10px',
        border: "none",
        backgroundColor: 'white',
    },
    inputArea: {
        padding: '5px',
        height: '50px',
        borderRadius: '10px',
        border: "none",
        backgroundColor: 'white',
    },
    select: {
        padding: '5px',
        width: '100%',
        height: '10px',
    }
}