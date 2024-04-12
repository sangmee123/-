import axios from "axios"


// require()를 이용한 commonjs를 사용하는 동안 typescript 타이핑을 사용하려면
const axios = require('axios').default;

/* GET */

// 지정된 ID를 가진 유저에 대한 요청
axios.get('/user?ID=12345')
    .then(function (response){
        //success
        console.log(response);
    })
    .catch(function (error) {
        //error
        console.log(error);
    })
    .finally(function () {
        // 항상 실행되는 영역
    })

// 선택적으로 위의 요청은 다음과 같이 수행되기도 함
axios.get('user',{
    params: {
        ID: 12345
    }
    })
    .then(function (response){
        console.log(response);
    })
    .catch(function (error) {
        console.log(error);
    })
    .finally(function (){
        // 항상 실행되는 영역
    })

// async/await 사용을 원한다면, 함수 외부 'async' 키워드를 추가하세요
async function getUser() {
    try {
        const response = await axios.get('/user?ID=12345');
        console.log(response);
    } catch (error){
        console.error(error);
    }
}

/* POST */
axios.post('/user', {
    fistName: 'Fred',
    lastName: 'Flintstone'
})
.then(function (response){
    console.log(response);
})
.catch(function (error) {
    console.log(error);
})

// 여러 동시 POST 요청 생성
function getUserAccount(){
    return axios.get('/user/12345');
}

function getUserPermissions(){
    return axios.get('user/12345/permissions');
}

Promise.all([getUserAccount(), getUserPermissions()])
.then(function (results){
    const acct = results[0];
    const perm = results[1];
})


/* axios(config) */

// POST 요청 전송
axios({
    method: 'post',
    url: '/user/12345',
    data: {
        firstName: 'Fred',
        lastName: 'Flintstone'
    }
});

//node.js에서 GET 요청으로 원격 이미지 가져오기
axios({
    method: 'get',
    url: 'http://bit.ly/2mTM3nY',
    responseType: 'stream'
})
    .then(function (response){
        response.data.pipe(fs.createWriteStream('ada_lovelace.jpg'))
    })

/* axios(url, [config]) */

// GET 요청 전송 (기본값)
axios('/users/12345')


/* 인스턴스 만들기 -> axios.create([config]) */

const instance = axios.create({
    baseURL: 'https://some-domain.com/api',
    timeout: 1000,
    headers: {'X-Custom-Header': 'foobar'}
});

/* 요청 Config */
{
    // 서버에 요청에 사용될 서버 URL
    url: '/user',

    // method는 요청을 생성할때 사용되는 메소드
    method: 'get', // 기본값

    //'url'은 절대값이 아닌 경우 'baseURL'은 URL 앞에 붙는다.
    baseURL: 'https://some-domain.com/api',

    // 'transformRequest'는 요청 데이터를 서버로 전송하기 전에 변경할 수 있게 해줍니다.
    // 이것은 'PUT', 'POST', 'PATCH', 'DELETE' 메소드에서만 적용됩니다.
    // 마지막 함수는 Buffer, ArrayBuffer, FormData 또는 Stream의 인스턴스 또는 문자열을 반환해야 함
    // 헤더 객체를 수정할 수 있음
    transfromRequest: [function (data, headers) {
        // 데이터를 변환하려는 작업 수행
        return data;
    }],

    // 'transformResponse'는 응답 데이터가 then/catch로 전달되기 전에 변경할 수 있게 해줍니다.
    transformResponse: [function (data){
        // 데이터를 변환하려는 작업 수행
        return data;
    }],

    // 'headers'는 사용자 지정 헤더입니다
    headers: {'X-Requested-With': 'XMLHttpRequest'},

    // 'params'은 요청과 함께 전송되는 URL 파라미터입니다.
    // 반드시 일반 객체나 URLSearchParams 객체여야 함
    params: {
        ID: 12345
    },

    // 'paramsSerializer'는 'params'의 시리얼라이즈를 담당하는 옵션 함수
    // (예: https://www.npmjs.com/package/qs, http://api.jquery.com/jquery.param/)
    paramSerializer: function (params){
        return qs.stringify(params, {arrayFormat: 'brackets'})
    },

    // 'data'는 요청 바디로 전송될 데이터 입니다
    // 'put', 'post', 'patch', 'delete' 메서드에서만 적용 가능
    // 'transformRequest'가 설정되지 않은 경우 다음 타입 중 하나여야 함
    // - string, plain object, ArrayBuffer, ArrayBufferView, URLSearchParams
    // - 브라우저 전용: FormData, File, Blob
    // - Node 전용: Stream, Buffer
    data: {
        firstName: 'Fred'
    },

    
}