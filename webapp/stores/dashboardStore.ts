import { defineStore } from "pinia"


const boardNames = {
    // Lists
    chroniclesList: "CHRONICLES_LIST",
    charactersList: "CHARACTERS_LIST",

    // Details
    chronicleDetail: "CHRONICLE_DETAIL",
    characterDetail: "CHARACTER_DETAIL"
};

let detailBoards = [
    boardNames.chronicleDetail,
    boardNames.characterDetail
]



const useDashboardStore = defineStore('boards', {
    state: () => ({
        chronicle: null,
        board: boardNames.chroniclesList,
        characters: [],
        locations: [],
        plots: [],
        sessions: []
    }),
    getters: {
        detail(): boolean {
            return detailBoards.includes(this.board);
        }
    },
    actions: {
        openBoard(boardName: string) {
            this.board = boardName;
        }
    },
})


export { boardNames, useDashboardStore }