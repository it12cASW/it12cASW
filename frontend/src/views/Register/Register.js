import React from 'react';
import axios from 'axios';
import { useNavigate } from "react-router-dom";



const Register = () => {

    function registrar() {
        // obten los valores de los campos input
        var nombre = document.querySelector('input[type="text"]').value;
        var apellidos = document.querySelector('input[type="text"]').value;
        var email = document.querySelector('input[type="text"]').value;
        var password = document.querySelector('input[type="password"]').value;
        var confirmarPassword = document.querySelector('input[type="password"]').value;

        // Haz una petición POST a la API
        axios.post('http://127.0.0.1:8000/polls/register', {
            params: {
                nombre: nombre,
                apellidos: apellidos,
                email: email,
                password: password,
                confirmarPassword: confirmarPassword,
            }
        })
        .then(function (response) {
            console.log(response);
        })
        .catch(function (error) {
            console.log(error);
        });   

    }


    return (
        <div style={ styles.mainContainer } >
            <div style={ styles.secondContainer } >
                <h1 style={ styles.titulo }>Register</h1>
                <div>
                    <div style={ styles.formStyle } >
                        <input type="text" style={ styles.input } placeholder='Nombre'/>
                        <input type="text" style={ styles.input } placeholder='Apellidos'/>
                        <input type="text" style={ styles.input } placeholder='Email'/>
                        <input type="password" style={ styles.input } placeholder='Password'/>
                        <input type="password" style={ styles.input } placeholder='Confirmar Password'/>
                        <button style={ styles.submitButton } onClick={ registrar } >Registrarme</button>
                    </div>
                </div>

            </div>
        </div>

    );
};



export default Register;

const styles = {
    mainContainer: {
        display: 'flex',
        flexDirection: 'column',
        width: '100%',
        border: '1px solid black',
        alignItems: 'center',
    },
    titulo: {
        fontSize: '30px',
        fontWeight: 'bold',
        alignSelf: 'center',
    },
    secondContainer: {
        display: 'flex',
        flexDirection: 'column',
        width: '50%',
        border: '1px solid blue',
    },
    formStyle: {
        display: 'flex',
        flexDirection: 'column',
        border: '1px solid black',
        
    },
    input: {
        padding: '10px',
        margin: '10px',
    },
    submitButton: {
        marginTop: '20px',
        height: '40px',
        width: '50%',
        alignSelf: 'center',
        backgroundColor: 'lightblue',
    },
};