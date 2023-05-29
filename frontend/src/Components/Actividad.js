import React from 'react';

const styles = {
    actividad: {
        paddingLeft:"10px",
        paddingRight:"10px",

        borderRadius:"5px",
        marginTop:"5px",
        backgroundColor: 'rgba(236, 236, 236, 0.7)',
        paddingLeft:"10px",
        paddingRight:"10px",
        paddingTop:"3px",
        paddingBottom:"3px",
    },
    texto: {
        fontFamily: 'sans-serif',
        height: '20px',
        fontSize: '12px',
    },
};

function getUserRepresentation(user){
    if (typeof user === 'number' && Number.isInteger(user)){
        return user;
    }else {
        return user.username
    }
}

function getDataRepresentation(data){

    var dateTime = new Date(data);
    var formattedDateTime = dateTime.toLocaleString('en-GB', {
        hour: '2-digit',
        minute: '2-digit',
        day: '2-digit',
        month: '2-digit',
        year: 'numeric'
    });
    return formattedDateTime;
}

const Actividad = ({ activity }) => {
    return (
        <div style={styles.actividad}>
            <p style={styles.texto}>
                El usuario {getUserRepresentation(activity.usuario)} ha hecho una modificación de tipo {activity.tipo} con la fecha {getDataRepresentation(activity.fecha)}
            </p>
        </div>
    );
};

export default Actividad;