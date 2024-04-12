<template lang="pug">
div.wrapper
    div.content
    div.data
        div.data-item(v-for="item in currentPageData" :key="item.id") {{ item.text }}
        div.pagination
            router-link.page-number(v-for="pageNumber in pageCount" :key="pageNumber" :to="{ path: $route.path, query: { page: pageNumber } }" @click.native="changePage(pageNumber)") {{ pageNumber }}
</template>

<script>
export default {
    data() {
        return {
            pageCount: 5, // 페이지 수
            currentPage: 1, // 현재 페이지
            pageSize: 6, // 페이지당 아이템 수
            dummyData: [], // 더미 데이터
            scrollPosition: 0 // 스크롤 위치
        };
    },
    computed: {
        currentPageData() {
            const startIndex = (this.currentPage - 1) * this.pageSize;
            const endIndex = startIndex + this.pageSize;
            return this.dummyData.slice(startIndex, endIndex);
        }
    },
    methods: {
        generateDummyData() {
            // 페이지별로 다른 데이터 생성
            for (let page = 1; page <= this.pageCount; page++) {
                const pageData = [];
                for (let i = 0; i < this.pageSize; i++) {
                    pageData.push({ id: (page - 1) * this.pageSize + i + 1, text: `Page ${page} - Item ${i + 1}` });
                }
                this.dummyData = this.dummyData.concat(pageData);
            }
        },

        changePage(pageNumber) {
            this.currentPage = pageNumber;
        },
    },
    created() {
        this.generateDummyData();
        this.$watch( // 라우트 변경 감지
            () => this.$route.query.page,
            () => {
                const pageNumber = parseInt(this.$route.query.page) || 1;
                this.currentPage = pageNumber;
            }
        );
    }
};
</script>

<style lang="stylus">
.wrapper
    border-radius: 20px
    display: flex
    flex-direction: column
    justify-content: center
    align-items: center
    padding: 20px 0
    gap: 1rem

.label
    font-size: 20px

.content
    border: 1px solid rgb(221,221,221)
    border-radius: 10px
    background-color: #656565
    width: 30%
    height: 200px
    overflow-y: auto

.pagination
    margin-top: auto;
    margin-bottom: 20px; 
    text-align: center

.page-number
    text-decoration: none
    margin: 0 10px

.data
    flex-wrap: wrap

.data-item
    width: 100%
    margin-right: 1rem
    margin-bottom: 1rem
    padding: 4rem
    background-color: #f0f0f0
    border-radius: 8px
</style>
