var idUsuario = 1;

const users = [
    
    {
        "id": 1,
        "username": "Joan",
        "email": "joan@gmail.com",
        "token": "5c6592a04c2d7118a654c832e229c0bc0fe69fcf"
    },
    {
        "id": 2,
        "username": "Juan",
        "email": "juan@gmail.com",
        "token": "07cd0a379247eef201ab82b6eae04ba375d38e00"
    },
    {
        "id": 3,
        "username": "Dimas",
        "email": "dimas@gmail.com",
        "token": "e38eb83cb86bfc0205b2c4f8b352b799ca3faf7e"
    },
    {
        "id": 4,
        "username": "Miguel",
        "email": "miguel@gmail.com",
        "token": "4dcd1fd2c99b1cf289e7327fc047dea51c5d4915"
    },
]

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