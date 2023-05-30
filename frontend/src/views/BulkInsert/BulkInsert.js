import { useEffect } from "react"
import { styles } from "./style"
import { useState } from "react"
import { Link } from "react-router-dom";

// Componentes

// Controladores
import { bulkInsertCtrl } from "../../Controllers/issueCtrl"
import { getUsuariosCtrl } from "../../Controllers/usuariosCtrl"

export default function BulkInsert({ idUsuario, handleUsuario } ) {

    // Parametros de input

    const [asuntos, setAsuntos] = useState("")

    const [usuarios, setUsuarios] = useState([])



    // Parametros de vista
    const [incorrecto, setIncorrecto] = useState(null)
    const [isLoading, setIsLoading] = useState(true)

    function handleAsuntos(e) {
        setAsuntos(e.target.value)
    }


    async function enviarFormulario() {
        console.log("Enviando formulario")


        var data = {
            "asuntos": asuntos.split('\n')
        }

        var res = await bulkInsertCtrl(idUsuario, data)
        setIncorrecto(res)
    }

    async function asignarVariables() {
        var usuarios_aux = await getUsuariosCtrl()
        if (usuarios_aux) setUsuarios(usuarios_aux)

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
                        <h1 style={ styles.tituloTexto }>Bulk Insert Issues</h1>
                    </div>
                    <div style={ styles.blockContainer }>
                        <div style={ styles.leftContainer }>

                            <div >
                                <textarea rows="31" placeholder="Asuntos ; uno por fila" onChange={ handleAsuntos } style={ styles.textarea }/>
                            </div>

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
