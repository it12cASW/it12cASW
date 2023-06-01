var idUsuario = 5;

const users = [
    // {
    //     "id": 4,
    //     "username": "test1",
    //     "email": "test1@gmail.com",
    //     "token": "426c253f3b374f23678e18aba4394268c49a8508"
    // },
    {
        "id": 5,
        "username": "Joan",
        "email": "joan@gmail.com",
        "token": "e76f2d82a326de231b8ff7b4d2ff8199132fe258"
    },
    {
        "id": 6,
        "username": "Juan",
        "email": "juan@gmail.com",
        "token": "d50b877a60295604c95ac06aa03f9e769c4b3898"
    },
    {
        "id": 7,
        "username": "Dimas",
        "email": "dimas@gmail.com",
        "token": "a6fff97a4599b1667a60e89a2c8c0d2d31efdd3a"
    },
    {
        "id": 8,
        "username": "Miguel",
        "email": "miguel@gmail.com",
        "token": "b3b2975d0de2df62a1cde575f22e98025b131db2"
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



const users = [
    {
        id: 1,
        username: 'admin',
        token: 'eca034cf07dc9fcfce33ec777702d989bc794cbf',
        email: 'admin123@gmail.com'
    },
    {
        id: 2,
        username: 'JoanTestSwagger',
        token: '08c02c5150c2fe158b7ac2d2774371e9db4167ac',
        email: 'sdfs@∫dfs.com',
    },
    {
        id: 3,
        username: 'JoanTestSwagger2',
        token: '',
        email: 'sdfs@∫dfs.com',
    },
];



export function getTokenUsuario(id_usuario) {
    return users[0].token;
}

export function getIdUsuario() {
    return users[0].id;
}

export function getAllUsers() {
    return users;
}

