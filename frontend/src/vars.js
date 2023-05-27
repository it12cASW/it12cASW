

const users = [
    {
        id: 0,
        username: 'miguel',
        token: '9538cdddef7cef4b4a997b2d3f921052125ebe99',
        email: 'admin@gmail.com'
    },
    {
        id: 2,
        username: 'JoanTestSwagger',
        token: '',
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

