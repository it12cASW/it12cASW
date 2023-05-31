import { useEffect } from "react";
import { FaCircle } from "react-icons/fa";
import React from "react";
import { Link } from "react-router-dom";

// Controladores
import { getIssuesCtrl } from "../Controllers/issueCtrl";
import IssueRow from "./IssueRow"

export default function ShowIssues({sharedIssues, parametros}) {

    // Pantalla
    const [isLoading, setIsLoading] = React.useState(true);

    // Variables
    const [issues, setIssues] = React.useState([]);
    const [issuesGuardades, setIssuesGuardades] = React.useState([]);

    async function getIssuesAPI() {
        var issues_aux = await getIssuesCtrl();
        setIssues(issues_aux);
        setIssuesGuardades(issues_aux);
    }
    async function orderIssuesAPI() {
        var issues_aux = {};
        setIssues(issues_aux);
        setIssuesGuardades(issues_aux);
    }

    useEffect(() => {

        setIsLoading(true);
        console.log("orderedIssues: " + sharedIssues);
        if (sharedIssues === null)getIssuesAPI();
        else orderIssuesAPI();
        // recorre issues
        for (var i = 0; i < issues.length; i++) {
            console.log("issue: " + issues[i]);
        }
        setIsLoading(false);
    }, []);
    useEffect(() => {
        setIsLoading(true);
        setIssues(sharedIssues); // Actualiza el valor de 'issues' cuando 'orderedIssues' cambie
        setIssuesGuardades(sharedIssues);
        setIsLoading(false);
    }, [sharedIssues]);

    React.useEffect(() => {
        setIsLoading(true);
      
        // Filtrar las issues
        const lowercaseParametros = parametros.toLowerCase(); // Convertir los parámetros a minúsculas
      
        var auxIssues = issuesGuardades.filter(issues =>
          issues.asunto.toLowerCase().includes(lowercaseParametros)
        );
        setIssues(auxIssues);
      
        setIsLoading(false);
    }, [parametros]);
      
      
    return (
        <div>
            {issues && issues.map((issue) => (
                <IssueRow issue={issue}></IssueRow>
            ))}
        </div>  
    );
}


const styles = {

    fila: {
        display: "flex",
        flexDirection: "row",
        justifyContent: "space-between",
        paddingTop:"10px",
        paddingBottom:"10px",
        paddingLeft:"20px",
    },
    filaIssue: {
        display: "flex",
        flexDirection: "row",
        justifyContent: "space-between",
        paddingTop:"10px",
        paddingBottom:"10px",
        paddingLeft:"20px",
        backgroundColor: "#f9f9fb",
        borderRadius: "5px",
        marginBottom: "10px",
    },
    columna: {
        display: "flex",
        flexDirection: "column",
        justifyContent: "center",
        width: "15%",
    },
    columnaTexto: {
        display: "flex",
        flexDirection: "column",
        justifyContent: "center",
        width: "50%",
    },
}


