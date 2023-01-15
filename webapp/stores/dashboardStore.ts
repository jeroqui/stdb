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
        openBoard(boardName: string, detailId?: string) {
            this.board = boardName;
            if (detailId) {
                navigateTo("/app/" + (this.chronicle as any).id + "/" + detailId)
            }else {
                navigateTo("/app/" + (this.chronicle as any).id)
            }
        },
        switchToChronicle(chronicleId: string) {
            navigateTo("/app/" + chronicleId);
            (this.chronicle as any) = {
                id: chronicleId,
                name: "Test"
            }
            this.board = boardNames.charactersList;
        }
    },
})


export { boardNames, useDashboardStore }