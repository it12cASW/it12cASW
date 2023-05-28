import axios from "axios";


export async function getTokenUsuario() {
    
}

export async function getUsuariosCtrl() {
    try {
        var url = "https://it12casw-backend.fly.dev/api/users/";
        const response = await axios.get(url);
        
        for(var i = 0; i < response.data.length; i++){
            
        }
        console.log(response.data);
        return response.data;
    } catch (error) {
        console.log(error)
        return null;
    }
    return null;
}