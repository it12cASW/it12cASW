import { useEffect } from "react";
import { FaCircle } from "react-icons/fa";
import React from "react";
import { Link } from "react-router-dom";

// Controladores
import { getIssuesCtrl } from "../Controllers/issueCtrl";

export default function ShowIssues({orderedIssues}) {

    // Pantalla
    const [isLoading, setIsLoading] = React.useState(true);

    // Variables
    const [issues, setIssues] = React.useState([]);

    async function getIssuesAPI() {
        var issues_aux = await getIssuesCtrl();
        setIssues(issues_aux);
    }
    async function orderIssuesAPI() {
        var issues_aux = {};
        setIssues(issues_aux);
    }

    useEffect(() => {
        setIsLoading(true);
        console.log("orderedIssues: " + orderedIssues);
        if (orderedIssues === null)getIssuesAPI();
        else orderIssuesAPI();
        // recorre issues
        for (var i = 0; i < issues.length; i++) {
            console.log("issue: " + issues[i]);
        }

        setIsLoading(false);
    }, []);
    useEffect(() => {
        setIssues(orderedIssues); // Actualiza el valor de 'issues' cuando 'orderedIssues' cambie
    }, [orderedIssues]);
    return (
        <div>
            {issues && issues.map((issue) => (
                <div style={styles.filaIssue} key={ issue.id }>
                    <div style={styles.columna}>
                        {issue.type && issue.type === "bug" && <FaCircle style={{ color:"red" }}/>}
                        {issue.type && issue.type === "question" &&<FaCircle styles={{ color:"blue" }}/>}
                        {issue.type && issue.type === "enhancement" && <FaCircle styles={{ color:"green" }}/>}
                    </div>
                    <div style={styles.columna}>
                        {issue.severity && issue.severity === "wishlist" && <FaCircle style={{ color:"violet" }}/>}
                        {issue.severity && issue.severity === "minor" && <FaCircle style={{ color:"blue" }}/>}
                        {issue.severity && issue.severity === "normal" && <FaCircle style={{ color:"green" }}/>}
                        {issue.severity && issue.severity === "important" && <FaCircle style={{ color:"orange" }}/>}
                        {issue.severity && issue.severity === "critical" && <FaCircle style={{ color:"red" }}/>}
                    </div>
                    <div style={styles.columna}>
                        {issue.prioridad && issue.prioridad === "low" && <FaCircle style={{ color:"green" }}/>}
                        {issue.prioridad && issue.prioridad === "normal" && <FaCircle style={{ color:"orange" }}/>}
                        {issue.prioridad && issue.prioridad === "high" && <FaCircle style={{ color:"red" }}/>}
                    </div>
                    <div style={styles.columna}>#{issue.id}</div>
                    <div style={styles.columnaTexto}><Link to={`/${issue.id}`}>{issue.asunto}</Link></div>
                    <div style={styles.columna}>
                        {issue.status && issue.status === "new" && <FaCircle style={{ color:"violet" }}/>}
                        {issue.status && issue.status === "progres" && <FaCircle style={{ color:"blue" }}/>}
                        {issue.status && issue.status === "test" && <FaCircle style={{ color:"yellow" }}/>}
                        {issue.status && issue.status === "closed" && <FaCircle style={{ color:"green" }}/>}
                        {issue.status && issue.status === "info" && <FaCircle style={{ color:"red" }}/>}
                        {issue.status && issue.status === "rejected" && <FaCircle style={{ color:"grey" }}/>}
                        {issue.status && issue.status === "postponed" && <FaCircle style={{ color:"blue" }}/>}
                    </div>
                    <div style={styles.columna}>{issue.actividades && issue.actividades[issue.actividades.length - 1].fecha.split('T')[0]}</div>
                    <div style={styles.columna}>{issue.asignada && issue.asignada.username}</div>
                </div>
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


