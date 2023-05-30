import axios from "axios";
import { API_URL } from '../vars.js';

export async function getTokenUsuario() {
    
}

export async function getUsuariosCtrl() {
    try {
        var url = "https://it12casw-backend.fly.dev/api/users/";
        const response = await axios.get(url);
        
        for(var i = 0; i < response.data.length; i++){
            
        }

        return response.data;
    } catch (error) {
        console.log(error)
        return null;
    }
    return null;
}


export async function getUsuariosFullCtrl(params) {
    try {
        const url = API_URL + 'users/';

        const response = await axios.get(url, {
            params,
        });

        return response.data;
    } catch (error) {
        console.error(error);
        return null;
    }
}