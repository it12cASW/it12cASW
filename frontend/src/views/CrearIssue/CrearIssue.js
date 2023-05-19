import { useEffect } from "react"
import { styles } from "./style"
import { useState } from "react"
import { Link } from "react-router-dom";

// Componentes
import RightBar from "../RightBar/RightBar"

// Controladores
import { crearIssueCtrl } from "../../Controllers/issueCtrl"
import { getUsuariosCtrl } from "../../Controllers/usuariosCtrl"
import { getTiposCtrl } from "../../Controllers/tiposCtrl"
import { getPrioridadesCtrl } from "../../Controllers/prioridadesCtrl"
import { getSeveridadesCtrl } from "../../Controllers/severidadesCtrl"
import { getEstadosCtrl } from "../../Controllers/estadosCtrl"

export default function CrearIssue( { idUsuario, handleUsuario } ) {

    // Parametros de input
    const [usuario, setUsuario] = useState({})
    const [titulo, setTitulo] = useState("")
    const [descripcion, setDescripcion] = useState("")
    const [asignado, setAsignado] = useState("")
    const [estado, setEstado] = useState("")
    const [tipo, setTipo] = useState("")
    const [prioridad, setPrioridad] = useState("")
    const [severidad, setSeveridad] = useState("")
    const [archivo, setArchivo] = useState("")

    // Parametros de información 
    const [usuarios, setUsuarios] = useState([])
    const [tipos, setTipos] = useState([])
    const [prioridades, setPrioridades] = useState([])
    const [severidades, setSeveridades] = useState([])
    const [estados, setEstados] = useState([])

    // Parametros de vista
    const [incorrecto, setIncorrecto] = useState(null)
    const [isLoading, setIsLoading] = useState(true)

    function handleAsignado(e) {
        setAsignado(e.target.value)
    }

    function handleEstado(e) {
        setEstado(e.target.value)
    }

    function handleTipo(e) {
        setTipo(e.target.value)
    }

    function handleSeverity(e) {
        setSeveridad(e.target.value)
    }

    function handlePriority(e) {
        setPrioridad(e.target.value)
    }

    async function enviarFormulario() {
        console.log("Enviando formulario")

        var data = {
            "usuario": usuario,
            "titulo": titulo,
            "descripcion": descripcion,
            "asignado": asignado,
            "estado": estado,
            "tipo": tipo,
            "prioridad": prioridad,
            "severidad": severidad,
            "archivo": archivo,
        }

        var res = await crearIssueCtrl(data)
        setIncorrecto(res)
    }

    async function asignarVariables() {
        var usuarios_aux = await getUsuariosCtrl()
        // var tipos_aux = await getTiposCtrl()
        // var prioridades_aux = await getPrioridadesCtrl()
        // var severidades_aux = await getSeveridadesCtrl()
        // var estados_aux = await getEstadosCtrl()

        if (usuarios_aux) setUsuarios(usuarios_aux)
        // if (tipos_aux) setTipos(tipos_aux)
        // if (prioridades_aux) setPrioridades(prioridades_aux)
        // if (severidades_aux) setSeveridades(severidades_aux)
        // if (estados_aux) setEstados(estados_aux)
    }

    useEffect(() => {
        setIsLoading(true)
        asignarVariables()
        setIsLoading(false)
    }, [])


    return (
        
        <div style={ styles.mainContainer }>
            {!isLoading ? (
                <div style={{ display: "flex", flexDirection:"column" }}>
                    <div style={ styles.tituloContainer }>
                        <h1 style={ styles.tituloTexto }>New Issue</h1>
                    </div>
                    <div style={ styles.blockContainer }>
                        <div style={ styles.leftContainer }>
                            <div>
                                <input type="text" placeholder="Asunto" style={ styles.inputText } />
                            </div>
                            <div>
                                <button style={ styles.botonTag }>Tags</button>

                            </div>
                            <div>
                                <input type="textarea" placeholder="Descripción" style={ styles.inputText } />
                            </div>
                            <div>
                                <input type="file" placeholder="Titulo" style={ styles.inputFile } />
                            </div>
                        </div>
                        <div style={ styles.rightContainer }>
                            <RightBar usuarios={ usuarios } 
                                handleEstado={ handleEstado } 
                                handleAsignado={ handleAsignado } 
                                handleTipo={ handleTipo } 
                                handleSeverity={ handleSeverity } 
                                handlePriority={ handlePriority } />
                        </div>
                    </div>
                    <div>
                        <div style={ styles.botonContainer }>
                            <button style={ styles.botonCrear } onClick={ enviarFormulario }>Crear</button>
                        </div>
                        <div style={ styles.botonContainer }>
                            <button style={ styles.botonCrear }>
                                <Link to="/">Volver</Link>
                            </button>
                        </div>
                    </div>
                    
                    {incorrecto == true && <div style={ styles.incorrecto }>No se ha podido crear la issue</div>}
                    {incorrecto == false && <div style={ styles.incorrecto }>Issue creada correctamente</div>}
                    
                </div>
            ) : (
                <div>
                    <h1>Cargando...</h1>
                </div>
            )}
        </div>
    )
}