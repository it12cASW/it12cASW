import React, { useState } from 'react';
import { orderIssues } from '../../Controllers/issueCtrl';
import { RiArrowDownSFill, RiArrowUpSFill } from 'react-icons/ri';
import ShowIssues from "../../Components/ShowIssues";

const ClickableArrows = ({ isActive, handleClick, direction, order }) => {
  const handleArrowClick = async () => {
    await handleClick();
    await order();
  };

  return (
    <div style={styles.column}>
      <div onClick={handleArrowClick}>
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

const ColumnWithClickableArrows = ({ sharedIssues, setSharedIssues }) => {
  const [activeIndexes, setActiveIndexes] = useState({});
  const [direction, setDirection] = useState(true);

  const handleClick = (index) => {
    setActiveIndexes((prevState) => {
      const newActiveIndexes = { ...prevState };
      if (newActiveIndexes[index] && Object.keys(newActiveIndexes).length >= 1) {
        setDirection(!direction);
        console.log(direction);
      } else {
        Object.keys(newActiveIndexes).forEach((key) => {
          newActiveIndexes[key] = false;
        });
        newActiveIndexes[index] = true;
        setDirection(false);
        console.log("direction: " + true);
      }
      if (newActiveIndexes[index]) {
        setActiveIndexes(newActiveIndexes);
      } else {
        setActiveIndexes({});
      }
      return newActiveIndexes;
    });
  };

  const handleOrder = async (field, order) => {
    const issues = await orderIssues(field, order);
    await setSharedIssues(issues);
  };

  return (
    <div>
      <div style={styles.fila}>
        <ClickableArrows
          isActive={activeIndexes[0]}
          handleClick={() => {
            handleClick(0);
            console.log("Ordenar por type");
          }}
          direction={direction && activeIndexes[0]} // Pasar el valor booleano de direction
          order={() => handleOrder("type", direction)}
        />
        <div style={styles.columna}>Type</div>
        <ClickableArrows
          isActive={activeIndexes[1]}
          handleClick={() => {
            handleClick(1);
            console.log("Ordenar por severity");
          }}
          direction={direction && activeIndexes[1]} // Pasar el valor booleano de direction
          order={() => handleOrder("severity", direction)}
        />
        <div style={styles.columna}>Severity</div>
        <ClickableArrows
          isActive={activeIndexes[2]}
          handleClick={() => {
            handleClick(2);
            console.log("Ordenar por priority");
          }}
          direction={direction && activeIndexes[2]} // Pasar el valor booleano de direction
          order={() => handleOrder('prioridad', direction)}
        />
        <div style={styles.columna}>Priority</div>
        <ClickableArrows
          isActive={activeIndexes[3]}
          handleClick={() => {
            handleClick(3);
            console.log("Ordenar por issue");
          }}
          direction={direction && activeIndexes[3]} // Pasar el valor booleano de direction
          order={() => handleOrder('asunto', direction)}
        />
        <div style={styles.columna}>Issue</div>
        <div style={styles.columnaTexto}></div>
        <ClickableArrows
          isActive={activeIndexes[4]}
          handleClick={() => {
            handleClick(4);
            console.log("Ordenar por status");
          }}
          direction={direction && activeIndexes[4]} // Pasar el valor booleano de direction
          order={() => handleOrder('status', direction)}
        />
        <div style={styles.columnaDerecha}>Status</div>
        <ClickableArrows
          isActive={activeIndexes[5]}
          handleClick={() => {
            handleClick(5);
            console.log("Ordenar por modified");
          }}
          direction={direction && activeIndexes[5]} // Pasar el valor booleano de direction
          order={() => handleOrder('modified', direction)}
        />
        <div style={styles.columnaDerecha}>Modified</div>
        <ClickableArrows
          isActive={activeIndexes[6]}
          handleClick={() => {
            handleClick(6);
            console.log("Ordenar por assign to");
          }}
          direction={direction && activeIndexes[6]} // Pasar el valor booleano de direction
          order={() => handleOrder('asignada', direction)}
        />
        <div style={styles.columnaDerecha}>Assign to</div>
      </div>
      <ShowIssues orderedIssues={sharedIssues} />
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
    color: 'blue'
  },
  tablaContainer: {
    display: "flex",
    flexDirection: "column",
    width: "100%",
  },
};

export default ColumnWithClickableArrows;