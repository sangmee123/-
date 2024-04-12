<template lang="pug">
.data-table
    table
        thead
            tr
                th(v-for="(header, index) in headers" :key="index") {{ header }}
        tbody
            tr(v-for="(row, rowIndex) in rows" :key="rowIndex")
                td(v-for="(cell, cellIndex) in row" :key="cellIndex") {{ cell }}
</template>

<script>
import axios from 'axios';

export default {
data() {
    return {
        headers: [], // 테이블 헤더
        rows: [] // 테이블 데이터
    };
},
mounted() {
    this.getData();
},
methods: {
    async getData() {
        try {
            const spreadsheetId = '1A9jVQw5IdimIi_W-NKXaMiVQ3KZMSHVqZDl1x5LaWeU'; 
            // const spreadsheetId = '1fQ5XiIBlJYLSAguQARaZ2dLnadoHqUolQHHeETamA1k';
            const range = '시트1';
            // const range = '메인페이지';
            const response = await axios.get(`/api/get_spreadsheet_data/${spreadsheetId}/${range}`);
            this.headers = response.data.shift(); // 첫 번째 행은 헤더로 설정하고 제거
            this.rows = response.data;
        } catch (error) {
            console.error('Error fetching data:', error);
        }
    }
}
};
</script>

<style lang="stylus">
/* 필요한 스타일 추가 */
</style>
