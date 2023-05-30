import { useEffect } from "react";
import { FaCircle } from "react-icons/fa";
import React from "react";
import { Link } from "react-router-dom";
import 'react-tooltip/dist/react-tooltip.css'
import { Tooltip } from 'react-tooltip'


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


const IssueRow = ({ issue }) => {
    return (
        <div style={styles.filaIssue} key={ issue.id }>
            {/* <div style={styles.columna}>
                {issue.type && issue.type === "bug" && <FaCircle style={{ color:"red" }}/>}
                {issue.type && issue.type === "question" &&<FaCircle styles={{ color:"blue" }}/>}
                {issue.type && issue.type === "enhancement" && <FaCircle styles={{ color:"green" }}/>}
            </div>
            <div style={styles.columna}>
                {issue.severity && issue.severity === "wishlist" && <div><FaCircle data-tooltip-id="my-tooltip" data-tooltip-content="wishlist" style={{ color:"violet" }}/><Tooltip id="my-tooltip" /></div>}
                {issue.severity && issue.severity === "minor" && <div><FaCircle data-tooltip-id="my-tooltip" data-tooltip-content="minor" style={{ color:"blue" }}/><Tooltip id="my-tooltip" /></div>}
                {issue.severity && issue.severity === "normal" && <div><FaCircle data-tooltip-id="my-tooltip" data-tooltip-content="normal" style={{ color:"green" }}/><Tooltip id="my-tooltip" /></div>}
                {issue.severity && issue.severity === "important" && <div><FaCircle data-tooltip-id="my-tooltip" data-tooltip-content="important" style={{ color:"orange" }}/><Tooltip id="my-tooltip" /></div>}
                {issue.severity && issue.severity === "critical" && <div><FaCircle data-tooltip-id="my-tooltip" data-tooltip-content="critical" style={{ color:"red" }}/><Tooltip id="my-tooltip" /></div>}
            </div> */}
            <div style={styles.columna}>
                {issue.prioridad && issue.prioridad === "low" && <div><FaCircle data-tooltip-id="my-tooltip" data-tooltip-content="Low" style={{ color:"green" }}/> <Tooltip id="my-tooltip" /></div>}
                {issue.prioridad && issue.prioridad === "normal" && <div><FaCircle  data-tooltip-id="my-tooltip" data-tooltip-content="Normal" style={{ color:"orange" }}/><Tooltip id="my-tooltip" /></div>}
                {issue.prioridad && issue.prioridad === "high" && <div><FaCircle  data-tooltip-id="my-tooltip" data-tooltip-content="High" style={{ color:"red" }}/><Tooltip id="my-tooltip" /></div>}
            </div>
            <div style={styles.columna}>#{issue.id}</div>
            <div style={styles.columnaTexto}><Link to={`/${issue.id}`}>{issue.asunto}</Link></div>
            <div style={styles.columna}>
                {issue.status && issue.status === "new" && <div><FaCircle data-tooltip-id="my-tooltip" data-tooltip-content="New" style={{ color:"violet" }}/><Tooltip id="my-tooltip" /></div>}
                {issue.status && issue.status === "progres" && <div><FaCircle data-tooltip-id="my-tooltip" data-tooltip-content="Progres" style={{ color:"blue" }}/><Tooltip id="my-tooltip" /></div>}
                {issue.status && issue.status === "test" && <div><FaCircle data-tooltip-id="my-tooltip" data-tooltip-content="Test" style={{ color:"yellow" }}/><Tooltip id="my-tooltip" /></div>}
                {issue.status && issue.status === "closed" && <div><FaCircle data-tooltip-id="my-tooltip" data-tooltip-content="Closed" style={{ color:"green" }}/><Tooltip id="my-tooltip" /></div>}
                {issue.status && issue.status === "info" && <div><FaCircle data-tooltip-id="my-tooltip" data-tooltip-content="Needs Info" style={{ color:"red" }}/><Tooltip id="my-tooltip" /></div>}
                {issue.status && issue.status === "rejected" && <div><FaCircle data-tooltip-id="my-tooltip" data-tooltip-content="Rejected" style={{ color:"grey" }}/><Tooltip id="my-tooltip" /></div>}
                {issue.status && issue.status === "postponed" && <div><FaCircle data-tooltip-id="my-tooltip" data-tooltip-content="Postponed" style={{ color:"blue" }}/><Tooltip id="my-tooltip" /></div>}
            </div>
            <div style={styles.columna}>{issue.actividades && issue.actividades[issue.actividades.length - 1].fecha.split('T')[0]}</div>
            <div style={styles.columna}>{issue.asignada && issue.asignada.username}</div>
        </div>
    );
};

export default IssueRow;