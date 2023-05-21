import axios from "axios";

// Funciones de utilidad
import { getTokenUsuario } from "../vars.js";
import { getIdUsuario } from "../vars.js";

export async function getIssuesCtrl(idUsuario) {

    try {
        var url = "https://it12casw-backend.fly.dev/api/issues/";
        var auth = "Token " + getTokenUsuario(idUsuario);
        const response = await axios.get(url, {
            headers: {
                "Authorization": auth,
            }
        });
        return response.data;

    } catch (error) {
        console.log(error)
        return null;
    }
    return null;
}

export async function getIssueCtrl(id) {
    try {
        var idUsuario = getIdUsuario();
        var url = "https://it12casw-backend.fly.dev/api/issues/" + id + "/";
        var auth = "Token " + getTokenUsuario(idUsuario);
        const response = await axios.get(url, {
            headers: {
                "Authorization": auth,
            }
        });
        return response.data;

    } catch (error) {
        console.log(error)
        return null;
    }
    return null;
}

export async function crearIssueCtrl(idUsuario, data) {

    try {
        var url = "https://it12casw-backend.fly.dev/api/issues/create/";
        var auth = "Token " + getTokenUsuario(idUsuario);
        const response = await axios.post(url, data, {
            headers: {
                "Authorization": auth,
            }
        });
        console.log("La peticion ha funcionado")
        return response.data;

    } catch (error) {
        console.log(error)
        return null;
    }
    return true;
}

export async function editarIssueCtrl(id_issue, data){

    console.log("API: " + data.id_user + " issue: " + id_issue)
    try{
        var idUsuario = getIdUsuario();
        var url = "https://it12casw-backend.fly.dev/api/issues/" + id_issue + "/edit/";
        
        var auth = "Token " + getTokenUsuario(idUsuario);
        console.log("URL: " + url + " auth: " + auth + " id: " + idUsuario)
        const response = await axios.put(url, data, {
            headers: {
                "Authorization": auth,
            },
        });
        console.log("La peticion ha funcionado")
    }
    catch(error){
        console.log("API: La peticion no ha funcionado")
        return null;
    }
    return true;
}

export async function deleteAsociadoCtrl(id_issue){

    try {
        
        var idUsuario = getIdUsuario();
        var url = "https://it12casw-backend.fly.dev/api/issues/" + id_issue + "/associated/delete/";
        var auth = "Token " + getTokenUsuario(idUsuario);
        console.log("URL: " + url + " auth: " + auth)
        const response = await axios.delete(url, {
            headers: {
                "Authorization": auth,
            },
        });
        console.log("API: Se ha eliminado el asociado")
    }
    catch(error){
        if( error.response.status == 400 ){
            console.log("API: La issue no tiene nigun usuario asociado")
            return true;
        }
        else console.log("API: No se ha podido eliminar el usuario asociado")
        console.log(error)
        return null;
    }
    return true;
}

export async function setAsociadoCtrl(id_issue, asociado){
    try {

        var idUsuario = getIdUsuario();
        var url = "https://it12casw-backend.fly.dev/api/issues/" + id_issue + "/associated/";
        var data =
            {
                "idUser": asociado,
            };
        var auth = "Token " + getTokenUsuario(idUsuario);
        const response = await axios.put(url, data, {
            headers: {
                "Authorization": auth,
            },
        });
        console.log("API: Se ha asociado el usuario" )
        return true;
    }
    catch(error){
        if( error.response.status == 409 ){
            console.log("API: La issue ya tiene un usuario asociado")
            return false;
        }
        console.log("API: Ha habido un error al asociar el usuario")
        return null;
    }
}

export async function deleteAsignadoCtrl(id_issue) {

    try {
        var idUsuario = getIdUsuario();
        var url = "https://it12casw-backend.fly.dev/api/issues/" + id_issue + "/asigned/delete/";
        var auth = "Token " + getTokenUsuario(idUsuario);
        const response = await axios.delete(url, {
            headers: {
                "Authorization": auth,
            },
        });
        console.log("API: Se ha eliminado el asignado")
        return true;
    }
    catch(error){   
        if (error.response.status == 400) {
            console.log("API: No hay ningun usuario asignado")
            return true;
        }
        console.log(error)
        return null;
    }
}

export async function setAsignadoCtrl(id_issue, asignado) {

    try {
        var idUsuario = getIdUsuario();
        var url = "https://it12casw-backend.fly.dev/api/issues/" + id_issue + "/asigned/";
        var data =
            {
                "idUser": asignado,
            };
        var auth = "Token " + getTokenUsuario(idUsuario);
        const response = await axios.put(url, data, {
            headers: {
                "Authorization": auth,
            }
        });
        console.log("Se ha asignado el usuario")
        return true;
    }
    catch(error){
        console.log(error)
        return null;
    }
}

export async function deleteDeadlineCtrl(id_issue) {
    try {
        var idUsuario = getIdUsuario();
        var url = "https://it12casw-backend.fly.dev/api/issues/" + id_issue + "/deadline/delete/";
        var auth = "Token " + getTokenUsuario(idUsuario);
        const response = await axios.delete(url, {
            headers: {
                "Authorization": auth,
            }
        });
        console.log("API: Se ha eliminado el deadline")
        return true;
    }
    catch(error){
        if (error.response.status == 400) {
            console.log("API: No hay ningun deadline")
            return true;
        }
        console.log("API: Ha habido un error")
        return null;
    }
}

export async function setDeadlineCtrl(id_issue, deadline) {
    try {
        
        var idUsuario = getIdUsuario();
        var url = "https://it12casw-backend.fly.dev/api/issues/" + id_issue + "/deadline/";
        var data =
            {
            "deadline": deadline,
            "motivo": "sin Motivo"
          }
        var auth = "Token " + getTokenUsuario(idUsuario);
        const response = await axios.post(url, data, {
            headers: {
                "Authorization": auth,
            },
        });
        console.log("API: Se ha asignado el deadline")
        return true;
    }
    catch(error){
        if( error.response.status == 409 ){
            console.log("API: La issue ya tiene un deadline")
            return true;
        }
        console.log("API: Ha habido un error al asignar el deadline")
        return null;
    }
}
