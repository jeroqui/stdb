<template>
    <div class="flex justify-between">
        <h1 class="text-4xl font-black">Characters</h1>
        <UIButton @click="store.openBoard('CHARACTER_DETAIL')">New Character</UIButton>
    </div>

    <div class="mt-8">
        <BoardsCharacterListItem
            v-for="character in data?.chronicleCharacters"
            :key="character.id"
            :name="character.name"
            :pc="character.pc"
            @click="store.openBoard(boardNames.characterDetail, character.id)"
        />
    </div>
</template>

<script lang="ts" setup>
import { useDashboardStore, boardNames } from '~~/stores/dashboardStore';

const store = useDashboardStore();

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