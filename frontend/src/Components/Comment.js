import React from 'react';

const styles = {
    comentario: {
        width:"100%",
        backgroundColor:"rgba(236, 236, 236, 0.9)",
        marginTop:"5px",
        borderRadius:"10px",
        padding:"10px"
    },
    texto: {
        fontFamily: 'sans-serif',
        height: '20px',
        fontSize: '15px',
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


const Comment = ({ comment }) => {
    return (
        <div style={ styles.comentario }>
            <div style={{ display:"flex", flexDirection:"row", justifyContent:"space-around" }}>
                <p style={ styles.texto }>{ getUserRepresentation(comment.autor) }</p>
                <p style={ styles.texto }>{ getDataRepresentation(comment.fecha) }</p>
            </div>
            <div style={{ display:"flex", alignContent:"center", alignItems:"center", justifyContent:"center", borderRadius:"10px", backgroundColor:"white" }}>
                <p style={ styles.texto }>{ comment.contenido }</p>
            </div>
        </div>
    );
};

export default Comment;