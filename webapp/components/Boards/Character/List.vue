<template>
    <div class="mt-8">
        <BoardsCharacterListItem v-for="character in data?.chronicleCharacters" :key="character.id"
            :name="character.name" :pc="character.pc"
            @click="store.openBoard(DashboardBoards.boardNames.CHARACTER_DETAIL, character.id)" />
    </div>
</template>


<script lang="ts" setup>
import { useDashboardStore } from '~~/stores/dashboardStore';

const store = useDashboardStore();

// Data fetching
const query = gql`
query getCharacters($chronicle_id: PublicId!) {
	chronicleCharacters(chronicle: $chronicle_id) {
    id,
    name,
    pc
  }
}
`

type CharactersResult = {
    chronicleCharacters: {
        id: string;
        name: string;
        pc: boolean;
    }[]
}


const variables = {
    chronicle_id: store.chronicle
}
const { data, error } = await useAsyncQuery<CharactersResult>(query, variables);
</script>