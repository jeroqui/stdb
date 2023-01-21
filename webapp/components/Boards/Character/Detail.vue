<template>
    <div class="flex">
        <div class="flex-grow pr-8">
            <h1 class="text-4xl ml-8 mt-8 font-black">{{ character.name || "Name" }}</h1>
        
            <p>
                {{ character.story || "no-description" }}
            </p>
        </div>
        <div class="h-80 w-60 bg-dark bg-opacity-20 rounded-xl"></div>
    </div>

    <!-- Add a table of contents of existing CCs to quickly go to info. -->

    <BoardsCharacterRelationships />

    <div class="mt-10">
      <BoardsCharacterHumanCC />
      <BoardsCharacterVampireCC />
      <div class="text-center">
        ---
      </div>
      <BoardsCharacterVampireCC />
    </div>
</template>

<script lang="ts" setup>
import { useDashboardStore } from '~~/stores/dashboardStore';


// If no detail was provided
// -> we want to create a new character instead of viewing or updating an existing one.
// If it was, we want to display that character's data.
const character = reactive({
    name: "",
    story: ""
});

const store = useDashboardStore();


type CharacterResult = {
    character: {
        id: string;
        name: string;
        pc: boolean;
        story?: string;
        relationshups?: {
            feeling: string;
            character2: {
                id: string;
            }
        }[]
    }
};


if (store.detailId != "" && store.detailId != undefined) {
    // If we have a detail id, we want to fetch that character's data.
    const query = gql`
  query getCharacter($character_id: PublicId!) {
    character(id: $character_id) {
      id,
      name,
      pc,
      story,
      relationships {
        feeling,
        character2 {
          id
        }
      }
    }
  }
  `

    const variables = {
        character_id: store.detailId
    }


    const { data, error } = await useAsyncQuery<CharacterResult>(query, variables);

    // Save the data to a reactive reference so we can edit it.
    if ('value' in data) {
        character.name = data.value?.character.name!;
        character.story = data.value?.character.story || "";
    }
}




</script>