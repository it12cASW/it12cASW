
import React, { useEffect } from 'react';
import { useState } from "react"

import { useParams } from 'react-router-dom';
import { getIssuesCtrl } from '../../Controllers/issueCtrl';
import { styles } from "./style"
import { Link } from "react-router-dom";


// Controladores
import { getIssueCtrl } from '../../Controllers/issueCtrl';
import { getCommentsCtrl } from '../../Controllers/commentCtrl';
import { getActivitiesCtrl } from '../../Controllers/activityCtrl';
import {getUsuariosFullCtrl} from '../../Controllers/usuariosCtrl';

// Componentes
import IssueRow from '../../Components/IssueRow';
import Actividades from '../../Components/Actividades';
import Comments from '../../Components/Comments';
import {getIdUsuario} from '../../vars'
import Actividad from '../../Components/Actividad';


import axios from 'axios';

// Estilos

// Pantallas


export default function Profile({ idUsuario, handleUsuario }) {
    const [user, setUser] = useState('');


    useEffect(() => {
        const fetchUser = async () => {
            try {
                const params = {
                    id: idUsuario,
                    serializer_type: 'full', // Replace with the desired serializer type
                };

                const userData = await getUsuariosFullCtrl(params);

                setUser(userData[0]);
            } catch (error) {
                console.error('Error fetching user:', error);
            }
        };

        fetchUser();
    }, [idUsuario]);

    if (!user) {
        return <div>Loading user...</div>;
    }

    return (
        <div>
            <div style={{width: "100%"}}>
                <h2>User Information</h2>
                <p>Username: {user.username}</p>
                <p>Email: {user.email}</p>
            </div>
            <div style={{display: "flex" , margin:"5px"}}>

                <div style={{width: "50%", margin:"5px", border:"1px"}}>
                    <h3>Activities</h3>
                    {user.actividades_hechas.map((actividad) => (
                        <Actividad activity={actividad} />
                    ))}

                    <h3>Comments</h3>
                    {user.comments.map((comment) => (
                        <div key={comment.id}>
                            <p>Text: {comment.text}</p>
                            {/* Display other relevant fields */}
                        </div>
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
}
