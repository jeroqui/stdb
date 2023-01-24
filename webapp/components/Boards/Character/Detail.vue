<template>
    <SkeletonBoardDetail v-if="loading" />
    <div v-else>
        <div class="flex">
            <div class="flex-grow pr-8">
                <h1 class="text-4xl ml-8 mt-8 font-black">
                    <UIField :text="character.name" default-text="Character Name" @change="(value) => editCharacter('name', value)" />
                </h1>
    
                <p>
                    {{ character.story || "no-description" }}
                </p>
            </div>
            <div class="h-80 w-60 shrink-0 bg-dark bg-opacity-20 rounded-xl"></div>
        </div>
    
        <BoardsCharacterRelationships />
    </div>

    <div class="mt-10">
        <BoardsCharacterHumanCC />
        <BoardsCharacterVampireCC />
        <hr>
        <BoardsCharacterVampireCC />
    </div>
</template>

<script lang="ts" setup>
const props = defineProps({
    detailId: {
        type: String,
    }
});

// If no detail was provided
// -> we want to create a new character instead of viewing or updating an existing one.
// If it was, we want to display that character's data.
const character = reactive({
    name: "",
    story: ""
});


let loading = ref(false);


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

if (props.detailId != "" && props.detailId != undefined) {
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
        character_id: props.detailId
    }

    
    
    const { loading:_loading, onResult } = useQuery<CharacterResult>(query, variables);

    loading = _loading;


    onResult(result => {
        // Save the data to a reactive reference so we can edit it.
        if ('data' in result) {
            character.name = result.data.character.name;
            character.story = result.data.character.story || "";
        }
    })
}


function editCharacter(element: string, value: string) {
    // TODO: character mutation
    switch (element) {
        case 'name':
            character.name = value;
            break;
    
        default:
            break;
    }
}

</script>