

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

