<template>
    <h1 class="text-4xl font-black">{{ result.character.name }}</h1>

    {{ result.character.story }}
</template>

<script lang="ts" setup>
const props = defineProps({
    detailId: {
        type: String
    }
})

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

const { result, error } = useQuery(query, variables);



</script>