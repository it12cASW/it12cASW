import React from "react";
import { styles } from "./style";
import { GiAlienEgg } from "react-icons/gi";
import { RiAliensFill } from "react-icons/ri";
import { AiOutlineSearch } from "react-icons/ai";
import { AiOutlineAppstoreAdd } from "react-icons/ai";
import { GrAdd } from "react-icons/gr";
import { FaCircle } from "react-icons/fa";
import { Link } from "react-router-dom";


import ColumnWithClickableArrows from "./OrderArrow";


// Controladores
import { getUsuariosCtrl } from "../../Controllers/usuariosCtrl";
import { getIssuesCtrl } from "../../Controllers/issueCtrl";


export default function Main ({ idUsuario, handleUsuario }){
    const [isLoading, setIsLoading] = React.useState(true);
    const [issues, setIssues] = React.useState([]);
    const [usuarios, setUsuarios] = React.useState(Array);    
  
    async function getUsuariosAPI() {

        return await getUsuariosCtrl();
    }

    async function getIssuesAPI() {
         return await getIssuesCtrl();
    }


    // Cuando cargue la pgina
    React.useEffect(() => {

        // var auxUsuarios = getUsuariosAPI();
        var auxIssues = getIssuesAPI();
        

        // var auxIssues = [
        // {
        //     id: 1,
        //     type: "bug",
        //     severity: "minor",
        //     priority: "low",
        //     title: "Issue 1",
        //     description: "Description 1",
        //     status: "test",
        //     modified: "2021-10-10",
        //     assignee: "Assignee 1",
        // },
        // {
        //     id: 2,
        //     type: "question",
        //     severity: "wishlist",
        //     priority: "normal",
        //     title: "Issue 2",
        //     description: "Description 2",
        //     status: "closed",
        //     modified: "2021-10-10",
        //     assignee: "Assignee 2",
        // },
        // ];

        var auxUsuarios = [
            {
                id: 1,
                name: "Usuario 1",
                token: "Token 1",
            },
            {
              id: 2,
              name: "Usuario 2",
              token: "Token 1",
          }
        ];

        if (auxUsuarios != null) {
          setUsuarios(auxUsuarios);
        }
        
        if (auxIssues != null) setIssues(auxIssues);
        setIsLoading(false);

    }, []);

    return (
        <div style={styles.mainScreen} id="test">
      
      <div style={styles.upperContainer}>
        <div>
          <RiAliensFill style={{ fontSize: "35px" }} />
        </div>
        <div
          style={{
            display: "flex",
            flexDirection: "row",
            display: "flex",
            justifyContent: "center",
          }}
        >
          <div style={{ width: "80px" }}>
            <p style={{ fontFamily: "sans-serif", color: "#008aa8" }}>Login</p>
          </div>
          <div
            style={{
              display: "flex",
              flexDirection: "row",
              display: "flex",
              justifyContent: "center",
            }}
          >
            <p style={{ fontFamily: "sans-serif", color: "#008aa8" }}>
              Sign Up
            </p>
          </div>
        </div>
      </div>
      <div style={styles.mainContainer}>
        <div style={styles.lateralBar}>
          <div style={styles.lateralSuperior}>
            <div
              style={{
                height: "auto",
                backgroundColor: "rgb(46, 52, 64)",
                paddingLeft: "10px",
                margin: "0px",
                display: "flex",
                alignItems: "center",
                justifyContent: "space-between",
                paddingLeft: "15px",
                paddingRight: "15px",
                paddingTop: "15px",
                paddingBottom: "15px",
              }}
            >
              <GiAlienEgg style={{ color: "#008aa8" }} />
              <p style={styles.nombreLateral}>ASW-2022-2023</p>
            </div>
            <p style={styles.textLateral}>Epics</p>
            <p style={styles.textLateral}>Scrum</p>
            <p style={styles.textLateral}>Issues</p>
          </div>
          <div styles={styles.lateralInferior}>
            <p style={styles.textLateral}>Search</p>
            <p style={styles.textLateral}>Wiki</p>
            <p style={styles.textLateral}>Team</p>
          </div>
        </div>
        {isLoading ? (
          <p>Loading...</p>
        ) : (
          <div style={styles.containerBlock}>
            {/* Issues */}
            <div
              style={{
                width: "100%",
                display: "flex",
                flexDirection: "flex-start",
                justifyContent: "unset",
                width: "100%",
                paddingBottom: "20px",
              }}
            >
              <p
                style={{
                  fontSize: "30px",
                  margin: "0px",
                  fontFamily: "sans-serif",
                  color: "#008aa8",
                }}
              >
                Issues
              </p>
            </div>
            {/* Buscador y filtros */}
            <div style={styles.barraFiltro}>
              <div
                style={{
                  display: "flex",
                  flexDirection: "row",
                  justifyContent: "space-between",
                  width: "50%",
                }}
              >
                {/* Filters */}
                <div>
                  <a
                    href="#"
                    style={{ color: "#008aa8", textDecoration: "none" }}
                  >
                    Filters
                  </a>
                </div>
                {/* Buscador */}
                <div style={{ position: "relative" }}>
                  <input
                    type="text"
                    placeholder="Search issues"
                    style={styles.inputBuscador}
                  />
                  <AiOutlineSearch
                    style={{ position: "absolute", right: "10px", top: "6px" }}
                  />
                </div>
                {/* Tags */}
                <div
                  style={{
                    flexWrap: "wrap",
                    width: "30%",
                    display: "flex",
                    flexDirection: "row",
                    alignContent: "center",
                    justifyContent: "flex-start",
                  }}
                >
                  <label style={{ marginRight: "5px" }}>
                    Tags
                  </label>
                  <input
                    type="checkbox"
                    style={{ width: "20px", height: "20px" }}
                  />
                </div>
                <div>
                    <select style={{width: "100px", height: "30px"}} onChange={ handleUsuario } >
                        <option value="0" key="0">Usuario</option>
                        {/* Recorre la variable 'usuarios' y crea una opción para cada uno */}
                        {usuarios.map((usuario) => 
                            <option value={usuario.id} key={usuario.id}>{usuario.name}</option>
                        )}  
                    </select>
                </div>
              </div>
              <div
                style={{
                  display: "flex",
                  flexDirection: "row",
                  width: "30%",
                  justifyContent: "end",}}
              >
                {/* New issue */}
                <div style={{ position: "relative" }}>
                  <GrAdd
                    style={{ position: "absolute", top: "10px", left: "7px" }}
                  />
                  <button style={styles.newIssueButton} >
                    {/* /Link a /createIssue */}
                    <Link to="/crearIssue" style={{color: "white", textDecoration: "none"}}>
                    New issue</Link>
                  </button>
                </div>
                {/* Bulk insert */}
                <div
                  style={{
                    display: "flex",
                    paddingLeft: "20px",
                    paddingRight: "20px",
                  }}
                >
                  <button
                    style={{
                      borderWidth: "0px",
                      borderRadius: "3px",
                      backgroundColor: "#C2C2C2",
                      borderStyle: "solid",
                      paddingRight: "10px",
                      paddingLeft: "10px",
                    }}
                  >
                    <AiOutlineAppstoreAdd />
                  </button>
                </div>
              </div>
            </div>
            {/* Tabla */}
            <div style={styles.tablaContainer}>
              {/* Fila */}
              <ColumnWithClickableArrows />              
            </div>
          </div>
        )}
      </div>
    </div>
  );
}