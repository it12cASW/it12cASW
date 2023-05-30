import { useEffect } from "react";
import { FaCircle } from "react-icons/fa";
import React from "react";
import { Link } from "react-router-dom";

// Controladores
import { getIssuesCtrl } from "../Controllers/issueCtrl";
import IssueRow from "./IssueRow"




export default function ShowIssues({ parametros }) {

    // Pantalla
    const [isLoading, setIsLoading] = React.useState(true);

    // Variables
    const [issues, setIssues] = React.useState([]);

    async function getIssuesAPI() {
        var issues_aux = await getIssuesCtrl();
        setIssues(issues_aux);
        if(parametros != null && parametros != "") {
            var auxIssues = issues.filter(issue => issue.asunto.includes(parametros));
            setIssues(auxIssues);
        }
    }

    useEffect(() => {

        setIsLoading(true);
        getIssuesAPI();
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


