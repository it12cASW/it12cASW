var idUsuario = 1;

const users = [
    
    {
        "id": 1,
        "username": "Joan",
        "email": "joan@gmail.com",
        "token": "d6ff5166a8c8289e27348c50b70de3c774a436a3"
    },
    {
        "id": 2,
        "username": "Juan",
        "email": "juan@gmail.com",
        "token": "7a45e7ce6c6e65e585295ccac0fa12023306c05a"
    },
    {
        "id": 3,
        "username": "Dimas",
        "email": "dimas@gmail.com",
        "token": "cab197b7acc1ae9e341164fe30e317adf6fa7061"
    },
    {
        "id": 4,
        "username": "Miguel",
        "email": "miguel@gmail.com",
        "token": "5cb63162fec93bcd049ece8c2d4a9e1b5da997a4"
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