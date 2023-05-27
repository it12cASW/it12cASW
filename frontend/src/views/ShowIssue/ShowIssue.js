
import React, { useEffect } from 'react';
import { useParams } from 'react-router-dom';
import { getIssuesCtrl } from '../../Controllers/issueCtrl';

// Controladores
import { getIssueCtrl } from '../../Controllers/issueCtrl';
import { getCommentsCtrl } from '../../Controllers/commentCtrl';
import { getActivitiesCtrl } from '../../Controllers/activityCtrl';

// Componentes
import InfoIssue from '../../Components/InfoIssue';
import Actividades from '../../Components/Actividades';
import Comments from '../../Components/Comments';

// Estilos

// Pantallas

export default function ShowIssue() {

    // Pantalla
    const [isLoading, setIsLoading] = React.useState(true);

    // Variables
    const { id } = useParams();
    const [issue, setIssue] = React.useState(null);
    const [comments, setComments] = React.useState(null);
    const [activities, setActivities] = React.useState(null);

    async function getIssueAPI(id) {
        var issue_aux = await getIssueCtrl(id);
        setIssue(issue_aux);
        setIsLoading(false);
    }

    function rechargeInfoIssue() {
        setIsLoading(true);
        getIssueAPI(id);
        
    }

    async function getCommentsAPI(id) {
        var comments_aux = await getCommentsCtrl(id);
        setComments(comments_aux);
    }

    async function getActivitiesAPI(id) {
        var activities_aux = await getActivitiesCtrl(id);
        setActivities(activities_aux);
    }

    // Funciones
    useEffect(() => {
        setIsLoading(true);

        // Obtengo issue y comentarios y actividades
        getIssueAPI(id);
    
    }, []);

    return (
        <div style={{ display:"flex", justifyContent:"center"}}>
            { isLoading ? (
                <div>
                    <h1>Cargando...</h1>
                </div>
            ) : (
                <div style={styles.mainContainer}>
                    {/* vertical */}
                    <div style={ styles.infoContainer }>
                        <div style={ styles.upperContainer }>
                            <div style={ styles.containerInfoIssue }>
                                <InfoIssue issue={issue} setIssue={ rechargeInfoIssue }/>
                            </div>
                            <div sytle={ styles.containerActivities }>
                                <Actividades issue={issue.id}/>
                            </div>
                        </div>
                        <div style={ styles.commentsContainer}>
                            <Comments issue={issue.id}/>
                        </div>
                    </div>
                </div>
            )}
        </div>
    )
}

const styles = {
    mainContainer: {
        display: 'flex',
        justifyContent: 'center',
    },
    infoContainer: {
        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'center',
        marginTop: '50px',
        marginBottom: '50px',

        width: '90%',
        // borderRadius: '10px',
        // borderWidth: '1px',
        // borderColor: 'grey',
        // border: "solid",
        padding: '20px',
    },
    containerInfoIssue: {
        // border: "solid",
        // borderRadius: '10px',
        // borderWidth: '1px',
        padding: '20px',
        width: '70%',

        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'center',
    },
    upperContainer: {
        display: 'flex',
        flexDirection: 'row',
        justifyContent: 'space-between',
        width: '100%',
        height: 'auto',
    },
    containerActivities: {
        marginLeft: '20px',
        padding: '20px',
    },
    commentsContainer: {
        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'center',
    },

}