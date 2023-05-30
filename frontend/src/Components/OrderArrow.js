import React, { useState } from 'react';
import { orderIssues } from '../Controllers/issueCtrl';
import { RiArrowDownSFill, RiArrowUpSFill } from 'react-icons/ri';
import ShowIssues from "./ShowIssues";

const ClickableArrows = ({ isActive, handleClick, direction, order }) => {
  const handleArrowClick = async () => {
    await handleClick();
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

const ColumnWithClickableArrows = ({ sharedIssues, setSharedIssues, sharedUrl, setSharedUrl , parametros}) => {
  const [activeIndexes, setActiveIndexes] = useState({});
  const [direction, setDirection] = useState(true);
  const [order, setOrder] = useState(null);

  React.useEffect(() => {
    setActiveIndexes({});
  }, [sharedUrl]);
  
  React.useEffect(() => {
    console.log("Direction: " + direction)
    handleOrder(order);
  }, [order, direction]);
  
  const getActiveField = () => {
    if (activeIndexes[0]) {
      return "prioridad";
    } else if (activeIndexes[1]) {
      return "id";
    } else if (activeIndexes[2]) {
      return "issue";
    } else if (activeIndexes[3]) {
      return "status";
    } else if (activeIndexes[4]) {
      return "modified";
    } else if (activeIndexes[5]) {
      return "asignada";
    }
  };
  
  const handleClick = async (index, newOrder) => {
    await setActiveIndexes(async (prevState) => {
      const newActiveIndexes = { ...prevState };
      if (newActiveIndexes[index] && Object.keys(newActiveIndexes).length >= 1) {
        await setDirection(!direction);
      } else {
        Object.keys(newActiveIndexes).forEach((key) => {
          newActiveIndexes[key] = false;
        });
        newActiveIndexes[index] = true;
        await setDirection(false);
      }
      if (newActiveIndexes[index]) {
        setActiveIndexes(newActiveIndexes);
      } else {
        setActiveIndexes({});
      }
      return newActiveIndexes;
    });
    await setOrder(newOrder);
  };

  const handleOrder = async (field) => {
    if (field !== null) {
      const issues = await orderIssues(field, direction, sharedUrl);
      await setSharedIssues(issues);
    }
  };

  return (
    <div>
      <div style={styles.fila}>
        <ClickableArrows
          isActive={activeIndexes[0]}
          handleClick={() => {
            handleClick(0, 'prioridad');
            console.log("Ordenar por priority");
          }}
          direction={direction && activeIndexes[0]}
          
        />
        <div style={styles.columna}>Priority</div>
        <ClickableArrows
          isActive={activeIndexes[1]}
          handleClick={() => {
            handleClick(1, 'id');
            console.log("Ordenar por id");
          }}
          direction={direction && activeIndexes[1]}
          
        />
        <div style={styles.columna}>Issue</div>
        <ClickableArrows
          isActive={activeIndexes[2]}
          handleClick={() => {
            handleClick(2, 'issue');
            console.log("Ordenar por Assunto");
          }}
          direction={direction && activeIndexes[2]}
          
        />
        <div style={styles.columna}>Title</div>
        <div style={styles.columnaTexto}></div>
        <ClickableArrows
          isActive={activeIndexes[3]}
          handleClick={() => {
            handleClick(3, 'status');
            console.log("Ordenar por status");
          }}
          direction={direction && activeIndexes[3]}
        
        />
        <div style={styles.columnaDerecha}>Status</div>
        <ClickableArrows
          isActive={activeIndexes[4]}
          handleClick={() => {
            handleClick(4, 'modified');
            console.log("Ordenar por modified");
          }}
          direction={direction && activeIndexes[4]}
          
        />
        <div style={styles.columnaDerecha}>Date</div>
        <ClickableArrows
          isActive={activeIndexes[5]}
          handleClick={() => {
            handleClick(5, 'asignada');
            console.log("Ordenar por assign to");
          }}
          direction={direction && activeIndexes[5]}
          
        />
        <div style={styles.columnaDerecha}>Assign to</div>
      </div>
      <ShowIssues sharedIssues={sharedIssues} parametros={parametros} />
    </div>

  );
};

const styles = {
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
  fila: {
    display: "flex",
    flexDirection: "row",
    justifyContent: "space-between",
    alignItems: "center",
    padding: "10px 20px",
  },
  columna: {
    width: "15%",
  },
  columnaTexto: {
    width: "45%",
  },
  columnaDerecha: {
    width: "16%",
    textAlign: "left",
  },
};

export default ColumnWithClickableArrows;