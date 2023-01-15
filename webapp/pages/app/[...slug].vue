<template>
    <PartsPanel>
        <BoardsChronicleList v-if="store.board == boardNames.chroniclesList" />
        <BoardsCharacterList v-else-if="store.board == boardNames.charactersList" />
        <BoardsCharacterDetail
          v-else-if="store.board == boardNames.characterDetail"
          :detailId="$route.params.slug[1]"
        />
        <div v-else>{{ store.board }}</div>
    </PartsPanel>
</template>


<script setup>

import { boardNames, useDashboardStore } from '~~/stores/dashboardStore';

const store = useDashboardStore();

definePageMeta({
  layout: "dashboard",
});

</script>