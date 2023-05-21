import React from "react";
import { useEffect } from "react";

// Controladores
import { getIssueCtrl } from '../Controllers/issueCtrl';

export default function Actividades({ issue }) {

    const [activities, setActivities] = React.useState(null);

    async function getActivitiesAPI(id) {

        var issue_obj = await getIssueCtrl(id);
        var activities = issue_obj.actividades;
        setActivities(activities);
    }

    useEffect(() => {

        // Obtengo issue y comentarios y actividades
        getActivitiesAPI(issue);
        
    }, []);

    return (
        <div style={{ backgroundColor:"#A3BB98", width:"100%", maxHeight:"650px", overflow:"auto", marginTop:"5px", borderRadius:"10px"}}>
            <div style={{ paddingLeft:"10px", display:"flex", flexDirection:"row", justifyContent:"center" }}>
                <h2>Actividades</h2>
            </div>
            <div style={{ width:"100%" }}>
                {activities ? (
                    <div style={{ padding:"10px" }}>
                        {activities.map((activity) => (
                            <div style={ styles.actividad }>
                                <p style={{ fontSize:"15px" }}>El usuario {activity.usuario} ha hecho una modificación de tipo {activity.tipo} con la fecha {activity.fecha}</p>
                            </div>
                        ))}
                    </div>
                ) : (
                    <div>
                        <p>No hay actividades</p>
                    </div>
                )}

            </div>  
        </div>
    );
}

const styles = {
    actividad: {
        paddingLeft:"10px",
        paddingRight:"10px",
        borderWidth:"1px",
        borderStyle:"solid",
        borderColor:"#000000",
        borderRadius:"5px",
        marginTop:"5px",
        backgroundColor:"#F0ECCF",
    },
}