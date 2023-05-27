var idUsuario = 4;

const users = [
    {
        "id": 1,
        "username": "admin",
        "email": "admin@gmail.com",
        "token": 'eca034cf07dc9fcfce33ec777702d989bc794cbf',
    },
    {
        "id": 2,
        "username": "JoanTestSwagger",
        "email": "joan@email.com",
        "token": '',
    },
    {
        "id": 3,
        "username": "miguel",
        "email": "admin@gmail.com",
        "token": '',
    },
    {
        "id": 4,
        "username": "test1",
        "email": "test1@gmail.com",
        "token": "426c253f3b374f23678e18aba4394268c49a8508"
    }
]

//export const API_URL = "http://127.0.0.1:8000/api/";
export const API_URL = "https://it12casw-backend.fly.dev/api/";




export function getTokenUsuario() {

    var usuario = users.findIndex((usuario) => usuario.id == idUsuario);
    return users[usuario].token;
}

export function getIdUsuario() {
    return getUsuario();
}

export function getAllUsers() {
    return users;
}

export function getUsuario() {
    return idUsuario;
}

export function setUsuario(id){
    idUsuario = id;
}

export function getUsernameUsuario(){

    return users[users.findIndex((usuario) => usuario.id == idUsuario)].username;
}

