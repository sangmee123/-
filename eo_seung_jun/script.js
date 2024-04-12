import http from 'k6/http';
import { sleep } from 'k6';

export default function () {
    const url = 'http://localhost:8000/test';
    // const todos = { text: "todo", date: "2024-04-04", done: false, color: "red" }

    // const payload = JSON.stringify(todos);

    const params = {

    };

    http.get(url, params);
    // http.post(url, payload, params);

    sleep(1);

}
