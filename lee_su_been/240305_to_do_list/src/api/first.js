import index from './index';

export async function RequestToken(){
    return index.get('/url')
}

export async function GetToken(code, state){
    return index.get(`/token?code=${code}&state=${state}`)
}