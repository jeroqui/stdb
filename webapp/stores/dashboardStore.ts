import { defineStore } from "pinia"

import { DashboardBoards } from "~~/utils/boards";


const useDashboardStore = defineStore('boards', {
    state: () => ({
        chronicle: "",
        board: DashboardBoards.getDefault(),
        characters: [],
        locations: [],
        plots: [],
        sessions: []
    }),
    getters: {
        detail(): boolean {
            return this.board.is_detail;
        }
    },
    actions: {
        openBoard(boardName: string, detailId?: string) {
            this.board = DashboardBoards.getBoardByName(boardName)!;
            
            if (detailId) {
                navigateTo("/app/" + this.chronicle + "/" + detailId)
            }else {
                navigateTo("/app/" + this.chronicle)
            }
        }
    },
})


export { useDashboardStore }