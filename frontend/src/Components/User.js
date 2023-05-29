import React from 'react';

import { Link } from "react-router-dom";
import IssueRow from './IssueRow';
import Actividades from './Actividades';
import Comment from './Comment';
import {getIdUsuario} from '../vars'
import Actividad from './Actividad';

const styles = {
    botonCrear: {
        width: "30%",
        height: "30px",
        alignSelf: "center",
        borderRadius: "5px",
        border: "2px solid #ccc",
        backgroundColor: "#F5F5F5",
        color: "black",
        padding: "10px",
        marginTop: "10px",
        marginBottom: "10px",
    },

};



const User = ({ user }) => {
    return (
        <div>


            <div style={{display: "flex" , margin:"5px"}}>

                <div style={{width: "50%", margin:"5px", border:"1px"}}>
                    <h3>Activities</h3>
                    {user.actividades_hechas.map((actividad) => (
                        <Actividad activity={actividad} />
                    ))}

                    <h3>Comments</h3>
                    {user.comments.map((comment) => (
                        <Comment comment={comment}></Comment>
                    ))}

                </div>
                <div style={{width: "50%",margin:"5px" , border:"1px"}}>
                    <h3>Vigilant Issues</h3>
                    {user.issues_vigiladas.map((issue) => (
                        <IssueRow issue={issue}></IssueRow>
                    ))}



                    <h3>Created Teams</h3>
                    {user.equipos_creados.map((equipo) => (
                        <div key={equipo.id}>
                            <p>Name: {equipo.name}</p>
                            {/* Display other relevant fields */}
                        </div>
                    ))}

                </div>

            </div>

            <div style={{ alignSelf: "center"}}>
                <button style={ styles.botonCrear }>
                    <Link to="/">Volver</Link>
                </button>
            </div>
        </div>
    );
};

export default User;