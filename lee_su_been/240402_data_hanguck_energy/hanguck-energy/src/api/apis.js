import index from "./index";

export async function DataHanJun(query)
{   
    const query_list = Object.keys(query).reduce((acc, k) => {
        const text = `${k}=${query[k]}`;
        acc = [...acc, text];
        return acc;
    }, []);
    const query_text = query_list.join("&");
    console.log(query_text);
    return index.get(`http://localhost:8000?${query_text}`);
}

