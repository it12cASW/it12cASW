import React from 'react';
import { styles } from "./style"


export default function RightBar({ usuarios,
    handleEstado,
    handleAsignado,
    handleTipo,
    handleSeverity,
    handlePriority
    }) {

    return (
        <div>
            <div style={ styles.contenedorCampos }>
                <div>
                    <p>Estado de la issue: </p>
                    <select name="estado" id="estado" style={ styles.select }  onChange={ handleEstado }>
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
                    <p>Usuario asignado:</p>
                    <select name="asignado" id="asignado" style={ styles.select } onChange={ handleAsignado }>
                        <option value="null" defaultValue>Nadie</option>
                        { usuarios.map( usuario => 
                            <option value={ usuario.id }>{ usuario.username }</option> 
                        ) }
                    </select>
                </div>
                <div>
                    <div>
                        <p>Tipo de la issue:</p>
                        <select name="tipo" id="tipo" style={ styles.select } onChange={ handleTipo }>
                            <option value="bug" defaultValue>Bug</option>
                            <option value="question">Question</option>
                            <option value="enhacement">Enhacement</option>
                        </select>
                    </div>
                    {/* <div>
                        <select name="severidad" id="severidad" style={ styles.select } onChange={ handleSeverity }>
                            <option value="wishlist">Wishlist</option>
                            <option value="minor">Minor</option>
                            <option value="normal" defaultValue>Normal</option>
                            <option value="important">Important</option>
                            <option value="critical">Critical</option>
                        </select>
                    </div> */}
                    <div>
                        <p>Prioridad de la issue:</p>
                        <select name="prioridad" id="prioridad" style={ styles.select } onChange={ handlePriority }>
                            <option value="low">Low</option>
                            <option value="normal" defaultValue>Normal</option>
                            <option value="high">High</option>
                        </select>
                    </div>
                </div>
                <div>
                    

                </div>
            </div>
        </div>
    )
}