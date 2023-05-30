import React from "react";
import { styles } from "./style";
import { GiAlienEgg } from "react-icons/gi";
import { RiAliensFill } from "react-icons/ri";
import { AiOutlineSearch } from "react-icons/ai";
import { AiOutlineAppstoreAdd } from "react-icons/ai";
import { GrAdd } from "react-icons/gr";
import { FaCircle } from "react-icons/fa";
import { Link } from "react-router-dom";

// Controladores
import { getUsuariosCtrl } from "../../Controllers/usuariosCtrl";
import { getIssuesCtrl } from "../../Controllers/issueCtrl";
import { getUsernameUsuario, setUsuario } from "../../vars";
import { getIdUsuario } from "../../vars";
import { getUsuario } from "../../vars";

// Componentes
import ShowIssues from "../../Components/ShowIssues";
import { getAllUsers } from "../../vars";



export default function Main ({ idUsuario, handleUsuario }){
    const [isLoading, setIsLoading] = React.useState(true);
    const [issues, setIssues] = React.useState([]);
    const [parametros, setParametros] = React.useState(null);
    const [usuarios, setUsuarios] = React.useState(Array);    
  
    async function getUsuariosAPI() {
        return await getUsuariosCtrl();
    }

    async function getIssuesAPI() {
         return await getIssuesCtrl();
    }

    function handleUsuario(e) {
      setUsuario(e.target.value)

      var auxIssues = getIssuesAPI();
      if (auxIssues != null) setIssues(auxIssues);
      setIsLoading(false);
    }

    function buscarIssues(e) {
      setIsLoading(true);
      setParametros(e.target.value)

      setIsLoading(false);
    }


    // Cuando cargue la pgina
    React.useEffect(() => {

        console.log("El usuario por defecto es: " + getUsernameUsuario())
        var auxUsuarios = getAllUsers();  
        var auxIssues = getIssuesAPI();

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
                <p>
                    <Link to="/profile" style={{ fontFamily: "sans-serif", color: "#008aa8" }}>
                        Profile</Link>
                </p>

            </div>
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
                    onChange={buscarIssues}
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
                    <select style={{width: "100px", height: "30px"}} onChange={ handleUsuario }>
                        {/* Recorre la variable 'usuarios' y crea una opción para cada uno */}
                        {usuarios && usuarios.map((usuario) => 
                            <option value={usuario.id} key={usuario.id} defaultValue={ usuario.id === getUsuario() }>{usuario.username}</option>
                        )}  
                    </select>
                    <p>Se ha iniciado con el usuario: { getUsernameUsuario() }</p>
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

                  <div style={{ position: "relative" , marginLeft:"5px" }}>
                      <AiOutlineAppstoreAdd
                          style={{ position: "absolute", top: "10px", left: "7px" }}
                      />
                      <button style={styles.newIssueButton }>
                          <Link to="/bulkInsert" style={{color: "white", textDecoration: "none"}}>Bulk Insert</Link>
                      </button>
                  </div>
              </div>
            </div>
            {/* Tabla */}
            <div style={styles.tablaContainer}>
              {/* Fila */}
              <div style={styles.fila}>
                {/* <div style={styles.columna}>Type</div>
                <div style={styles.columna}>Severity</div> */}
                <div style={styles.columna}>Priority</div>
                <div style={styles.columna}>Issue</div>
                <div style={styles.columnaTexto}>Title</div>
                <div style={styles.columna}>Status</div>
                <div style={styles.columna}>Date</div>
                <div style={styles.columna}>Assign to</div>
              </div>
              {/* por cada elemento en issues crea una nueva fila */}
              <ShowIssues parametros={ parametros }/>
              
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

