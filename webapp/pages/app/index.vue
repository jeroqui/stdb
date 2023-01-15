<template>
    <PartsPanel>
        <BoardsChronicleList v-if="store.board == boardNames.chroniclesList" />
        <BoardsCharacterList v-else-if="store.board == boardNames.charactersList" />
    </PartsPanel>
</template>


<script setup>

import { boardNames, useDashboardStore } from '~~/stores/dashboardStore';

const store = useDashboardStore();

definePageMeta({
  layout: "dashboard",
});

</script>