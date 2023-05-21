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
                                <p>{ comment.autor.username }</p>
                                <p>{ comment.fecha }</p>
                            </div>
                            <div style={{ display:"flex", alignContent:"center", alignItems:"center", justifyContent:"center", borderWidth:"0.5px", border:"solid", borderRadius:"10px", backgroundColor:"white" }}>
                                <p>{ comment.contenido }</p>
                            </div>
                        </div>
                    ))}
                </div>
            ) : (
                <div>
                    <p>No hay comentarios</p>
                </div>
            )}
        </div>
    );
}

const styles = {
    comentario: {
        width:"100%",
        backgroundColor:"#FBC252",
        marginTop:"5px",
        borderRadius:"10px",
        padding:"10px"
    },
};