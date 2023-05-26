import React, { useState } from 'react';
import { RiArrowDownSFill, RiArrowUpSFill } from 'react-icons/ri';

const ClickableArrows = ({ isActive, handleClick, direction }) => {
    return (
      <div style={styles.column}>
        <div onClick={handleClick}>
          {isActive ? (
            <>
              <RiArrowUpSFill style={direction ? styles.clickedIcon : styles.icon} />
              <RiArrowDownSFill style={direction ? styles.icon : styles.clickedIcon} />
            </>
          ) : (
            <>
              <RiArrowUpSFill style={!isActive ? styles.icon : null} />
              <RiArrowDownSFill style={!isActive ? styles.icon : null} />
            </>
          )}
        </div>
      </div>
    );
  };  

  const App = () => {
    const [activeIndexes, setActiveIndexes] = useState({});
    const [direction, setDirection] = useState(false); // Estado para almacenar la dirección de la flecha
  
    const handleClick = (index) => {
      setActiveIndexes((prevState) => {
        const newActiveIndexes = { ...prevState };
        if (newActiveIndexes[index] && Object.keys(newActiveIndexes).length > 1) {
          // Si ya está activa y hay otras instancias activas, cambiar solo la dirección
          setDirection(direction ? false : true);
          //escribe por pantalla el valor de direction
          console.log(direction);
        } else {
          // Deseleccionar cualquier otra instancia activa
          Object.keys(newActiveIndexes).forEach((key) => {
            newActiveIndexes[key] = false;
          });
          newActiveIndexes[index] = true; // Seleccionar el nuevo componente
          setDirection(true); // Restablecer la dirección a la predeterminada al seleccionar uno nuevo
        }
  
        // Actualizar el estado de setActiveIndexes
        if (newActiveIndexes[index]) {
          setActiveIndexes(newActiveIndexes);
        } else {
          setActiveIndexes({});
        }
  
        return newActiveIndexes;
      });
    };
  
    return (
      <div>
        <div style={styles.fila}>
          <ClickableArrows
            isActive={activeIndexes[0]}
            handleClick={() => handleClick(0)}
            direction={direction && activeIndexes[0]} // Pasar el valor booleano de direction
          />
          <div style={styles.columna}>Type</div>
          <ClickableArrows
            isActive={activeIndexes[1]}
            handleClick={() => handleClick(1)}
            direction={direction && activeIndexes[1]} // Pasar el valor booleano de direction
          />
          <div style={styles.columna}>Severity</div>
          <ClickableArrows
            isActive={activeIndexes[2]}
            handleClick={() => handleClick(2)}
            direction={direction && activeIndexes[2]} // Pasar el valor booleano de direction
          />
          <div style={styles.columna}>Priority</div>
          <ClickableArrows
            isActive={activeIndexes[3]}
            handleClick={() => handleClick(3)}
            direction={direction && activeIndexes[3]} // Pasar el valor booleano de direction
          />
          <div style={styles.columna}>Issue</div>
          <div style={styles.columnaTexto}></div>
          <ClickableArrows
            isActive={activeIndexes[4]}
            handleClick={() => handleClick(4)}
            direction={direction && activeIndexes[4]} // Pasar el valor booleano de direction
          />
          <div style={styles.columnaDerecha}>Status</div>
          <ClickableArrows
            isActive={activeIndexes[5]}
            handleClick={() => handleClick(5)}
            direction={direction && activeIndexes[5]} // Pasar el valor booleano de direction
          />
          <div style={styles.columnaDerecha}>Modified</div>
          <ClickableArrows
            isActive={activeIndexes[6]}
            handleClick={() => handleClick(6)}
            direction={direction && activeIndexes[6]} // Pasar el valor booleano de direction
          />
          <div style={styles.columnaDerecha}>Assign to</div>
        </div>
      </div>
    );
  };

const styles = {
  fila: {
    display: "flex",
    flexDirection: "row",
    justifyContent: "space-between",
    paddingTop: "10px",
    paddingBottom: "10px",
    paddingLeft: "20px",
    paddingRight: "20px",
  },
  columna: {
    display: "flex",
    flexDirection: "column",
    justifyContent: "center",
    width: "9%",
  },
  columnaDerecha: {
    display: "flex",
    flexDirection: "column",
    justifyContent: "center",
    width: "10%",
  },
  columnaTexto: {
    display: "flex",
    flexDirection: "column",
    justifyContent: "center",
    width: "45%",
  },
  column: {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center'
  },
  icon: {
    margin: '0.5px',
    cursor: 'pointer',
    color: '#d4d4d4'
  },
  clickedIcon: {
    margin: '0.5px',
    cursor: 'pointer',
    color: '#83eede'
  },
  tablaContainer: {
    display: "flex",
    flexDirection: "column",
    width: "100%",
  },
};

export default App;