import React from "react";
import { useEffect } from "react";

// Controladores
import { getIssueCtrl } from '../Controllers/issueCtrl';
import Actividad from './Actividad';


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
        <div style={ styles.conentedor }>
            <div style={{ paddingLeft:"10px", display:"flex", flexDirection:"row", justifyContent:"center" }}>
                <h2>Actividades</h2>
            </div>
            <div style={ styles.commentContainer }>
                {activities ? (
                    <div style={{ padding:"10px" }}>
                        {activities.map((activity) => (
                            <Actividad activity={activity} />

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
    conentedor : {
        width:"100%",
        height:"100%",
        // borderColor:"#000000",
        // borderWidth:"1px",
        // borderStyle:"solid",
        // borderRadius:"5px",
        marginLeft:"10px",
    },
    commentContainer: {
        paddingBottom:"10px",
        // backgroundColor:"#F0ECCF",
        height:"800px",
        overflow:"auto",
        marginLeft:"10px",
        marginRight:"10px",
        borderRadius:"10px",
    },
    actividad: {
        paddingLeft:"10px",
        paddingRight:"10px",
        
        borderRadius:"5px",
        marginTop:"5px",
        backgroundColor: 'rgba(236, 236, 236, 0.7)',
        paddingLeft:"10px",
        paddingRight:"10px",
        paddingTop:"3px",
        paddingBottom:"3px",
    },
    texto: {
        fontFamily: 'sans-serif',
        height: '20px',
        fontSize: '12px',
    }
}