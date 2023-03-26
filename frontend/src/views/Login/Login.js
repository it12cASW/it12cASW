import React from 'react';
import axios from 'axios';
import { Link, useNavigate } from "react-router-dom";



const Login = () => {


    function myfunction() {

        // obten los valores de los campos input
        var email = document.querySelector('input[type="text"]').value;
        var password = document.querySelector('input[type="password"]').value;
        var codigo = '';

        axios.get('http://127.0.0.1:8000/polls/login', {
            params: {
                email: email,
                password: password,
            }
        })
        .then(function (response) {
            window.location.assign('/panel');
        })
        .catch(function (error) {
            document.querySelector('.alerta').style.display = 'flex';
        });   
    }

    return (
        <div style={ styles.pantallaPrincipal }>

            <h1 style={ styles.tituloLogin } >Login</h1>

            <div style={ styles.mainContainer }>
                <input style={ styles.input } type="text" placeholder='email'/>
                <input style={ styles.input } type="password" placeholder='password'/>
                <button style={ styles.buttonInput } onClick={myfunction}>Click me</button>
            </div>

            <div class='alerta' style={ styles.alerta }>
                <h1>ALERTA</h1>
            </div>

            <Link to='/register' style={ styles.buttonRegistrarse } >Registrarse</Link>
        </div>
        
    );
};



export default Login;

const styles = {
    pantallaPrincipal: {
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        width: '100%',
    },
    tituloLogin: {
        fontSize: '50px',
    },
    mainContainer: {
        display: 'flex',
        flexDirection: 'column',
        padding: '20px',
        alignItems  : 'center',
    },
    input: {
        margin: '10px',
        width: '300px',
        height: '30px',
    },
    buttonInput: {
        marginTop: '20px',
        width: '100x',
        height: '30px',
    },
    buttonRegistrarse: {
        padding: '10px',
        backgroundColor: 'lightblue',
        color: 'white',
        textDecoration: 'none',
    },
    alerta: {
        display: 'none',
    },
};