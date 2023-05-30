import React, { useState } from "react";
import { useEffect } from "react";

// Controllers
import { getAllUsers } from "../vars.js";
import { getIssue_usersCtrl } from "../Controllers/issueCtrl.js";
import { addWatcherCtrl } from "../Controllers/issueCtrl.js";
import { deleteWatcherCtrl } from "../Controllers/issueCtrl.js";





// 1.- Obtener usuarios 
// 2.- Obtener usuario de la issue
// 3.- Pintar todos los usuarios 
// 4.- Marcar los que estan en la issue




export default function Watchers({ id_issue }) {

    // Variables
    const [users, setUsers] = useState([]);
    const [watchers, setWatchers] = useState([]);

    /**
     * Obtiene los usuarios de la issue
     * @param {} id_issue
     */
    async function getIssue_usersAPI(id_issue) {

        var res = await getIssue_usersCtrl(id_issue);
        if (res) setWatchers(res);

    }

    /**
     * Añade un watcher a la issue
     * @param {} user_id
     */
    async function addWatcher(user_id) {
        
        var res = await addWatcherCtrl(id_issue, user_id);
        if(res) getIssue_usersAPI(id_issue);
        
    }

    /**
     * Elimina un watcher de la issue
     * @param {} user_id 
     */
    async function deleteWatcher(user_id) {

        var res = await deleteWatcherCtrl(id_issue, user_id);
        if(res) getIssue_usersAPI(id_issue);
    }   

    useEffect(() => {

        // Usuarios
        const users = getAllUsers();
        setUsers(users);

        // Usuarios de la issue
        getIssue_usersAPI(id_issue);

    }, [ id_issue ]);

    return (
        <div style={ styles.container}>
            {/* Recorre los usuarios */}
            <p>Marca para añadir watcher:</p>
            <div style={ styles.watcherContainer }>
            {users.map((user) => (
                <div key={user.id} style={ styles.watcher }>
                    {watchers.includes(user.id) ? <input type="checkbox" checked onClick={ () => deleteWatcher(user.id) } style={ styles.input }/> : <input type="checkbox" onChange={ () => addWatcher(user.id) } style={ styles.input } />}
                    <p>{ user.username }</p>
                </div>
            ))}
            </div>
        </div>
    );
}



const styles = {
    container: {
        width: "100%",
    },
    watcherContainer: {

    },
    watcher: {
        display: "flex",
        flexDirection: "row",
        alignItems: "center",
        padding: "1px",
    },
    input: {
        marginRight: "10px",
        width: "20px",
        height: "20px",
    },
}