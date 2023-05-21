
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
        <div>
            { isLoading ? (
                <div>
                    <h1>Cargando...</h1>
                </div>
            ) : (
                <div style={styles.mainContainer}>
                    <div style={ styles.infoContainer }>
                        <div style={{ display:"flex", flexDirection:"row" }}>
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
        flexDirection: 'row',
        justifyContent: 'space-between',
        width: '100%',
        backgroundColor: '#E6FFFD',
        alignItems: 'center',
        alignObject: 'center',

    },
    infoContainer: {
        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'space-between',
        width: '90%',
        backgroundColor: 'rbga(236, 236, 236, 0.9)',
        height: "700px",
        alignItems: 'center',
        selfAlign: 'center',
    },
    containerInfoIssue: {
        width: '70%',
    },
    containerActivities: {
        width: '30%',

    },
    commentsContainer: {
        width: '100%',
        maxHeight: '500px',
        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'center',
        backgroundColor: '#F0ECCF',
        borderRadius: '10px',
        marginTop: '20px',
        alignItems: 'center',
        alignObject: 'center',
    
    },

}