
import React, { useEffect } from 'react';
import { useParams } from 'react-router-dom';
import { getIssuesCtrl } from '../../Controllers/issueCtrl';

// Controladores
import { getIssueCtrl } from '../../Controllers/issueCtrl';
import { getCommentsCtrl } from '../../Controllers/commentCtrl';
import { getActivitiesCtrl } from '../../Controllers/activityCtrl';

// Componentes

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
        getCommentsAPI(id);
        getActivitiesAPI(id);

        setIsLoading(false);
    }, []);


    return (
        <div>
            { isLoading ? (
                <div>
                    <h1>Cargando...</h1>
                </div>
            ) : (
                <div>
                    <h1>Mostrar Issue número: { id }</h1>
                </div>
            )}
        </div>
    )
}