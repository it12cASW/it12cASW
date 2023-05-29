
import React, { useEffect } from 'react';
import { useState } from "react"
import {getIdUsuario} from '../../vars'
import { BiSearch } from "react-icons/bi";



import { useParams } from 'react-router-dom';
import { getIssuesCtrl } from '../../Controllers/issueCtrl';
import { Link } from "react-router-dom";


// Controladores
import { getIssueCtrl } from '../../Controllers/issueCtrl';
import { getCommentsCtrl } from '../../Controllers/commentCtrl';
import { getActivitiesCtrl } from '../../Controllers/activityCtrl';
import {getUsuariosFullCtrl} from '../../Controllers/usuariosCtrl';
import {saveUsuario} from '../../Controllers/usuariosCtrl';

// Componentes
import IssueRow from '../../Components/IssueRow';
import Actividades from '../../Components/Actividades';
import Comments from '../../Components/Comments';
import Actividad from '../../Components/Actividad';
import User from '../../Components/User'


import axios from 'axios';

// Estilos

import { styles } from "./style"


// Pantallas


export default function Profile() {
    const [user, setUser] = useState('');
    const [username, setUsername] = useState('')
    const [usernameChange, setUsernameChange] = useState('')
    const [emailChange, setEmail] = useState('')


    useEffect(() => {
        const fetchUser = async () => {
           getUserFromApi();
        };

        fetchUser();
    },[]);

    if (!user) {
        return <div>No user found</div>;
    }

    async function getUserFromApi(){
        var params = null;
        var id_user = getIdUsuario();
        if (username==""){
            params = {
                id: id_user,
                serializer_type: 'full', // Replace with the desired serializer type
            };
        }else{
            params = {
                username: username,
                serializer_type: 'full', // Replace with the desired serializer type
            };
        }


        const userData = await getUsuariosFullCtrl(params);

        setUser(userData[0]);
    }

    function handleUsername(e) {
        setUsername(e.target.value);
    }

    function handleChangeUsername(e) {
        setUsernameChange(e.target.value);
    }

    function handleChangeEmail(e) {
        setEmail(e.target.value);
    }

    async function saveChanges(){
        try{
            const body = {
                "username": usernameChange,
                "email": emailChange
            }
            const userData = await saveUsuario(body);

            getUserFromApi()

        }catch (e){
            console.log(e)
        }


    }

    function getUserInfo(){
        if(username!=""){
            return (
                <div style={{width: "100%"}}>
                    <h2>User Information</h2>
                    <p>Username: {user.username}</p>
                    <p>Email: {user.email}</p>
                </div>
            );
        }else{
            return (
                <div style={{width: "100%"}}>
                    <h2>User Information</h2>
                    <p>Username:</p>
                        <input onChange={ handleChangeUsername }type="text" placeholder={user.username} defaultValue={ user.username }  />
                    <p>Email:</p>
                        <input onChange={ handleChangeEmail }type="text" placeholder={user.email} defaultValue={ user.email } />

                    <div style={{ position: "relative"}}>
                        <BiSearch
                            style={{ position: "absolute", top: "10px", left: "7px" }}
                        />
                        <button onClick={saveChanges} style={styles.Button}>
                            SaveChanges
                        </button>
                    </div>

                </div>
            );

        }
    }

    return (
        <div>
            <div style={{ alignContent:"center", width:"100%", display: "flex" , margin:"5px" }}>



                <input onChange={ handleUsername }type="text"  />
                <div style={{ position: "relative"}}>
                    <BiSearch
                        style={{ position: "absolute", top: "10px", left: "7px" }}
                    />
                    <button onClick={getUserFromApi} style={styles.Button}>
                        Search
                    </button>
                </div>

            </div>
            {getUserInfo()}
            <User user={user}></User>
        </div>
    );
}
