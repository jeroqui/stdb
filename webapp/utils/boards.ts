type Board = {
    name: string;
    component: string;
    is_detail: boolean;
    is_fullscreen: boolean;
}

class Boards {
    private boards: Board[];
    boardNames: {[k: string]: string};
    default: string;

    constructor() {
        this.boards = [];
        this.boardNames = {};
        this.default = "";
    }

    define(name: string, component: string, is_detail: boolean = false) {
        if (this.boards.length === 0){
            this.default = name
        }

        let board = {
            name,
            component,
            is_detail,
            is_fullscreen: false
        }
        this.boards.push(board)
        this.boardNames[name] = name
    }

    getBoardByName(name: string): Board {
        if (this.boardNames.hasOwnProperty(name)) {
            return this.boards.find(element => element.name === name)!
        }

        let defaultBoard = {
            name,
            component: "<h1>" + name + "</h1>",
            is_detail: false,
            is_fullscreen: false
        }

        return defaultBoard
    }

    getDefault():Board {
        // if it is default, it will be found, because it was set
        return this.getBoardByName(this.default)
    }
}


// Object to handle all boards.
let DashboardBoards = new Boards();

// Define all boards that we want to use
DashboardBoards.define("CHRONICLES_LIST", "BoardsChronicleList")
DashboardBoards.define("CHARACTERS_LIST", "BoardsCharacterListBoard")
DashboardBoards.define("CHRONICLE_DETAIL", "BoardsChronicleDetail", true)
DashboardBoards.define("CHARACTER_DETAIL", "BoardsCharacterDetail", true)

// This object can now be used to switch to a new board in any component
export {DashboardBoards}