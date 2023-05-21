import React from "react";
import { useEffect } from "react";

// Controladores
import { getCommentsCtrl } from '../Controllers/issueCtrl';

export default function Comments({issue}) {

    const [comments, setComments] = React.useState(null);

    async function getCommentsAPI(id) {
        var comments_aux = await getCommentsCtrl(id);
        setComments(comments_aux.comments);
    }

    useEffect(() => {

        // Obtengo issue y comentarios y actividades
        getCommentsAPI(issue);

    }, []);

    return(
        <div style={{ alignSelf:"center", width:"70%", maxHeight:"500px"}}>
            <div>
                <h1>Comentarios</h1>
            </div>
            {comments && comments.length > 0 ? (
                <div style={{ width:"100%" }}>
                    {comments.map((comment) => (
                        <div style={ styles.comentario }>
                            <div style={{ display:"flex", flexDirection:"row", justifyContent:"space-around" }}>
                                <p style={ styles.texto }>{ comment.autor.username }</p>
                                <p style={ styles.texto }>{ comment.fecha }</p>
                            </div>
                            <div style={{ display:"flex", alignContent:"center", alignItems:"center", justifyContent:"center", borderRadius:"10px", backgroundColor:"white" }}>
                                <p style={ styles.texto }>{ comment.contenido }</p>
                            </div>
                        </div>
                    ))}
                </div>
            ) : (
                <div>
                    <p style={ styles.texto }>No hay comentarios</p>
                </div>
            )}
        </div>
    );
}

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