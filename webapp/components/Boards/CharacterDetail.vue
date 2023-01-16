<template>
    <h1 class="text-4xl font-black">{{ data.character?.name || "Name" }}</h1>

    {{ data.character?.story || "no-description" }}
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

const { data, error } = await useAsyncQuery(query, variables);



</script>